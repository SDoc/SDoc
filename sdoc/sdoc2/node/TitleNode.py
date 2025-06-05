from typing import Dict

from sdoc.io.SDocIO import SDocIO
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.NodeStore import NodeStore


class TitleNode(Node):
    """
    Node for title in sdoc document.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, io: SDocIO, options: Dict[str, str], argument: str):
        """
        Object constructor.

        :param io: The IO object.
        :param options: The options of the title.
        :param argument:
        """
        Node.__init__(self, io=io, name='title', options=options, argument=argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self, parent_hierarchy_level: int = -1) -> int:
        """
        Returns 0.
        """
        return 0

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
NodeStore.register_inline_command('title', TitleNode)
