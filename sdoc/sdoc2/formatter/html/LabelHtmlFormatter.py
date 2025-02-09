from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.LabelNode import LabelNode
from sdoc.sdoc2.NodeStore import NodeStore


class LabelHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for labels.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: LabelNode) -> Html:
        """
        Generates the HTML code for a label node.

        :param node: The label node.
        """
        return Html(inner=self._struct_inner(node))


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('label', 'html', LabelHtmlFormatter)
