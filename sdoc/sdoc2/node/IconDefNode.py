from typing import Dict

from sdoc.io.SDocIO import SDocIO
from sdoc.sdoc2.node.IconNode import IconNode
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.NodeStore import NodeStore


class IconDefNode(Node):
    """
    The class for definition of icons in sdoc2.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, io: SDocIO, options: Dict[str, str], argument: str):
        """
        Object constructor.

        :param io: The IO object.
        :param options: The options of this figure.
        :param argument: Not used.
        """
        Node.__init__(self, io=io, name='icondef', options=options, argument=argument)

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
    def prepare_content_tree(self) -> None:
        """
        Prepares this node for further processing.
        """
        reference_name = self.argument
        attributes = self._options

        IconNode.add_definition(reference_name, attributes)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('icondef', IconDefNode)
