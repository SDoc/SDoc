from typing import Dict

from cleo.io.io import IO

from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.NodeStore import NodeStore


class CodeNode(Node):
    """
    Node for (inline) code.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: IO, options: Dict[str, str], argument: str):
        """
        Object constructor.

        :param io: The IO object.
        :param options: The options of this figure.
        :param argument: Not used.
        """
        super().__init__(io, 'code', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self) -> str:
        """
        Returns the command of this node, i.e., code.
        """
        return 'code'

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
    def is_phrasing(self) -> bool:
        """
        Returns whether this node is a phrasing node, i.e., is a part of a paragraph.
        """
        return True

# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('code', CodeNode)
