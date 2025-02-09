from typing import Dict, List

from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.TocNode import TocNode
from sdoc.sdoc2.NodeStore import NodeStore


class TocHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for table of contents.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: TocNode) -> Html:
        """
        Generates the HTML code for a table of contents node.

        :param node: The table of contents node.
        """
        return Html(tag='nav',
                    attr={'role':  'navigation',
                          'class': 'table-of-contents'},
                    inner=[Html(tag='h3', text=node.argument),
                           Html(tag='ul', inner=TocHtmlFormatter.__struct_toc_items(node))])

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __struct_toc_items(node: TocNode) -> List[Html]:
        """
        Writes the contents into file.

        :param TocNode node: The table of contents node.
        """
        toc_items = []

        depth = node.get_option_value('depth')
        for item in node.get_option_value('ids'):
            if not depth or (depth and item['level'] <= int(depth)):
                toc_items.append(TocHtmlFormatter.__struct_toc_item(item))

        return toc_items

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __struct_toc_item(item: Dict[str, str]) -> Html:
        """
        Write the containing elements.

        :param item: The item which we outputs.
        """
        inner = []

        number = item['number'] if item['numbering'] else None
        if number:
            inner.append(Html(tag='span', text=number))
            inner.append(Html(text=' '))
        inner.append(Html(text=item['arg']))

        link = Html(tag='a',
                    attr={'href': f'#{item['id']}'},
                    inner=inner)

        return Html(tag='li',
                    attr={'class': f'level{item['level']}'},
                    inner=link)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('toc', 'html', TocHtmlFormatter)
