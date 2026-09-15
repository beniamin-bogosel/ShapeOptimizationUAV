# ShapeOptimizationUAV
Materials for shape optimization course at Aurel Vlaicu University of Arad Romania

Testing

Course 1.

## First eleven sessions — English

Each session consists of a 90-minute course and a 90-minute lab.
See the [session plan and source map](SESSION_PLAN.md) for the timetable,
learning outcomes, teaching suggestions and links to last year's material.

| Session | Course | Lab |
| --- | --- | --- |
| 1 | Introduction and shape optimization examples | Models, projections and Heron's problem |
| 2 | Isoperimetric heuristics, catenary, existence questions | Torricelli/Fermat point in a triangle |
| 3 | Existence, convexity, uniqueness, first-order conditions | Fixed-area rectangle and distance problems |
| 4 | Gradients, Taylor formula and equality constraints | Polygonal isoperimetric inequality |
| 5 | Regular polygons, equivalent formulations, polygonal approximation, Dido | Scaling, monotonicity, limit argument and shoreline problem |
| 6 | Steiner's hinge arguments, cyclic quadrilaterals and the existence gap | Bisectors, two- and four-cap constructions, proof logic |
| 7 | L¹ and Hausdorff distances; Blaschke selection via Arzelà–Ascoli | Counterexamples, distance functions and compactness |
| 8 | Existence, support functions, convex continuity, constant and minimum width | Confinement, admissible limits and Pál's triangle inequality |
| 9 | Mixed areas and volumes; Brunn–Minkowski by box induction; isoperimetry | Parallel bodies, matching cuts, mixed coefficients and geometric inequalities |
| 10 | Constant width; support characterization; existence; Chakerian’s proof | Smooth examples, the covering hexagon and a mixed-area plateau |
| 11 | Tangent-polygon proof and equality; Reuleaux approximation; variational proof | Paired cuts, regular Reuleaux polygons and constrained gradients |

- [Course notes — PDF](pdf/course-notes.pdf)
- [Student lab sheets — PDF](pdf/lab-sheets.pdf)
- [Instructor notes and solutions — PDF](pdf/instructor-notes.pdf)

Editable LaTeX sources are in `sessions/`, `labs/` and `instructor/`.
Run `make` in this directory to rebuild the PDFs; see
[build requirements](SESSION_PLAN.md#materials-and-build).

Sessions 5–6 draw on the local Treibergs and Blåsjö references. The polygonal
approximation argument establishes the inequality and disk attainment;
Steiner's arguments characterize the equality case. Detailed source locations
and the correction to Treibergs' shoreline area formula are in the session plan.

Sessions 7–8 use the corresponding manuscripts, Henrot–Pierre's Chapter 2
and Yaglom–Boltyanskii's Chapter 6. They develop the direct method for convex
shapes and prove that an equilateral triangle minimizes area at prescribed
minimum width. Each lecture and lab remains 90 minutes; longer geometric
proofs are collected in the instructor notes.

Session 9 follows Schneider and Treibergs. The elementary induction on unions
of rectangular boxes is proved in any dimension; mixed areas and the planar
Steiner formula lead to isoperimetry. General mixed volumes are introduced
through their polynomial coefficients and first variation, with advanced
theory left outside the core.

Sessions 10–11 develop constant-width shapes and the Blaschke–Lebesgue
theorem. Chakerian’s mixed-area proof is followed by the equiangular
tangent-polygon proof, including equality, and a variational proof using
Reuleaux polygons. The instructor notes include the area derivative,
Lagrange multipliers, Blaschke motions, the classical three-arc reduction,
and further mixed-volume connections. The source map identifies supplied
lemmas and optional material from the three requested papers.

## Supplementary Python exercises

Each of the eleven labs has a Jupyter notebook with **two additional programming
exercises**: English statements, starter code, plotting tasks, checks and
discussion prompts. Separate worked solution notebooks include executed figures.

See the [notebook index and setup instructions](notebooks/README.md) for all
eleven pairs. Topics include geometric searches, gradient descent, constrained
polygon improvement, Dido, hinge motions, shape distances, minimum width,
mixed areas, the box-cut construction, constant-width support functions,
covering hexagons, tangent refinement and Reuleaux-pentagon variations.
These supplements can be assigned as homework or additional computer sessions;
the original mathematical lab schedule remains 90 minutes.
