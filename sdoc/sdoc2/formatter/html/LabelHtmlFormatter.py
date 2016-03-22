"""
SDoc

Copyright 2016 Set Based IT Consultancy

Licence MIT
"""
# ----------------------------------------------------------------------------------------------------------------------
from sdoc.helper.Html import Html
from sdoc.sdoc2 import node_store
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter


class LabelHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for labels.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file):
        """
        Generates the HTML code for a label node.

        :param sdoc.sdoc2.node.LabelNode.LabelNode node: The label node.
        :param file file: The output file.
        """
        super().generate(node, file)

# ----------------------------------------------------------------------------------------------------------------------
node_store.register_formatter('label', 'html', LabelHtmlFormatter)