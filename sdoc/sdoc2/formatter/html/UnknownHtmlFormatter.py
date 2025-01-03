from typing import Any

from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.NodeStore import NodeStore


class UnknownHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for unknown SDoc2 node types.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node: Node, file: Any) -> None:
        """
        Generates the HTML code for an unknown node.

        :param node: The unknown node.
        :param file: The output file.
        """
        self.write_into_file(node)

    # ------------------------------------------------------------------------------------------------------------------
    def generate_chapter(self, node: Node, file: Any) -> None:
        """
        Generates the HTML code for an unknown node.

        :param node: The unknown node.
        :param file: The output file.
        """
        if file:
            self.write_into_file(node)

    # ------------------------------------------------------------------------------------------------------------------
    def write_into_file(self, node: Node):
        """
        Writes into the opened file.

        :param node: The unknown node.
        """
        self.error(f"Unknown SDoc2 command '{node.name}'", node)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('unknown', 'html', UnknownHtmlFormatter)
