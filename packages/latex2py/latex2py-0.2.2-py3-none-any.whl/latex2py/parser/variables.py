import re
from .config import Config
from .parse import parse_latex_with_config as sympy_parse_latex


def number_to_base(n: int, b: int) -> list[int]:
  """Convert a number to a given base.
  
  See: https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-to-a-string-in-any-base
  """
  if n < 0:
    raise ValueError("Number must be positive.")
  if n == 0:
    return [0]
  digits = []
  while n:
    digits.append(int(n % b))
    n //= b
  return digits[::-1]


def number_to_base_string(n: int, L: int = 3) -> str:
  """Convert a number to a unique string.
  
  To do this, we convert the number to base 26 and then map the digits to the
  letters of the alphabet. The resulting string will be unique for every number
  up to 26^L, where L is the number of digits.

  The "Zx" prefix is added since it is unlikely it will conflict with another
  identifier, and is similar to the `0x` prefix for hexadecimal numbers.
  """
  if n < 0:
    raise ValueError("Number must be positive.")
  if n >= 26 ** L:
    raise ValueError(f"Number must be less than {26 ** L}.")
  digits = number_to_base(n, 26)
  padded = [0] * max(0, (L - len(digits))) + digits
  return "Zx" + "".join([chr(ord("A") + d) for d in padded])


def parse_latex(expr: str, strict: bool = False, config: Config = Config()) -> str:
  """Parse a LaTeX expression while respecting identifiers.
  
  Due to the limitations of SymPy, we need to temporarily remove identifiers,
  parse, and then substitute them back in.

  https://docs.sympy.org/latest/modules/parsing.html#mathrm-latex-parsing-functions-reference
  """
  if expr.strip() == "":
    raise ValueError("This expression is empty!")

  # Find all identifiers in the expression. An identifier is an alphanumeric
  # variable name that must start with a letter or an underscore, or a forward
  # slash in the case of latex commands.
  identifier_pattern = re.compile(r"([\\a-zA-Z_][a-zA-Z0-9\._]*)")
  string_literal_pattern = re.compile(r'(["](?:[^\\"]|\\.)*["])')
  
  # First replace all string literals since these won't parse natively.
  literals = re.findall(string_literal_pattern, expr)
  literals_mapping = {}
  for i, l in enumerate(literals):
    literals_mapping[l] = number_to_base_string(i)
    expr = expr.replace(l, literals_mapping[l])

  # Add a \ before any identifier.
  expr = re.sub(identifier_pattern, r"\\\1", expr)
  matches = re.findall(identifier_pattern, expr)

  identifier_mapping = {}
  for i, m in enumerate(matches):
    # Don't map special LaTeX commands.
    if m.startswith("\\\\"):
      continue

    # Don't map any single slashes detected as identifiers.
    if len(m) == 1:
      continue

    # Map the identifier to a unique string.
    if m not in identifier_mapping:
      # IMPORTANT: We need to add the number of literals to the index here.
      identifier_mapping[m] = number_to_base_string(i + len(literals_mapping))

    # Match the identifier only if it isn't preceded by a backslash (LaTeX command)
    # or followed by a word character (part of a larger identifier).
    pattern_not_part_of_larger = rf"(?<!\\)({re.escape(m)})(?![\w]+)"
    expr = re.sub(pattern_not_part_of_larger, re.escape(f"\\{identifier_mapping[m]}"), expr)

  # The line above will add an extra \ before LaTeX commands, which we need to remove.
  expr = expr.replace("\\\\", "\\")
  expr = sympy_parse_latex(expr, config=config, strict=strict)

  # Unmap the identifiers to add the . back in where they were.
  for k, v in identifier_mapping.items():
    expr = expr.replace(v, k)

  # Un-map all of the string literals.
  for k, v in literals_mapping.items():
    expr = expr.replace(v, k)

  # Remove all the backslashes added to the LaTeX commands.
  expr = expr.replace("\\", "")

  return expr
