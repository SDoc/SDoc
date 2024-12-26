from pathlib import Path
from typing import Any

from pygments import highlight
from pygments.formatters import HtmlFormatter as PyHtmlFormatter
from pygments.lexers import get_lexer_for_filename

from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.SourceNode import SourceNode
from sdoc.sdoc2.NodeStore import NodeStore


class SourceHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for a source code block in HTML representation.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node: SourceNode, file: Any) -> None:
        """
        Generates the HTML code for an icon node.

        :param node: The source node.
        :param file: The output file.
        """
        path = node.get_relative_path()
        code = Path(path).read_text()
        style = node.get_option_value('style', 'source')

        lexer = get_lexer_for_filename(path, stripall=True)
        formatter = PyHtmlFormatter(linenos=True, cssclass=style)
        result = highlight(code, lexer, formatter)
        file.write(result)

        # XXX Infra structure for assets.
        css = formatter.get_style_defs()

        # XXX wrapper with copy and download button.


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('source', 'html', SourceHtmlFormatter)
