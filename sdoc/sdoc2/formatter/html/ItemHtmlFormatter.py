from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.ItemNode import ItemNode
from sdoc.sdoc2.NodeStore import NodeStore


class ItemHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for items.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: ItemNode) -> Html:
        """
        Generates the HTML code for an item node.

        :param node: The item node.
        """
        return Html(tag='li',
                    attr={'id': node.get_option_value('id')},
                    inner=self._struct_inner(node))


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('item', 'html', ItemHtmlFormatter)
