from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.TitleNode import TitleNode
from sdoc.sdoc2.NodeStore import NodeStore


class TitleHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for title of SDoc document.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: TitleNode) -> Html:
        """
        Generates HTML code for a title node.

        :param node: The title node.
        """
        return Html(tag='span', text=node.argument)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('title', 'html', TitleHtmlFormatter)
