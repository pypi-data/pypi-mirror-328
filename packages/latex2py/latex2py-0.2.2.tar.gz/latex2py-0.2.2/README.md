# LaTeX-to-Python Parser (`latex2py`)

This is a lightweight **LaTeX-to-Python** parser.

We needed a parser that could convert LaTeX math expressions into Python-like expressions. However, [SymPy](https://github.com/sympy/sympy) is an extremely large library (`~50 MB`) and leads to bundle size issues when deploying code as an AWS lambda function (max. size `250MB`). This codebase strips out the minimal code that we need, and is around `~200kb` in size.

The parser is inspired by the `sympy` LaTeX parser, but instead of returning symbolic SymPy expressions, we return lines of Python-like code which could can then be evaluated in the interpreter.

## Setup

Run `poetry install` to create a virtual environment and install dependencies.

You can also run `poetry shell` to activate the virtual environment.

## Usage

```python
from latex2py.parser import parse_latex

latex = r'\frac{1}{2} + \frac{3}{4}'
python = parse_latex(latex)
print(python) # "(1 / 2) + (3 / 4)"

# You can also evaluate the expression
result = eval(python)
print(result) # 1.25
```

## Important Notes
- Integrals and derivatives are not supported yet.
- The `\\sum` and `\\prod` commands are mapped to special `Sum()` and `Product()` functions that the calling code will have to implement. See the tests for examples.
- Variables like `HelloWorld`, `Hello_World`, or even `Hello.world` are interpreted as Python-like variables and object properties. Usually, LaTeX would treat these as implicit multiplication. Multiplication must be made explicit using `\\cdot` or `*`.

You can also adjust the parsing behavior using the `Config` object - see `latex2py/config.py` for more details.

## Tests

Run `pytest tests` to run the test suite. You can find examples of parseable LaTeX syntex there too.

## Re-Generating the Grammar (Advanced)

If you make changes to `LaTeX.g4`, you will need to regenerate the parser using the following commands:

```
pip install antlr4-tools
# This will download the antlr4 jar file if you don't have it already.

cd src/latex2py/parser
antlr4 LaTeX.g4 -o gen
```

The generated files will be in the `gen` directory.

## Publishing to PyPI (Maintainers)

1. Update the version number in `pyproject.toml`.
2. Run `poetry build` to build the package.
3. Run `poetry publish` to publish the package to PyPI.