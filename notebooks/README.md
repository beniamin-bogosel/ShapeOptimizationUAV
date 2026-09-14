# Python supplements for Labs 1–9

Each student notebook contains **two programming exercises in English**, with
mathematical statements, explicit code tasks, starter functions, plotting cells,
checks and written discussion prompts. Allow approximately 60–90 minutes per
pair, depending on Python experience. These are supplementary activities or
homework; the original 90-minute mathematical labs remain the core schedule.

| Lab | Exercise 1 | Exercise 2 | Student notebook | Worked solutions |
| --- | --- | --- | --- | --- |
| 1 | Compare equal-perimeter shapes | Heron's reflection and a grid search | [Lab 1](lab-01-models-and-reflection.ipynb) | [Solutions](solutions/lab-01-models-and-reflection.ipynb) |
| 2 | Locate the Fermat point on a triangular grid | Observe the transition at 120 degrees | [Lab 2](lab-02-fermat-point.ipynb) | [Solutions](solutions/lab-02-fermat-point.ipynb) |
| 3 | Fixed-area rectangle with backtracking descent | Gradient fields and unstable step sizes | [Lab 3](lab-03-gradient-descent.ipynb) | [Solutions](solutions/lab-03-gradient-descent.ipynb) |
| 4 | Tangent ascent on an ellipse | Improve a convex polygon at fixed perimeter | [Lab 4](lab-04-constraints-and-polygons.ipynb) | [Solutions](solutions/lab-04-constraints-and-polygons.ipynb) |
| 5 | Regular polygons under both normalizations | Dido with a polygonal free boundary | [Lab 5](lab-05-isoperimetry-and-dido.ipynb) | [Solutions](solutions/lab-05-isoperimetry-and-dido.ipynb) |
| 6 | Hinge angle and area gain | Fixed-side quadrilaterals and cyclic optimality | [Lab 6](lab-06-hinges-and-quadrilaterals.ipynb) | [Solutions](solutions/lab-06-hinges-and-quadrilaterals.ipynb) |
| 7 | Raster symmetric difference and missed thin features | Hausdorff distance and distance functions | [Lab 7](lab-07-shape-distances.ipynb) | [Solutions](solutions/lab-07-shape-distances.ipynb) |
| 8 | Support functions and directional widths | Random convex polygons at minimum width one | [Lab 8](lab-08-support-and-width.ipynb) | [Solutions](solutions/lab-08-support-and-width.ipynb) |
| 9 | Polygonal Minkowski sums and mixed-area coefficients | The matching cut and rectangle-union areas | [Lab 9](lab-09-mixed-areas-and-box-cuts.ipynb) | [Solutions](solutions/lab-09-mixed-areas-and-box-cuts.ipynb) |

## Start Jupyter

Use Python 3.10 or newer. From the course repository:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r notebooks/requirements.txt
python -m ipykernel install --user --name shape-optimization --display-name "Shape Optimization"
python -m jupyterlab notebooks
```

Select the **Shape Optimization** kernel in the notebook. An existing Python
environment containing these packages also works. On Windows, activate the
environment with `.venv\Scripts\activate` instead of the `source` command.
GitHub can display saved notebooks and figures, but running code requires a
Jupyter kernel. The notebooks use no external datasets, network calls or local
helper modules: each is self-contained and can be copied independently.

## How to use the exercises

Run the setup cell, read the mathematical statement, then complete the functions
marked `TODO`. A starter function returns `None`, and its demonstration prints
an instruction until the task is completed. This lets **Run All** open a clean
student notebook without deliberate exceptions. It does **not** mean an
unfinished student notebook has passed the mathematical checks. Those checks
run only once the task returns a result.

Rerun both the function-definition cell and its demonstration after an edit.
Use the provided checks as feedback, adapt the plots as requested, and write
explanations in the response cells. Finish with **Restart Kernel and Run All**.
The solution notebooks include completed code, discussion guidance and saved
figures. Distribute the student versions separately when solutions should be
withheld; both versions are visible if this entire repository is published.

Labs 1–2 use geometric and grid searches before differentiation is introduced.
Lab 3 introduces gradients and step-size control. Lab 4's polygon exercise is
the most demanding algorithm: the gradient and convexity helpers are supplied,
so students can concentrate on tangent steps, feasibility and backtracking.
The later notebooks explicitly distinguish finite searches from proofs, and
point-cloud, boundary, pixel and angular approximations from their continuous
counterparts.

## Validation and maintenance

The `.ipynb` files are the editable sources. From the repository root:

```bash
python scripts/validate_notebooks.py
python scripts/validate_notebooks.py --execute
python scripts/validate_notebooks.py --execute --kind solutions --write-solutions
```

The first command validates notebook structure and the two-exercise pairing.
The second executes all 18 notebooks, each in a fresh kernel, and saves copies
under ignored `build/notebooks/`. The third refreshes the saved solution outputs.
Execution checks include analytic optima, area/perimeter constraints, gradient
finite differences, descent/ascent, approximation errors, metric identities and
width bounds. Student stubs are checked for a clean startup; the completed
solutions run all numerical assertions and must render figures.

The default validation kernel is `python3`. If you followed the named-kernel
setup above, append `--kernel shape-optimization` to the execution commands.
The chosen kernel must have the requirements installed. No package installation
is performed by a notebook or by the validator.
Use `--lab 9` (or several lab numbers) to validate and execute only selected
labs; pairing and consecutive numbering are still checked for the collection.

## API references

- [NumPy: absolute basics for beginners](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [Matplotlib: pyplot introduction](https://matplotlib.org/stable/tutorials/pyplot.html)
- [SciPy ConvexHull](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.ConvexHull.html): 2D hull vertex order and area/perimeter naming.
- [SciPy nearest-neighbor queries](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.cKDTree.query.html): distances used in Lab 7.
- [NBClient execution](https://nbclient.readthedocs.io/en/latest/client.html): fresh-kernel notebook validation.

Mathematical references and manuscript locations are in the
[course source map](../SESSION_PLAN.md#source-map-and-editorial-choices).
