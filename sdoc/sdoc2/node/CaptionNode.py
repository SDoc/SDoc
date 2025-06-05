from typing import Dict

from sdoc.io.SDocIO import SDocIO
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.NodeStore import NodeStore


class CaptionNode(Node):
    """
    SDoc2 node for captions.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, io: SDocIO, options: Dict[str, str], argument: str):
        """
        Object constructor.

        :param io: The IO object.
        :param options: The options of this caption.
        :param argument: The title of this caption.
        """
        Node.__init__(self, io=io, name='caption', options=options, argument=argument)

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


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('caption', CaptionNode)
