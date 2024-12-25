from typing import Dict

from cleo.io.io import IO

from sdoc.sdoc2.node.HeadingNode import HeadingNode
from sdoc.sdoc2.NodeStore import NodeStore


class Sub1SectionNode(HeadingNode):
    """
    SDoc2 node for subsections.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, io: IO, options: Dict[str, str], argument: str):
        """
        Object constructor.

        :param io: The IO object.
        :param options: The options of this section.
        :param argument: The title of this section.
        """
        HeadingNode.__init__(self, io=io, name='subsection', options=options, argument=argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_hierarchy_level(self, parent_hierarchy_level: int = -1) -> int:
        """
        Returns 3.
        """
        return 3


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('sub1section', Sub1SectionNode)
NodeStore.register_inline_command('subsection', Sub1SectionNode)
