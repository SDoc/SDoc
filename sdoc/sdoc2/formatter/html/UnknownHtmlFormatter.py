"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


class UnknownHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for paragraph.
    """
    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for a paragraph node.

        :param sdoc.sdoc2.node.ParagraphNode.ParagraphNode node: The paragraph node.
        :param file file: The output file.
        """
        file.write('<b>Unknown SDoc2 command</b>')


# ----------------------------------------------------------------------------------------------------------------------
node_store.register_formatter('unknown', 'html', UnknownHtmlFormatter)
