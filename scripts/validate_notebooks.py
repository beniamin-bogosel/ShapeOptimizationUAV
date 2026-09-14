#!/usr/bin/env python3
"""Validate all course notebooks; optionally execute each in a fresh kernel."""
import argparse
from pathlib import Path
import os
import re
import sys

import nbformat
from nbclient import NotebookClient


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--execute', action='store_true')
    parser.add_argument('--kind', choices=['all', 'student', 'solutions'], default='all')
    parser.add_argument('--kernel', default='python3', help='Installed Jupyter kernel name.')
    parser.add_argument('--lab', type=int, nargs='+', help='Restrict checks to selected lab numbers.')
    parser.add_argument('--write-solutions', action='store_true',
                        help='Save successful executed solution outputs in their source notebooks.')
    args = parser.parse_args()
    if args.write_solutions and not args.execute:
        parser.error('--write-solutions requires --execute')
    root = Path(__file__).resolve().parents[1]
    directory = root / 'notebooks'
    students = sorted(directory.glob('lab-*.ipynb'))
    solutions = sorted((directory / 'solutions').glob('lab-*.ipynb'))
    numbers = [int(re.match(r'lab-(\d+)-', p.name).group(1)) for p in students]
    if (not students or numbers != list(range(1, len(students)+1))
            or {p.name for p in students} != {p.name for p in solutions}):
        raise ValueError('Expected consecutively numbered student notebooks with matching solutions.')
    paths = students + solutions if args.kind == 'all' else (
        students if args.kind == 'student' else solutions)
    if args.lab:
        if not set(args.lab).issubset(numbers):
            parser.error('Requested lab number is not present in the notebook collection.')
        paths = [p for p in paths if int(re.match(r'lab-(\d+)-', p.name).group(1)) in args.lab]
    cache = root / 'build' / 'notebooks'
    if args.execute:
        cache.mkdir(parents=True, exist_ok=True)
        os.environ.setdefault('MPLCONFIGDIR', str(cache / 'matplotlib'))
        os.environ.setdefault('JUPYTER_RUNTIME_DIR', str(cache / 'runtime'))
    failed = []
    for path in paths:
        label = str(path.relative_to(root))
        try:
            nb = nbformat.read(path, as_version=4)
            nbformat.validate(nb)
            headings = [c.source for c in nb.cells if c.cell_type == 'markdown'
                        and re.match(r'^## Exercise \d+\.\d+:', c.source)]
            if len(headings) != 2:
                raise ValueError('Exactly two numbered programming exercises are required.')
            solved = path.parent.name == 'solutions'
            tag = 'solution' if solved else 'task'
            if sum(tag in c.metadata.get('tags', []) for c in nb.cells) != 2:
                raise ValueError(f'Expected two cells tagged {tag!r}.')
            if nb.metadata.shape_optimization.version != ('solutions' if solved else 'student'):
                raise ValueError('Version metadata does not match the notebook location.')
            if args.execute:
                for cell in nb.cells:
                    if cell.cell_type == 'code':
                        cell.outputs = []
                        cell.execution_count = None
                client = NotebookClient(nb, timeout=120, kernel_name=args.kernel,
                                        allow_errors=False,
                                        resources={'metadata': {'path': str(path.parent)}})
                client.execute()
                executed_code = [c for c in nb.cells if c.cell_type == 'code']
                if any(c.execution_count is None for c in executed_code):
                    raise ValueError('Some code cells did not execute.')
                if solved:
                    pictures = sum('image/png' in output.get('data', {})
                                   for c in executed_code for output in c.outputs)
                    if pictures < 2:
                        raise ValueError('Expected at least one rendered figure per exercise.')
                    text = '\n'.join(output.get('text', '')
                                     for c in executed_code for output in c.outputs)
                    if 'then rerun this cell' in text:
                        raise ValueError('An unfinished task remains in a solution notebook.')
                target = path if solved and args.write_solutions else (
                    cache / ('solution-' if solved else 'student-') / path.name)
                target.parent.mkdir(parents=True, exist_ok=True)
                nbformat.write(nb, target)
            print(('EXECUTED ' if args.execute else 'VALID ') + label, flush=True)
        except Exception as exc:
            failed.append(label)
            print(f'FAILED {label}: {exc}', file=sys.stderr, flush=True)
    if failed:
        print(f'{len(failed)} notebook(s) failed.', file=sys.stderr)
        return 1
    print(f'All {len(paths)} notebooks passed.', flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
