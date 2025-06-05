import re
from typing import Dict, List

import sdoc
from sdoc.io.SDocIO import SDocIO
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.NodeStore import NodeStore


class TextNode(Node):
    """
    SDoc2 node for items.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, io: SDocIO, options: Dict[str, str] | None = None, argument: str):
        """
        Object constructor.

        :param io: The IO object.
        :param options: Not used.
        :param argument: The actual text.
        """
        Node.__init__(self, io=io, name='TEXT', options=options, argument=argument)

    # ------------------------------------------------------------------------------------------------------------------
    def print_info(self, level: int) -> None:
        """
        Temp function for development.

        :param level: The level of block commands.
        """
        self._io.write_line(f"{' ' * 4 * level}{self.id} {self.name} {self.argument.replace("\n", '\\n')}")

    # ------------------------------------------------------------------------------------------------------------------
    def is_block_command(self) -> bool:
        """
        Returns False.
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_inline_command(self) -> bool:
        """
        Returns False.
        """
        return False

    # ------------------------------------------------------------------------------------------------------------------
    def is_phrasing(self) -> bool:
        """
        Returns True.
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    def split_by_paragraph(self) -> List[int]:
        """
        Splits this text node into text nodes without a paragraph separator (i.e., a double new line) in to a list of
        text nodes without paragraph separators. Each paragraph separator is replaced with an end paragraph node.

        Returns a list of node IDs.
        """
        text_ids = []
        list_of_texts = re.split("\n\n", self.argument)

        # Cleaning the text parts.
        if "\n" in list_of_texts:
            list_of_texts[list_of_texts.index("\n")] = ' '
        if list_of_texts[0] == '':
            list_of_texts.remove('')

        # Checking the range.
        if list_of_texts:
            if not list_of_texts[-1]:
                to = len(list_of_texts) - 1
            else:
                to = len(list_of_texts)

            # Creating text and paragraph end nodes and put id's in list.
            for text in list_of_texts[:to]:
                text_node = TextNode(io=self._io, argument=text)
                sdoc.sdoc2.node_store.store_node(text_node)
                text_ids.append(text_node.id)

                end_paragraph_node = sdoc.sdoc2.node_store.create_inline_node('end_paragraph')
                text_ids.append(end_paragraph_node.id)

            # Checking where we need to add paragraph.
            if text_ids:
                if list_of_texts[-1]:
                    text_ids.pop()

        return text_ids

    # ------------------------------------------------------------------------------------------------------------------
    def prune_whitespace(self, leading: bool = False, trailing: bool = False):
        """
        Method for removing whitespace in text.

        :param leading: Whether to remove leading whitespaces.
        :param trailing: Whether to remove trailing whitespaces.
        """
        argument = self.argument
        if leading:
            argument = argument.lstrip()
        if trailing:
            argument = argument.rstrip()
        self._set_argument(re.sub(r'\s+', ' ', argument))


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('TEXT', TextNode)
