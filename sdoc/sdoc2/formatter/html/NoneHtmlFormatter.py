from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.NodeStore import NodeStore


class NoneHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for an unsupported SDoc2 command.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: Node) -> Html:
        """
        Generates HTML code for a node.

        :param node: The SDoc2 node.
        """
        if node.is_phrasing():
            tag = 'span'
        else:
            tag = 'div'

        return Html(tag=tag,
                    attr={'class': 'error'},
                    text=f"No formatter available for SDoc2 command '\\{node.name} at {node.position}.")


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('none', 'html', NoneHtmlFormatter)
