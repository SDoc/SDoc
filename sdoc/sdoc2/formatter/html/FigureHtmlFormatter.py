from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.FigureNode import FigureNode
from sdoc.sdoc2.NodeStore import NodeStore


class FigureHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for figures.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: FigureNode) -> Html:
        """
        Generates the HTML code for a figure node.

        :param node: The figure node.
        """
        return Html(tag='figure',
                    attr={'id': node.get_option_value('id')},
                    inner=[Html(tag='img',
                                attr={'src':    node.get_option_value('src'),
                                      'width':  node.get_option_value('width'),
                                      'height': node.get_option_value('height'),
                                      'alt':    node.caption}),
                           FigureHtmlFormatter.__struct_caption(node)])

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __struct_caption(node: FigureNode) -> Html | None:
        """
        Generates the caption for the table in HTML representation.

        :param node: The figure node.
        """
        if not node.caption:
            return None

        figure_number = node.get_option_value('number')
        if figure_number:
            inner_text = f'Figuur {figure_number}: {node.caption}'  # TODO Internationalization
        else:
            inner_text = node.caption

        return Html(tag='figcaption', text=inner_text)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('figure', 'html', FigureHtmlFormatter)
