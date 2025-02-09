from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.SmileNode import SmileNode
from sdoc.sdoc2.NodeStore import NodeStore


class SmileHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for smile.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: SmileNode) -> Html:
        """
        Generates the HTML code for a smile node.

        :param node: The smile node.
        """
        return Html(tag='b', text='SMILE')


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('smile', 'html', SmileHtmlFormatter)
