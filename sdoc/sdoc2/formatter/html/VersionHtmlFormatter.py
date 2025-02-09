from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.VersionNode import VersionNode
from sdoc.sdoc2.NodeStore import NodeStore


class VersionHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for version of SDoc document.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: VersionNode) -> Html:
        """
        Generates HTML code for a version node.

        :param node: The version node.
        """
        return Html(tag='span', text=node.argument)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('version', 'html', VersionHtmlFormatter)
