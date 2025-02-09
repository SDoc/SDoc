from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.HyperlinkNode import HyperlinkNode
from sdoc.sdoc2.NodeStore import NodeStore


class HyperlinkHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for hyperlinks.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: HyperlinkNode) -> Html:
        """
        Generates the HTML code for a hyperlink node.

        :param node: The hyperlink node.
        """
        return Html(tag='a',
                    attr=node.get_html_attributes(),
                    text=node.argument)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('hyperlink', 'html', HyperlinkHtmlFormatter)
