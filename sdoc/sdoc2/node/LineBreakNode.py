from typing import Dict

from sdoc.io.SDocIO import SDocIO
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.NodeStore import NodeStore


class LineBreakNode(Node):
    """
    SDoc2 node for line breaks.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, io: SDocIO, options: Dict[str, str], argument: str):
        """
        Object constructor.

        :param io: The IO object.
        :param options: The options of this smile.
        :param argument: Not used.
        """
        Node.__init__(self, io=io, name='br', options=options, argument=argument)

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
        Returns True.
        """
        return True


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('br', LineBreakNode)
