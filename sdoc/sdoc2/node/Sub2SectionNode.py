from typing import Dict

from cleo.io.io import IO

from sdoc.sdoc2.node.HeadingNode import HeadingNode
from sdoc.sdoc2.NodeStore import NodeStore


class Sub2SectionNode(HeadingNode):
    """
    SDoc2 node for sub-subsections.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: IO, options: Dict[str, str], argument: str):
        """
        Object constructor.

        :param io: The IO object.
        :param options: The options of this section.
        :param argument: The title of this section.
        """
        HeadingNode.__init__(self, io, 'sub2section', options, argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self, parent_hierarchy_level: int = -1) -> int:
        """
        Returns 4.
        """
        return 4


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('sub2section', Sub2SectionNode)
NodeStore.register_inline_command('subsubsection', Sub2SectionNode)
