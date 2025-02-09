from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.LineBreakNode import LineBreakNode
from sdoc.sdoc2.NodeStore import NodeStore


class LineBreakHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for a linebreak.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: LineBreakNode) -> Html:
        """
        Generates the HTML code for a smile node.

        :param node: The linebreak node.
        """
        return Html(tag='br')


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('br', 'html', LineBreakHtmlFormatter)
