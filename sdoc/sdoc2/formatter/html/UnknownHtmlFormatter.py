from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.NodeStore import NodeStore


class UnknownHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for unknown SDoc2 node types.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: Node) -> Html:
        """
        Generates the HTML code for an unknown node.

        :param node: The unknown node.
        """
        self.error(f"Unknown SDoc2 command '\\{node.argument}'", node)

        return Html()


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('unknown', 'html', UnknownHtmlFormatter)
