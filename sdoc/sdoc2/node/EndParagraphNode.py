from typing import Dict

from cleo.io.io import IO

from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.NodeStore import NodeStore


class EndParagraphNode(Node):
    """
    SDoc2 node for the end of paragraphs.

    Note: End of paragraphs are temporary and only used during the content tree preparation. Before and after the
          content preparation end of paragraph nodes do not exist.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: IO, options: Dict[str, str], argument: str):
        """
        Object constructor.

        :param io: The IO object.
        :param options: Not used.
        :param argument: Not used.
        """
        Node.__init__(self, io, 'end_paragraph', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def is_block_command(self) -> bool:
        """
        Returns False.
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_inline_command(self) -> bool:
        """
        Returns False.
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def prepare_content_tree(self) -> None:
        """
        Not implemented for end paragraph nodes.
        """
        raise RuntimeError()


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('end_paragraph', EndParagraphNode)
