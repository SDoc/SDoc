from typing import Any

from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.NodeStore import NodeStore


class NoneHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for an unsupported SDoc2 command.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node: Node, file: Any) -> None:
        """
        Generates HTML code for a date node.

        :param node: The SDoc2 node.
        :param file: The output file.
        """
        if node.is_phrasing():
            tag = 'span'
        else:
            tag = 'div'

        html = Html.generate_element(tag,
                                     {'class': 'error'},
                                     f"No formatter available for SDoc2 command '\\{node.name} at {node.position}.")
        file.write(html)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('none', 'html', NoneHtmlFormatter)
