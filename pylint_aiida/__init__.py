from .raw import MyRawChecker
from .imports import WorkFunctionChecker

def register(linter):
    """This required method auto registers the checker.
    :param linter: The linter to register the checker to.
    :type linter: pylint.lint.PyLinter
    """
    linter.register_checker(MyRawChecker(linter))
    linter.register_checker(WorkFunctionChecker(linter))

