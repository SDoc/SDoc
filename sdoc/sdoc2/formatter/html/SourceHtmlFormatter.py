import re
from pathlib import Path

from pygments import highlight
from pygments.formatters import HtmlFormatter as PyHtmlFormatter
from pygments.lexers import get_lexer_for_filename

from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.SourceNode import SourceNode
from sdoc.sdoc2.NodeStore import NodeStore


class SourceHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for a source code block in HTML representation.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: SourceNode) -> Html:
        """
        Generates the HTML code for an icon node.

        :param node: The source node.
        """
        path = node.get_relative_path()
        code = Path(path).read_text()
        style = node.get_option_value('style', 'source')
        hl_lines = node.get_option_value('highlight', [])
        if isinstance(hl_lines, str):
            hl_lines = re.split(r'[, ]+', hl_lines)

        lexer = get_lexer_for_filename(path, stripall=True)
        formatter = PyHtmlFormatter(linenos=True, cssclass=style, hl_lines=hl_lines)

        highlight_code = highlight(code, lexer, formatter)

        return Html(inner=[Html(html=highlight_code),
                           Html(tag='style',
                                html=formatter.get_style_defs())])  # XXX Infra structure for assets.

        # XXX wrapper with copy and download button.


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('source', 'html', SourceHtmlFormatter)
