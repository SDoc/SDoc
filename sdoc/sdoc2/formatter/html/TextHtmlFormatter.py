from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.TextNode import TextNode
from sdoc.sdoc2.NodeStore import NodeStore


class TextHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for text.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: TextNode) -> Html:
        """
        Generates the HTML code for a text node.

        :param node: The text node.
        """
        return Html(text=node.argument)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('TEXT', 'html', TextHtmlFormatter)
