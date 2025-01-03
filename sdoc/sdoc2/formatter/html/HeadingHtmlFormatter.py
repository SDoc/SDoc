from typing import Any

from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.HeadingNode import HeadingNode
from sdoc.sdoc2.NodeStore import NodeStore


class HeadingHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for headings.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node: HeadingNode, file: Any) -> None:
        """
        Generates the HTML code for a heading node.

        :param node: The heading node.
        :param file: The output file.
        """
        self.generate_heading_node(node, file)
        HtmlFormatter.generate(self, node, file)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def generate_heading_node(node: HeadingNode, file: Any) -> None:
        """
        Generates the HTML code for heading node.

        :param node: The heading node.
        :param file: The output file.
        """
        # Set id attribute to heading node.
        attributes = {'id': node.get_option_value('id')}

        if node.numbering:
            number = node.get_option_value('number')
            text_in_tag = '{0} {1}'.format('' if not number else number, node.argument)
        else:
            text_in_tag = '{0}'.format(node.argument)

        file.write(Html.generate_element('h{0:d}'.format(node.get_hierarchy_level() + 2), attributes, text_in_tag))


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('part', 'html', HeadingHtmlFormatter)
NodeStore.register_formatter('chapter', 'html', HeadingHtmlFormatter)
NodeStore.register_formatter('section', 'html', HeadingHtmlFormatter)
NodeStore.register_formatter('subsection', 'html', HeadingHtmlFormatter)
NodeStore.register_formatter('sub2section', 'html', HeadingHtmlFormatter)
NodeStore.register_formatter('sub3section', 'html', HeadingHtmlFormatter)
