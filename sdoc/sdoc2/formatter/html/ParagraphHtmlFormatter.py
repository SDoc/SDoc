from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.ParagraphNode import ParagraphNode
from sdoc.sdoc2.NodeStore import NodeStore


class ParagraphHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for paragraph.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: ParagraphNode) -> Html:
        """
        Generates the HTML code for a paragraph node.

        :param node: The paragraph node.
        """
        inner = self._struct_inner(node)

        return Html(tag='p' if inner else None, inner=inner)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('paragraph', 'html', ParagraphHtmlFormatter)
