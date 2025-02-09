from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.IconDefNode import IconDefNode
from sdoc.sdoc2.NodeStore import NodeStore


class IconDefHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter stub for definition of the Icon.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: IconDefNode) -> Html:
        """
        Generates the HTML code for an icon node.

        :param IconDefNode node: The icon definition node.
        """
        return Html()


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('icondef', 'html', IconDefHtmlFormatter)
