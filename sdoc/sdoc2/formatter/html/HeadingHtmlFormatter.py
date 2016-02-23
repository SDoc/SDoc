"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


class HeadingHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for headings.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for a heading node.

        :param sdoc.sdoc2.node.HeadingNode.HeadingNode node: The heading node.
        :param file file: The output file.
        """
        text_in_tag = '%s %s' % (node._options['number'], node.argument)
        file.write(Html.generate_element('h%d' % node.get_hierarchy_level(), {}, text_in_tag))

        super().generate(node, file)


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_format_decorator('chapter', 'html', HeadingHtmlFormatter)
node_store.register_format_decorator('section', 'html', HeadingHtmlFormatter)
node_store.register_format_decorator('subsection', 'html', HeadingHtmlFormatter)
node_store.register_format_decorator('sub2section', 'html', HeadingHtmlFormatter)
node_store.register_format_decorator('sub3section', 'html', HeadingHtmlFormatter)
node_store.register_format_decorator('sub4section', 'html', HeadingHtmlFormatter)
node_store.register_format_decorator('sub5section', 'html', HeadingHtmlFormatter)
