# DGCV: Differential Geometry with Complex Variables

DGCV is an open-source Python package providing basic tools for differential geometry integrated with systematic organization of structures accompanying complex variables, in short, Differential Geometry with Complex Variables.

At its core are fully featured symbolic representations of standard DG objects such as vector fields and differential forms, defined relative to standard or complex coordinate systems. As systems of differential geometric objects constructed from complex variables inherit natural relationships from the underlying complex structure, DGCV tracks these relationships across the constructions. Immediate advantages of the uniform integration are seen in smooth switching between real and holomorphic coordinate representations of mathematical objects. In computations, DGCV classes dynamically manage this format switching on their own so that typical complex variables formulas can be written plainly and will simply work. Some examples of this: In coordinates $z_j = x_j + iy_j$, expressions such as $\frac{\partial}{\partial x_j}|z_j|^2$ or $d z_j \wedge d \overline{z_j} \left( \frac{\partial}{\partial z_j}, \frac{\partial}{\partial y_j} \right)$ are correctly parsed without needing to convert everything to a uniform variable format. Retrieving objects' complex structure-related attributes, like the holomorphic part of a vector field or pluriharmonic terms from a polynomial is straightforward. Complexified cotangent bundles and their exterior algebras are easily decomposed into components from the Dolbeault complex and Dolbeault operators themselves can be applied to functions and k-forms in either coordinate format.

DGCV was developed using Python 3.12, with dependencies on the SymPy and Pandas libraries in addition to base Python. Its classes integrate SymPy objects within their data structures and subclass from SymPy.Basic, thereby inheriting much of SymPy’s functionality. For instance, one can apply sympy.simplify() directly to most DGCV class objects. Developing complete compatibility with SymPy is a goal still in progress. Pandas is used to format and display data in a more readable manner.

## Features
- Fully featured symbolic representations of vector fields, differential forms, and tensor fields
- Intuitive interactions with complex structures from holomorphic coordinate systems: DGCV objects dynamically manage coordinate transformations between real and holomorphic coordinates during computation as necessary, so objects can be represented in and freely converted between either coordinate format at any time. 
- Dedicated python classes for representing common differential geometric structures including Riemannian metrics, Kahler structures, and more
- Custom LaTeX rendering for clean visual representation of mathematical objects, ideal for sharing mathematical ideas through clear Jupyter notebooks.

## Installation

You can install DGCV directly from PyPI with pip:

```bash
pip install DGCV
```

Note, depending on the operating system, a command like `python3` (for macOS/ Linux) or `py` (for windows) should proceed `pip`.

## Tutorials

Two Jupyter Notebook tutorials are available to help getting started with DGCV:

1. **DGCV Introduction**: An introduction to the key concepts and setup
   - [View DGCV Introduction Tutorial](https://www.realandimaginary.com/dgcv/tutorials/DGCV_introduction/)

2. **DGCV in Action**: A quick tour through examples from some of the library's more elaborate functions
   - [View DGCV in Action Tutorial](https://www.realandimaginary.com/dgcv/tutorials/DGCV_in_action/)


### Running the Tutorials Locally

If you clone the DGCV github repository, you can run the tutorials locally with Jupyter:

```bash
git clone https://github.com/YikesItsSykes/DGCV.git
cd DGCV/tutorials
jupyter notebook DGCV_introduction.ipynb
jupyter notebook DGCV_in_action.ipynb
```
Or download the tutorials individually from the repository [DGCV github repo](https://github.com/YikesItsSykes/DGCV).

## Documentation
DGCV documentation is hosted at [https://www.realandimaginary.com/dgcv/](https://www.realandimaginary.com/dgcv/), with documentation pages for each function in the library and more. Full documentation is under development, so for now, refer to the docstrings within the code for more information on available classes/methods and functions.

## License
DGCV is licensed under the MIT License. See the `LICENSE.txt` file for more information.

## Author
DGCV was created and is maintained by [David Sykes](https://www.realandimaginary.com).

---

### Future Development
The current (0.x.x) version of DGCV is foundation on which a lot more can be built. Many additions for future updates are planned, including:
 - Extending complex variable handling and dynamic coordinate-type conversion automations. The simple goal is to fully automate handling of complex variable formats, allowing input to be formatted freely with any coordinate type, with features to fully control coordinate type formatting or let the sytems automate the process. The current API meets this goal for interactions with DGCV's core classes, but it is not fully extended to some ancillary classes. For example, full coordinate conversion features are implemented for differential forms but not yet for general tensor fields.
 - Expanding libraries dedicated to specialized areas of differential geometry including, Symplect/Contact Hamiltonian formalism, CR structures, Riemannian and Kahler, Sasakian, etc.

Contributions and feedback from anyone interested are warmly welcomed.
Stay tuned for more updates!
