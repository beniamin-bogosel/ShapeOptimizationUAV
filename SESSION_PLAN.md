# Shape Optimization — first eight sessions

English course materials for Aurel Vlaicu University of Arad. Each session
consists of **90 minutes of course + 90 minutes of lab**: 24 contact hours in
total. The core labs are mathematical seminars; no programming environment is
required for them. Each lab also has two optional Python exercises in a
supplementary Jupyter notebook; see the section below. Students need elementary Euclidean geometry, single-variable
calculus, vectors and basic linear algebra. Partial derivatives and gradients
are introduced in Session 3.
Sessions 7–8 use basic compactness, uniform convergence and integration;
the required Arzelà–Ascoli theorem is stated, with an optional proof in
the instructor notes.

The progression follows the requested outline and the existing chapters and
2025 manuscripts. The new material is an edited teaching draft, not a verbatim
transcription. Proofs of the general existence and optimality results begin in
Session 3. Session 2 states the planar isoperimetric theorem and presents the
catenary as a model and candidate, without proving those results.
Sessions 5–6 return to planar isoperimetry: regular-polygon comparisons and
scaling lead to a proof by polygonal approximation, then geometric improvement
arguments determine the equality case and expose the classical existence gap.
Sessions 7–8 supply a general compactness and existence framework, establish
continuity for convex shapes, and study area optimization with width constraints.

| Session | Course, 90 minutes | Lab, 90 minutes |
| --- | --- | --- |
| 1 | Generalities, models and geometric examples | Modeling, projection, Heron's reflection problem |
| 2 | Isoperimetric heuristics, catenary, failures of attainment | Torricelli/Fermat point: minimizing TA + TB + TC |
| 3 | Direct method, convexity, uniqueness, first-order conditions in 1D and nD | Fixed-area rectangle, existence examples, minimum distances, quadratics |
| 4 | Taylor formula, steepest ascent, level sets, one and several equality constraints | Multipliers and polygonal isoperimetric inequality; optional Fermat revisit |
| 5 | Regular polygons; equivalent formulations; convex hull; polygonal approximation; Dido | Monotonicity, scaling, the limit argument and free-shoreline geometry |
| 6 | Area/perimeter bisectors; Steiner hinge; cyclic quadrilaterals; existence and equality | Reflection, area variations, quadrilateral formulas and logical gaps |
| 7 | L¹ and Hausdorff distances; properties; distance functions; Blaschke via Arzelà–Ascoli | Metrics, counterexamples, diameter, convexity and the selection proof |
| 8 | Direct method; support functions; convex continuity; constant and minimum width; Pál's inequality | Support examples, confinement, continuity and the incircle area calculation |

## Materials and build

- [Course notes](pdf/course-notes.pdf), editable master [course-notes.tex](course-notes.tex), with one source per session in `sessions/`.
- [Student lab sheets](pdf/lab-sheets.pdf), editable master [lab-sheets.tex](lab-sheets.tex), with one source per lab in `labs/`.
- [Instructor notes and solutions](pdf/instructor-notes.pdf), editable master [instructor-notes.tex](instructor-notes.tex), solutions in `instructor/solutions.tex`, `instructor/solutions-05-06.tex` and `instructor/solutions-07-08.tex`.

Run `make` from this folder to regenerate all three PDFs. It requires GNU Make
and a TeX installation with pdfLaTeX, AMS packages, Latin Modern, microtype,
geometry, TikZ, booktabs, tabularx, enumitem and hyperref. It uses two LaTeX
passes. Auxiliary files and build logs are in ignored `build/`; the finished
PDFs are in `pdf/`. Diagrams are drawn in TikZ, so the build does not depend
on the original slides' absolute image paths or on sibling folders.

The course and lab PDFs are for students. Keep the instructor PDF separate
when distributing exercises. Optional material does not add to the 90-minute
core. Lecture notes are a reference for board work, not a script that must be
read in full during class. Timings below include interaction and feedback;
no separate break has been deducted.

## Supplementary Python notebooks

All eight labs have **two additional programming exercises** in English.
The [notebook index](notebooks/README.md) links the student notebooks, separate
worked solutions, dependency list and instructions for running Jupyter.
The `.ipynb` files are self-contained and remain editable independently of
the LaTeX material. The solution versions contain saved plots and discussion
guidance; student versions provide starter functions and checks.

| Lab | Supplementary exercise 1 | Supplementary exercise 2 |
| --- | --- | --- |
| 1 | Plot and compare equal-perimeter shapes | Heron's reflection versus a sampled search |
| 2 | Fermat point on a triangular grid | The 120-degree transition on an angle bisector |
| 3 | Backtracking descent for a fixed-area rectangle | Gradient fields and step-size stability |
| 4 | Project a gradient onto an ellipse tangent | Improve a convex polygon at fixed perimeter |
| 5 | Both regular-polygon normalizations and convergence rates | Dido with discretized free arc length |
| 6 | Fixed-bar hinge motion and reflected area | Fixed-side quadrilaterals and cyclic optimality |
| 7 | Raster symmetric difference and vanishing thin features | Hausdorff distance through nearest neighbors |
| 8 | Support functions and constant/minimum width | Normalize random convex polygons to minimum width one |

Allow roughly 60–90 minutes per pair, or assign the exercises separately as
homework. These times are additional to the 24-hour core programme. Students
need basic Python functions, loops and arrays; geometry and plotting helpers
are supplied. Derivative-based algorithms start in Lab 3. The polygon ascent
exercise in Lab 4 is the most demanding and includes the gradients and a
convexity test so students can focus on constraint handling.

Assessment can use four items: correct implementation, constraint/error
checks, legible plots, and an explanation of the numerical limitations.
The notebooks emphasize the difference between sampled comparisons and
global mathematical conclusions. Numerical existence evidence is never used
in place of the compactness arguments in Sessions 7–8.

`python scripts/validate_notebooks.py --execute` runs each student and solution
notebook in a fresh kernel. Incomplete student tasks report what to finish;
all mathematical assertions run in the completed solution versions. The
validator also checks that each notebook contains exactly two exercises.

## Session 1 — generalities and examples

**Outcome:** students can state the design variable, objective and admissible
class of a geometric optimization problem and distinguish a candidate from a
global optimum.

| Course time | Activity |
| --- | --- |
| 0–10 | Opening question: what can be optimized about a shape? Start with a scalar minimum. |
| 10–25 | Introduce the admissible class, functional, infimum, minimum value and minimizer. |
| 25–40 | Shortest path and point-to-line distance; a bound and its equality case. |
| 40–60 | Area and perimeter, hanging chain, networks, surface and structural models. |
| 60–75 | Parametric, boundary and topology variations; what each model permits. |
| 75–85 | Existence, uniqueness, identification and approximation as separate questions. |
| 85–90 | Exit task: formulate a model with one explicit constraint. |

| Lab time | Activity |
| --- | --- |
| 0–15 | Exercise 1.1: formulate models and compare three equal-perimeter shapes. |
| 15–35 | Exercise 1.2: projection onto a line and onto a segment. |
| 35–65 | Exercise 1.3: Heron's reflection problem, calculation and geometric proof. |
| 65–80 | Exercise 1.4: shrinking disks and the effect of a fixed-area constraint. |
| 80–90 | Synthesis: feasibility, universal bound and equality case. |

**Board/materials:** ruler, a simple map or drawing of a route, a string loop
if available. Invite students to supply application examples without requiring
PDE background. The general reflection formula is optional homework.

## Session 2 — basic examples and the existence question

**Outcome:** students can explain the two isoperimetric formulations and the
chain's objective/constraints, and identify ways a best value may fail to be
attained. The lab establishes the geometric Torricelli result from a supplied
construction fact.

| Course time | Activity |
| --- | --- |
| 0–10 | Recall equal-perimeter comparisons and introduce the disk candidate. |
| 10–30 | State the isoperimetric inequality; scaling, two formulations and shoreline variant. |
| 30–45 | Dents and symmetry as improvement heuristics; why a candidate argument needs existence. |
| 45–65 | Demonstrate a hanging chain; fixed endpoints, length and gravitational energy; catenary formula. |
| 65–80 | Excluded endpoint, escape to infinity and unbounded perimeter at fixed area. |
| 80–85 | Draw fine teeth approaching a straight boundary; discuss what happens to length. |
| 85–90 | Exit task: a necessary property of an optimizer versus attainment. |

| Lab time | Activity |
| --- | --- |
| 0–10 | Exercise 2.1: equilateral-triangle warm-up. |
| 10–30 | Exercise 2.2: external equilateral construction and the 120-degree angle check. |
| 30–50 | Exercise 2.3: perpendicular side lines, auxiliary equilateral triangle and Viviani's identity. |
| 50–75 | Exercise 2.4: comparison with distances to lines and uniqueness. |
| 75–90 | Present the proof, identify the supplied construction fact, discuss the 120-degree threshold. |

**Board/materials:** a chain or cord hung between two supports; compass and
ruler for the lab. Give the concurrency/interior-location construction fact
rather than spending the lab proving it. State the obtuse-angle result during
the closing discussion; its full proof and a coordinate example are optional.
Do not require differentiation of the distance sum yet.

## Session 3 — theory of optimization

**Outcome:** students can give the finite-dimensional direct-method proof,
state the hypotheses for uniqueness, and use derivatives to identify and then
verify minimizers.

| Course time | Activity |
| --- | --- |
| 0–10 | Global/local minimizers, infimum and minimizing sequences. |
| 10–35 | Weierstrass proof; admissible limit; lower semicontinuity and coercive sublevels. |
| 35–50 | Convex sets/functions; local-to-global argument; strict convexity and uniqueness. |
| 50–70 | Fermat's condition in 1D, boundary/nonsmooth exceptions, partial derivatives and gradient in nD. |
| 70–85 | A quadratic example: stationarity plus a global comparison; discuss positive definite matrices. |
| 85–90 | Exit task: counterexamples to three common incorrect implications. |

| Lab time | Activity |
| --- | --- |
| 0–15 | Exercise 3.1: diagnose attainment and identify missing hypotheses. |
| 15–40 | Exercise 3.2: minimal-perimeter rectangle at fixed area, including existence. |
| 40–60 | Exercise 3.3: minimum distances using a quadratic parameterization. |
| 60–80 | Exercise 3.4: stationary point, saddle and the role of the feasible set. |
| 80–90 | Present existence, identification and uniqueness separately. |

**Pacing:** prove Weierstrass and strict-convexity uniqueness at the board.
Explain lower semicontinuity with the displayed limit inequality; advanced
function-space compactness is outside scope. The eigenvalue-based coercivity
estimate for a general quadratic is supplementary reading if needed. Two
lines in space and analytic Torricelli existence are optional follow-ups.

## Session 4 — constraints and multipliers

**Outcome:** students can use the first-order Taylor term to interpret ascent
and descent, explain normality to regular level sets, check the constraint
rank, and write and interpret one- and multiple-constraint Lagrange systems.

| Course time | Activity |
| --- | --- |
| 0–10 | Why constraints are natural; compare free and plane-constrained distance. |
| 10–30 | Taylor formula, directional derivative, Cauchy–Schwarz and steepest ascent. |
| 30–40 | Chain rule along a level curve; gradient orthogonality and feasible tangents. |
| 40–60 | One equality constraint; geometric multiplier argument and nearest point on a plane. |
| 60–75 | Several constraints, independent gradients, worked two-constraint example. |
| 75–85 | Singular constraint and minimum/maximum candidates; rectangle recap as time permits. |
| 85–90 | Exit task: assumptions before solving, verification after solving. |

| Lab time | Activity |
| --- | --- |
| 0–15 | Exercise 4.1: rectangle with one equality constraint. |
| 15–30 | Exercise 4.2: area of the regular n-gon and its limiting value. |
| 30–40 | Vertex variables, perimeter/area formulas, supplied existence and nondegeneracy lemma. |
| 40–60 | Exercise 4.3: local gradients, scaling identities, constraint regularity and multiplier sign. |
| 60–80 | Exercise 4.4: adjacent sides equal, then exterior angles equal. |
| 80–90 | Assemble the inequality, equality case and the role of existence. |

**Pacing:** the compactness and nondegeneracy lemma is supplied to students;
its proof is instructor background. If the algebra takes longer, supply the
cotangent identity and have students interpret it. Optional homework is a
second two-constraint example or a gradient-based return to the Fermat point.
This return is deliberately optional so the main Fermat seminar stays in
Session 2 and polygonal isoperimetry has the full Lab 4 slot.

## Session 5 — the isoperimetric inequality and polygonal approximation

**Outcome:** students can prove that regular-polygon perimeters decrease at
fixed area and areas increase at fixed perimeter, transfer competitors between
the two formulations by dilation, and explain how approximation establishes
the planar bound and disk attainment.

| Course time | Activity |
| --- | --- |
| 0–10 | State the two optimization problems and the admissible Jordan/convex classes; recall Lab 4. |
| 10–25 | Derive both regular n-gon formulas; compare examples and conjecture the disk. |
| 25–35 | Prove monotonicity of n tan(pi/n) and compute the disk limits. |
| 35–50 | Prove equivalence of the two formulations by rescaling arbitrary competitors. |
| 50–60 | Convex hull, perimeter budget and dilation; reduce to convex regions. |
| 60–80 | State the inscribed-polygon approximation lemma; prove the inequality and disk attainment; isolate the equality question. |
| 80–90 | Dido along a straight shore: reflection, the correct constant and free endpoints; exit question. |

| Lab time | Activity |
| --- | --- |
| 0–15 | Exercise 5.1: formulas, table and separate sketches for the two normalizations. |
| 15–30 | Exercise 5.2: rigorous monotonicity and limits. |
| 30–45 | Exercise 5.3: concrete scaling contradictions and limits of the method. |
| 45–65 | Exercise 5.4: pass from arbitrary inscribed polygons to the planar inequality. |
| 65–80 | Exercise 5.5: free-shoreline optimization and comparison with a closed fence. |
| 80–90 | Synthesis: dependencies of the proof and the outstanding equality case. |

**Difficulty and pacing:** polygonal approximation belongs in the core because
Lab 4 already supplied the polygonal inequality, including its finite-dimensional
existence lemma. Give the area-convergence lemma during the course and use the
short limit argument. Its explicit cap estimate and the convex-hull projection
proof are instructor background or optional lab extensions. Convergence of the
inscribed perimeters is not needed; an upper bound by the original perimeter
suffices. This avoids introducing general shape-space compactness.

**Board/materials:** calculator for the table, compass/ruler for the polygons,
and a sketch of the reflected shoreline region. The notes include equal-area
polygon and Dido diagrams. Do not present the numerical table as a proof, or
infer uniqueness of the disk merely from strict inequalities for finite polygons.

## Session 6 — Steiner's arguments and the existence gap

**Outcome:** students can explain the precise consequences of reflection,
identify the area increase in a hinge motion, use the quadrilateral area formula
correctly, and distinguish characterization of a hypothetical optimizer from a
proof that the optimum is attained.

| Course time | Activity |
| --- | --- |
| 0–10 | Temporarily assume a maximizer; convexification and exclusion of straight boundary segments. |
| 10–25 | Existence of area-bisecting lines; prove area/perimeter bisection implications; distinguish these from symmetry. |
| 25–45 | Half-region, two rigid caps, hinge angle and Thales: each optimal half is a half-disk. |
| 45–60 | General quadrilateral area formula, cyclic equality case and rhombus/square illustration. |
| 60–75 | Select four noncyclic boundary points; a small area-increasing flex with fixed side lengths and caps. |
| 75–90 | Existence gap, failure of an improvement-rule inference, and synthesis with Session 5 to obtain all equality cases. |

| Lab time | Activity |
| --- | --- |
| 0–15 | Exercise 6.1: reflection comparisons and the unsupported symmetry inference. |
| 15–35 | Exercise 6.2: hinge-area formula, numerical illustration and admissibility. |
| 35–55 | Exercise 6.3: Brahmagupta versus the general formula; cyclic maximum and circular reasoning. |
| 55–70 | Exercise 6.4: differentiate through the diagonal to justify a small improving flex. |
| 70–80 | Exercise 6.5: every other candidate can improve, but the distinguished candidate need not maximize. |
| 80–90 | Synthesis: planar bound, actual attainment and equality classification. |

**Pacing:** the half-region argument is the main geometric proof; the four-hinge
method is a second perspective. Supply the general quadrilateral formula in
class. Its cosine-law derivation and existence of a cyclic quadrilateral with
given sides are optional instructor material. Use a small improving motion:
neither proof needs the entire flex to its target to remain intersection-free.
The moved boundary must remain simple; it need not remain convex because the
admissible class includes nonconvex Jordan regions. The instructor notes spell
out local separation of the pieces without presupposing a smooth optimizer.

**Logical order:** the geometric arguments alone characterize an optimizer
conditional on existence. Session 5 has already established the universal bound
and exhibited an attaining disk, so applying the hinge arguments now also proves
that all equality shapes are disks. Reflection then gives the half-disk equality
case for Dido with free endpoints.

## Session 7 — sequences of shapes and compactness

**Outcome:** students can distinguish L¹ and Hausdorff convergence, prove
basic Hausdorff properties, and obtain a compact-set selection theorem
from uniform convergence of distance functions.

| Course time | Activity |
| --- | --- |
| 0–10 | Return to minimizing sequences: convergence, admissibility and objective behavior. Fix the measurable-set and compact-set settings. |
| 10–25 | Characteristic functions, symmetric difference, equality modulo null sets and area continuity in L¹. |
| 25–45 | Directed excess, Hausdorff metric, neighborhood inclusions and the metric properties. |
| 45–60 | Thin extension and fine grid; point-limit properties, convexity, diameter and degeneration. |
| 60–85 | Distance functions, supremum-norm identity, statement of Arzelà–Ascoli and the Blaschke selection proof. |
| 85–90 | Exit task: why the zero set must be shown to have distance function equal to the uniform limit. |

| Lab time | Activity |
| --- | --- |
| 0–15 | Exercise 7.1: pseudometric, interval formula and directed excess. |
| 15–35 | Exercise 7.2: exact distances in both counterexamples and the actual thin-extension limit. |
| 35–45 | Exercise 7.3: failure of intersection continuity. |
| 45–65 | Exercise 7.4: distance-function identity, diameter estimate and convexity of limits. |
| 65–80 | Exercise 7.5: recover a set from the uniform limit of distance functions. |
| 80–90 | Synthesis: confinement, degeneration and what remains for existence. |

**Pacing:** the main proof is Blaschke via Arzelà–Ascoli, not a second proof
of Arzelà–Ascoli itself. The latter, connectedness of limits, nested-set
convergence and volume upper semicontinuity are supplementary instructor
material or optional lab extensions. The sequence of nearest points used to
identify the limiting distance function may depend on the evaluation point;
the uniformly convergent sequence of functions remains the same.

**Topology convention:** use ordinary Hausdorff distance on nonempty compact
sets. Henrot–Pierre also define convergence of open domains by Hausdorff
distance between their compact complements in a fixed container. The new
notes explicitly distinguish these conventions. For ordinary compact-set
Hausdorff convergence, connectedness is preserved, diameter is continuous,
and volume is upper semicontinuous; volume need not be continuous. No
boundary regularity is assumed in the general selection theorem.

## Session 8 — existence, convexity and width

**Outcome:** students can apply the direct method on a Hausdorff-closed class,
use support functions to control geometric functionals, and distinguish area
optimization at constant width from area minimization at prescribed minimum
width. The latter has the equilateral triangle as its unique shape up to rigid
motions, with the prescribed altitude.

| Course time | Activity |
| --- | --- |
| 0–15 | Direct method on the compact space of shapes; closed constraints, continuous objectives and lower semicontinuity. |
| 15–35 | Signed support functions, examples, reconstruction by supporting half-spaces and the Hausdorff metric identity. |
| 35–50 | Directional/minimum width, diameter and constant-width examples; mechanisms for area and perimeter continuity. |
| 50–65 | Existence at fixed perimeter and constant width; minimum-width area sublevels supply the missing diameter bound. |
| 65–85 | State Pál's theorem; incircle contact construction, supplied geometric lemmas and the tangent-area formula. |
| 85–90 | Exit task: confinement versus closedness; minimum width versus constant width. |

| Lab time | Activity |
| --- | --- |
| 0–15 | Exercise 8.1: support functions of disks and rectangles; three width examples. |
| 15–30 | Exercise 8.2: width and area continuity; the segment limit and extended perimeter. |
| 30–45 | Exercise 8.3: area–diameter bound, translated minimizing sequence and attainment. |
| 45–65 | Exercise 8.4: one tangent region, three disjoint contributions and the lower bound F(r). |
| 65–80 | Exercise 8.5: derivative sign, endpoint values, equality and rescaling. |
| 80–90 | Synthesis: existence and identification, and the different constant-width class. |

**Difficulty and pacing:** prove the support-function metric identity at the
board; explain area continuity through homothetic inclusions and state
Cauchy's projection formula with its polygonal mechanism. Full approximation
details and inradius/circumradius continuity are instructor background. Supply
the incircle contact lemma, separation of the three tangent regions, and the
derivative identity in the guided lab. The instructor notes prove the geometric
inputs and give the differentiation. This keeps the technical identification
argument from displacing the core existence theory.

**Important distinctions:** minimum width alone does not bound diameter;
area sublevels do. Perimeter is extended continuously to twice the length
of a segment, which is different from the boundary's one-dimensional measure.
Support functions can be negative and determine only the convex hull of a
nonconvex set. The equilateral triangle has the required minimum width but
does not have constant width. Existence of area extrema among constant-width
bodies is proved here; identifying their area minimizer is outside this session.

## Source map and editorial choices

These are local source references in the parent course-content folder. The
new PDFs remain self-contained if this repository is copied elsewhere.
Manuscript page numbers refer to PDF pages, not handwritten numbering.

| New material | Existing source |
| --- | --- |
| Session 1 and Lab 1 | `../Chapter_1/chapter1_SHO.tex`: introductory definitions, distance and Heron problems, examples, representations; `../Notes/SHO_2025_Curs1.pdf`, pp. 1–10 |
| Session 2 course | Chapter 1: isoperimetry and hanging-chain motivation; `../Notes/SHO_2025_Curs2.pdf`, pp. 1–4 |
| Session 2 lab | `../Labs/Lab2.tex`, first geometric method; `../Notes/SHO_2025_Curs2.pdf`, pp. 5–12; construction also pictured in Curs1, pp. 5–7 |
| Session 3 course and rectangle lab | `../Chapter_2/chapter2_SHO.tex`: existence, uniqueness, first-order conditions, quadratic; `../Notes/SHO_2025_Curs3.pdf`, pp. 1–25 |
| Session 4 course | Chapter 2: constraints and multipliers; `../Notes/SHO_2025_Curs4.pdf`, pp. 1–11 |
| Session 4 polygon lab | `../Notes/SHO_2025_Curs4.pdf`, pp. 12–15: vertex variations, perimeter/area gradients, equal sides and angles |
| Session 5 regular polygons | Blåsjö, “Zenodorus's polygon proof,” printed pp. 528–529 (PDF pp. 3–4) |
| Session 5 approximation and existence | Blåsjö, “Existence for polygons,” printed pp. 542–543 (PDF pp. 17–18); the polygonal theorem already proved in Lab 4 |
| Session 5 Dido | Treibergs, Section 2, p. 3; Blåsjö's introductory discussion, printed p. 526 (PDF p. 1) |
| Session 6 half-region hinge and existence gap | Blåsjö, printed pp. 532–535 (PDF pp. 7–10), especially the first four-hinge argument on pp. 533–534 |
| Session 6 quadrilateral formula and four hinges | Treibergs, Sections 4–5, pp. 7–10; Blåsjö, printed p. 534 (PDF p. 9) |
| Session 7 metrics and selection | `../Notes/SHO_2025_Curs7.pdf`, pp. 2–11; Henrot–Pierre, Sections 2.2.2–2.2.3 and 2.2.6.1, especially Theorem 2.2.25 and Proposition 2.2.27 |
| Session 8 direct method and convex continuity | Curs7, pp. 12–14; `../Notes/SHO_2025_Curs8.pdf`, pp. 3–6; Henrot–Pierre, Chapter 2 |
| Session 8 support functions and width | Curs8, pp. 7–11 |
| Session 8 minimum-width inequality | Curs8, pp. 12–16; Yaglom–Boltyanskii, Chapter 6, Exercises 6-2 and 6-4 (printed pp. 59–60), solutions pp. 215–217 and 221–222 |

The isoperimetric references consulted for Sessions 5–6 are:

- Andrejs Treibergs, *Inequalities that Imply the Isoperimetric Inequality*,
  March 4, 2002: [local PDF](../Doc_Isoperimetric/isopTreibergs.pdf),
  [University of Utah copy](https://www.math.utah.edu/~treiberg/isoperim/isop.pdf).
- Viktor Blåsjö, *The Isoperimetric Problem*, *The American Mathematical
  Monthly* 112(6), 2005, pp. 526–566:
  [local PDF](../Doc_Isoperimetric/blasjo526Isoperimetric_proofs.pdf),
  [publication record](https://research-portal.uu.nl/en/publications/the-isoperimetric-problem/).

**Reference corrections and qualifications:** Treibergs' shoreline discussion
on p. 3 omits a factor of one half from the optimal area. For free arc length L,
the correct value is L²/(2π), as follows from his reflection construction.
The quadrilateral formula without an angle term is Brahmagupta's cyclic formula;
for a general convex quadrilateral we retain the correction term, commonly
called Bretschneider's formula. The early circular-cap application in Treibergs
uses the planar isoperimetric inequality, so it cannot serve as an independent
proof of the quadrilateral inequality used to establish planar isoperimetry.

The new half- and four-hinge presentations use local improving motions and
explicitly discuss admissibility; no convergence of an iterated hinge procedure
is claimed. The short cap estimate for polygonal approximation, the worked
scaling and Dido exercises, and the bounded-supremum logical counterexample
are added teaching details. The 2005 article's more advanced convergence and
functional-analytic proofs are not required for these two sessions.

The additional references consulted for Sessions 7–8 are:

- Antoine Henrot and Michel Pierre, *Shape Variation and Optimization:
  A Geometrical Analysis*, EMS, 2018, Chapter 2. The local PDF is
  `../(EMS Tracts in Mathematics) Antoine Henrot, Michel Pierre - Shape Variation and Optimization _ A Geometrical Analysis-Euopean Mathematical Society (2018).pdf`.
  Ordinary compact-set Hausdorff distance is introduced on printed p. 30
  (PDF p. 43); the selection theorem and distance-function proof are on
  printed pp. 42–44 (PDF pp. 55–57).
- I. M. Yaglom and V. G. Boltyanskii, *Convex Figures*, Holt, Rinehart
  and Winston, 1961, Chapter 6, “Various exercises on maxima and minima.”
  The local file is
  `../I. M. Yaglom, V. G. Boltyanskii-Convex Figures.-New York_ Holt, Rinehart & Winston 1961..djvu`.
  Printed pp. 59–60 correspond to DjVu pages 72–73; the relevant solutions
  on printed pp. 215–217 and 221–222 correspond to DjVu pages 228–230
  and 234–235.

The minimum-width presentation follows the manuscript's incircle and tangent
regions, using one-variable calculus for the final comparison. The notes add
an explicit proof that the three added regions have disjoint interiors and
an area-sublevel diameter bound before applying Blaschke. The proof does not
assume that the three contact directions are equally spaced. Pál's equality
case follows from the equality case of the incircle radius bound. These
details make the existence and identification arguments independently usable.

The written chapters are English Beamer sources; the relevant handwritten
notes are Romanian and were inspected visually. They were used to check the
sequence and arguments, not automatically OCR-transcribed.

Additions include explicit 90-minute schedules, student outcomes, complete
lab solutions, a precise energy/length formulation for the chain, illustrative
TikZ diagrams, a worked two-constraint example, the angle-at-least-120-degree
Fermat case, and a full instructor proof of the polygon existence lemma.
The second Ptolemy-based method in the old Lab 2 is not needed for the core
90-minute lab; the original file remains available in the source folder.

The new presentation makes several assumptions explicit: uniqueness requires
strict convexity on a convex feasible set; compactness in Euclidean space
does not automatically establish compactness of shapes; multipliers require
independent constraint gradients; tangency only preserves a curved constraint
to first order; and stationarity alone is not a proof of global minimality.
The Session 2 heuristics are labeled as such. Historical priority claims and
industry-specific numbers in the old slides are not needed for these sessions.
