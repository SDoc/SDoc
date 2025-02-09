from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.CodeNode import CodeNode
from sdoc.sdoc2.NodeStore import NodeStore


class CodeHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for (inline) code in HTML representation.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: CodeNode) -> Html:
        """
        Generates the HTML code for an icon node.

        :param node: The code node.
        """
        return Html(tag='code', text=node.argument)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('code', 'html', CodeHtmlFormatter)
