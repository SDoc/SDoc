from typing import Dict

from sdoc import sdoc2
from sdoc.io.SDocIO import SDocIO
from sdoc.sdoc2.node.HeadingNode import HeadingNode
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.node.TextNode import TextNode
from sdoc.sdoc2.NodeStore import NodeStore


class ParagraphNode(HeadingNode):
    """
    SDoc2 node for paragraphs.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, io: SDocIO, options: Dict[str, str], argument: str):
        """
        Object constructor.

        :param io: The IO object.
        :param options: Not used.
        :param argument: The text of this paragraph.
        """
        HeadingNode.__init__(self, io=io, name='paragraph', options=options, argument=argument)

    # ------------------------------------------------------------------------------------------------------------------
    def is_block_command(self) -> bool:
        """
        Returns False.
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def number(self, numbers: Dict[str, str]) -> None:
        """
        Overrides the HeadingNode implementation with the (original) Node implementation.

        :param numbers: The number of the last node.
        """
        Node.number(self, numbers)

    # ------------------------------------------------------------------------------------------------------------------
    def is_inline_command(self) -> bool:
        """
        Returns False.
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def set_toc_id(self) -> None:
        """
        Don't do anything. Because we needn't this behavior here.
        """
        pass

    # ------------------------------------------------------------------------------------------------------------------
    def prune_whitespace(self) -> None:
        """
        Removes spaces from the end of a paragraph.
        """
        first = self.child_nodes[0]
        last = self.child_nodes[-1]

        for node_id in self.child_nodes:
            node = sdoc2.in_scope(node_id)

            if isinstance(node, TextNode):
                if node.id == first:
                    node.prune_whitespace(leading=True)
                if node.id == last:
                    node.prune_whitespace(trailing=True)
                if node.id != last and node.id != first:
                    node.prune_whitespace()

            sdoc2.out_scope(node)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('paragraph', ParagraphNode)
