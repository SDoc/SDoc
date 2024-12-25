from typing import Dict

from cleo.io.io import IO

from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.NodeStore import NodeStore


class UnknownNode(Node):
    """
    SDoc2 node for development testing.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, io: IO, command: str):
        """
        Object constructor.

        :param io: The IO object.
        :param command: The unknown command.
        """
        Node.__init__(self, io=io, name='unknown', argument=command)

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
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_phrasing(self) -> bool:
        """
        Returns True.
        """
        return True


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_block_command('unknown', UnknownNode)
NodeStore.register_inline_command('unknown', UnknownNode)
