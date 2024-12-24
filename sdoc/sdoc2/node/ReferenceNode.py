from typing import Dict

from cleo.io.io import IO

from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.NodeStore import NodeStore


class ReferenceNode(Node):
    """
    SDoc2 node for references.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: IO, options: Dict[str, str], argument: str):
        """
        Object constructor.

        :param io: The IO object.
        :param options: The options of this reference.
        :param argument: The title of this reference.
        """
        Node.__init__(self, io, 'ref', options, argument)

        self.text = ''
        """
        The text of a reference.

        :type: str
        """

    # ------------------------------------------------------------------------------------------------------------------
    def get_command(self) -> str:
        """
        Returns the command of this node, i.e., reference.
        """
        return 'ref'

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
NodeStore.register_inline_command('ref', ReferenceNode)
