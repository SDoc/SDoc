from typing import Dict

from cleo.io.io import IO

from sdoc.helper.PathResolver import PathResolver
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.NodeStore import NodeStore


class SourceNode(Node):
    """
    Node for a code block.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, io: IO, options: Dict[str, str], argument: str):
        """
        Object constructor.

        :param io: The IO object.
        :param options: The options of this figure.
        :param argument: Not used.
        """
        Node.__init__(self, io=io, name='source', options=options, argument=argument)

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
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def get_relative_path(self) -> str:
        """
        Returns the relative path of to the source code.
        """
        return PathResolver.resolve_path(self.position.file_name, self.argument)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('source', SourceNode)
