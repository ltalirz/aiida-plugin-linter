from pylint.interfaces import IRawChecker
from pylint.checkers import BaseChecker

class MyRawChecker(BaseChecker):
    """check for line continuations with '\' instead of using triple
    quoted string or parenthesis
    """

    __implements__ = IRawChecker

    name = 'custom_raw'
    msgs = {'W9901': ('use \\ for line continuation',
                      'backslash-line-continuation',
                      ('Used when a \\ is used for a line continuation instead'
                       ' of using triple quoted string or parenthesis.')),
            }
    options = ()

    def process_module(self, node):
        """process a module
        the module's content is accessible via node.stream() function
        """
        with node.stream() as stream:
            for (lineno, line) in enumerate(stream):
                if line.rstrip().endswith(b'\\'):
                    self.add_message('backslash-line-continuation',
                                     line=lineno)

