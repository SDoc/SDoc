from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.IconNode import IconNode
from sdoc.sdoc2.NodeStore import NodeStore


class IconHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for icons in HTML representation.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: IconNode) -> Html:
        """
        Generates the HTML code for an icon node.

        :param IconNode node: The icon node.
        """
        attributes = IconNode.get_definition(node.argument)
        if attributes:
            return Html(tag='img', attr=attributes)

        NodeStore.error(f"There is no definition for icon with name '{node.argument}'.", node)

        return Html()


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('icon', 'html', IconHtmlFormatter)
