from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.ItemizeNode import ItemizeNode
from sdoc.sdoc2.NodeStore import NodeStore


class ItemizeHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for itemize.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: ItemizeNode) -> Html:
        """
        Generates the HTML code for an itemize node.

        :param node: The itemize node.
        """
        return Html(tag='ul', inner=self._struct_inner(node))


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('itemize', 'html', ItemizeHtmlFormatter)
