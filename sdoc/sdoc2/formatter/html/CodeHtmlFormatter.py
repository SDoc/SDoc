from typing import Any

from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.CodeNode import CodeNode
from sdoc.sdoc2.NodeStore import NodeStore


class CodeHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for (inline) code in HTML representation.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node: CodeNode, file: Any) -> None:
        """
        Generates the HTML code for an icon node.

        :param node: The code node.
        :param any file: The output file.
        """
        html_code = Html.generate_element('code', {}, node.argument)

        file.write(html_code)

# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('code', 'html', CodeHtmlFormatter)
