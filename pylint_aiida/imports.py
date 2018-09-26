import astroid

from pylint.interfaces import IAstroidChecker
from pylint.checkers import BaseChecker

from aiida import load_dbenv
load_dbenv()
from aiida.work.workfunction import workfunction


# This is our checker class.
# Checkers should always inherit from `BaseChecker`.
class WorkFunctionChecker(BaseChecker):
    """Check correct import for work functions."""
    __implements__ = IAstroidChecker

    # The name defines a custom section of the config for this checker.
    name = 'aiida-wf-import'
    # The priority indicates the order that pylint will run the checkers.
    priority = -1
    # This class variable declares the messages (ie the warnings and errors)
    # that the checker can emit.
    msgs = {
        # Each message has a code, a message that the user will see,
        # a unique symbol that identifies the message,
        # and a detailed help message
        # that will be included in the documentation.
        # W0402: uses of a deprecated module %r
        'W2000': ('workfunction has moved to aiida.work.workfunctions',
                  'aiida-wf-import',
                  'Message help'),
        'W2001': ('submit is now JobCalculation.submit',
                  'aiida-wc-submit',
                  'Message help'),
        'W2002': ("functions moved from 'aiida.work.run' to 'aiida.work.launch'",
                  'aiida-wc-run',
                  'Message help'),
    }
    # This class variable declares the options
    # that are configurable by the user.
    options = (
    )

    def visit_importfrom(self, node):
        """Checks that are called when importing from modules.
        See :mod:`astroid` for the description of available nodes.
        :param node: The node to check.
        :type node: astroid.node_classes.Call
        """
        if node.modname == 'aiida.work.workfunction':
            if 'workfunction' in node.names[0]:
                self.add_message('aiida-wf-import', node=node)

        if node.modname == 'aiida.work.run':
            if 'submit' in node.names[0]:
                self.add_message('aiida-wc-submit', node=node)
            else:
                self.add_message('aiida-wc-run', node=node)

    def visit_attribute(self, node):
        """Checks that are called when a :class:`.astroid.node_classes.Attribute` node is visited.
        See :mod:`astroid` for the description of available nodes.
        :param node: The node to check.
        :type node: astroid.node_classes.Attribute
        """

        # illustrating how to check whether submit method of a 
        # given class is called
        if node.attrname == 'submit':
            instance_name = node.last_child()

            # trying to infer class of instance
            for itype in instance_name.infer():
                #import pdb; pdb.set_trace()
                if itype.name == 'WorkChain' and itype.parent.name == 'aiida.work':
                    pass



#    def visit_import(self, node):
#        """Checks that Called when a :class:`.astroid.node_classes.Call` node is visited.
#        See :mod:`astroid` for the description of available nodes.
#        :param node: The node to check.
#        :type node: astroid.node_classes.Call
#        """
#        import pdb; pdb.set_trace()
#        if 'abc' in node.names[0]:

        #if not (isinstance(node.func, astroid.Attribute)
        #        and isinstance(node.func.expr, astroid.Name)
        #        and node.func.expr.name == self.config.store_locals_indicator
        #        and node.func.attrname == 'create'):
        #    return
        #in_class = node.frame()
        #for param in node.args:
        #    in_class.locals[param.name] = node

#    def visit_call(self, node):
#        """Called when a :class:`.astroid.node_classes.Call` node is visited.
#        See :mod:`astroid` for the description of available nodes.
#        :param node: The node to check.
#        :type node: astroid.node_classes.Call
#        """
#        if not (isinstance(node.func, astroid.Attribute)
#                and isinstance(node.func.expr, astroid.Name)
#                and node.func.expr.name == self.config.store_locals_indicator
#                and node.func.attrname == 'create'):
#            return
#        in_class = node.frame()
#        for param in node.args:
#            in_class.locals[param.name] = node
