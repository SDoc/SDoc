from typing import Dict

from sdoc.io.SDocIO import SDocIO
from sdoc.sdoc2 import in_scope, out_scope
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.node.TextNode import TextNode
from sdoc.sdoc2.NodeStore import NodeStore


class ItemNode(Node):
    """
    SDoc2 node for items.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, io: SDocIO, options: Dict[str, str], argument: str):
        """
        Object constructor.

        :param io: The IO object.
        :param options: The options of this item.
        :param argument: Not used.
        """
        Node.__init__(self, io=io, name='item', options=options, argument=argument)

        self._hierarchy_level: int = 0
        """
        The hierarchy level of the itemize.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self, parent_hierarchy_level: int = -1) -> int:
        """
        Returns parent_hierarchy_level.

        :param parent_hierarchy_level: The level of the parent in the hierarchy.
        """
        self._hierarchy_level = parent_hierarchy_level + 1

        return self._hierarchy_level

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_name(self) -> str:
        """
        Returns 'item'
        """
        return 'item'

    # ------------------------------------------------------------------------------------------------------------------
    def is_block_command(self) -> bool:
        """
        Returns False.
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_inline_command(self) -> bool:
        """
        Returns True.
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    def is_list_element(self) -> bool:
        """
        Returns True.
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    def prepare_content_tree(self) -> None:
        """
        Method which checks if all child nodes are phrasing.
        """
        first = self.child_nodes[0]
        last = self.child_nodes[-1]

        for node_id in self.child_nodes:
            node = in_scope(node_id)

            if isinstance(node, TextNode):
                if node_id == first:
                    node.prune_whitespace(leading=True)

                elif node_id == last:
                    node.prune_whitespace(trailing=True)

                elif node_id == first and node_id == last:
                    node.prune_whitespace(leading=True, trailing=True)

            # if not node.is_phrasing():
            #    raise RuntimeError("Node: id:%s, %s is not phrasing" % (str(node.id), node.name))

            out_scope(node)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _increment_last_level(number: str) -> str:
        """
        Increments the last level in number of the item node.

        :param number: The number of the last node.
        """
        heading_numbers = number.split('.')
        heading_numbers[-1] = str(int(heading_numbers[-1]) + 1)

        return '.'.join(heading_numbers)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def strip_start_point(number: str) -> str:
        """
        Removes start point if it in the number.

        :param number: The number of the last node.
        """
        return number.lstrip('.')

    # ------------------------------------------------------------------------------------------------------------------
    def number(self, numbers: Dict[str, str]) -> None:
        """
        Sets number for item nodes.

        :param numbers: The number of the last node.
        """
        numbers['item'] = self.strip_start_point(numbers['item'])
        numbers['item'] = self._increment_last_level(numbers['item'])

        self._options['number'] = numbers['item']

        Node.number(self, numbers)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('item', ItemNode)
