from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.ReferenceNode import ReferenceNode
from sdoc.sdoc2.NodeStore import NodeStore


class ReferenceHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for references.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: ReferenceNode) -> Html:
        """
        Generates the HTML code for a reference node.

        :param node: The reference node.
        """
        return Html(tag='a',
                    attr={'class': node.get_option_value('class'),
                          'href':  node.get_option_value('href'),
                          'title': node.get_option_value('title')},
                    text=node.text)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('ref', 'html', ReferenceHtmlFormatter)
