"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.node.HeadingNode import HeadingNode
from sdoc.sdoc2.node.Sub1SectionNode import Sub1SectionNode


class SectionNode(HeadingNode):
    """
    SDoc2 node for sections.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, options, argument):
        """
        Object constructor.

        :param dict[str,str] options: The options of this section.
        :param str argument: The title of this section.
        """
        super().__init__('section', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self):
        """
        Returns the command of this node, i.e. section.

        :rtype: str
        """
        return 'section'

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self):
        """
        Returns 2.

        :rtype: int
        """
        return 2

    # ------------------------------------------------------------------------------------------------------------------
    def set_numbers(self, level):
        """
        Sets numbers to subsection nodes.

        :param str level: The level of hierarchy.
        """
        self._options['number'] = level

        number = 1
        for node_id in self._child_nodes:
            node = node_store.in_scope(node_id)

            if isinstance(node, Sub1SectionNode):
                node.set_numbers(self._options['number'] + '.' + str(number))
                number += 1

            node_store.out_scope(node)

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_inline_command('section', SectionNode)
