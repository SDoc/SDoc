from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.HeadingNode import HeadingNode
from sdoc.sdoc2.NodeStore import NodeStore


class HeadingHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for headings.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: HeadingNode) -> Html:
        """
        Generates the HTML code for a heading node.

        :param node: The heading node.
        """
        if node.numbering:
            number = node.get_option_value('number')
            text_in_tag = f'{'' if not number else number} {node.argument}'
        else:
            text_in_tag = node.argument

        return Html(inner=[Html(tag=f'h{node.get_hierarchy_level() + 2}',
                                attr={'id': node.get_option_value('id')},
                                text=text_in_tag),
                           self._struct_inner(node)])


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('part', 'html', HeadingHtmlFormatter)
NodeStore.register_formatter('chapter', 'html', HeadingHtmlFormatter)
NodeStore.register_formatter('section', 'html', HeadingHtmlFormatter)
NodeStore.register_formatter('subsection', 'html', HeadingHtmlFormatter)
NodeStore.register_formatter('sub2section', 'html', HeadingHtmlFormatter)
NodeStore.register_formatter('sub3section', 'html', HeadingHtmlFormatter)
