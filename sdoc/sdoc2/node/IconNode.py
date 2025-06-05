from typing import Dict

from sdoc.io.SDocIO import SDocIO
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.NodeStore import NodeStore


class IconNode(Node):
    """
    Node for icons (i.e. small inline images).
    """

    # ------------------------------------------------------------------------------------------------------------------
    _definitions = {}
    """
    The icon definitions. Map from ion name ot attributes.

    :type: dict[str,dict[str,str]]
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, io: SDocIO, options: Dict[str, str], argument: str):
        """
        Object constructor.

        :param io: The IO object.
        :param options: The options of this figure.
        :param argument: Not used.
        """
        Node.__init__(self, io=io, name='icon', options=options, argument=argument)

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
        Returns True if this node is a phrasing node, i.e. is a part of a paragraph. Otherwise returns False.
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def add_definition(name: str, attributes: Dict[str, str]):
        """
        Adds the definition of an icon to the icon definitions.

        :param name: The name of a reference to icon definition.
        :param attributes: The attributes.
        """
        IconNode._definitions[name] = attributes

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def get_definition(name: str) -> Dict[str, str] | None:
        """
        Returns the attributes of the definition of an icon if the definition exists.

        :param name: The name of the icon definition.
        """
        if name in IconNode._definitions:
            return IconNode._definitions[name]
        else:
            return None


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('icon', IconNode)
