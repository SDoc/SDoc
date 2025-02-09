from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.DateNode import DateNode
from sdoc.sdoc2.NodeStore import NodeStore


class DateHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for date of SDoc document.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: DateNode) -> Html:
        """
        Generates HTML code for a date node.

        :param DateNode node: The date node.
        """
        return Html(tag='span', text=node.argument)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('date', 'html', DateHtmlFormatter)
