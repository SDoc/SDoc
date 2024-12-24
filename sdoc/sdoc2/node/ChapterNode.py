from typing import Dict

from cleo.io.io import IO

from sdoc.sdoc2.node.HeadingNode import HeadingNode
from sdoc.sdoc2.NodeStore import NodeStore


class ChapterNode(HeadingNode):
    """
    SDoc2 node for chapters.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: IO, options: Dict[str, str], argument: str):
        """
        Object constructor.

        :param io: The IO object.
        :param options: The options of this chapter.
        :param argument: The title of this chapter.
        """
        HeadingNode.__init__(self, io, 'chapter', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self, parent_hierarchy_level: int = -1) -> int:
        """
        Returns 1.
        """
        return 1


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('chapter', ChapterNode)
