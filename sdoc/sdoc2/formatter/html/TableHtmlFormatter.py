from typing import Any, List

from sdoc.helper.Html import Html
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.TableNode import TableNode
from sdoc.sdoc2.NodeStore import NodeStore


class TableHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for table.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: TableNode) -> Html:
        """
        Generates the HTML code for a table node.

        :param TableNode node: The table node.
        """
        return Html(tag='table',
                    attr={'class': node.get_option_value('class'),
                          'id':    node.get_option_value('id')},
                    inner=[self.__struct_caption(node),
                           self.__struct_table_body(node)])

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __struct_caption(node: TableNode) -> Html | None:
        """
        Generates the caption for the table in HTML representation.

        :param node: The table node.
        """
        if not node.caption:
            return None

        table_number = node.get_option_value('number')
        if table_number:
            text = f'Tabel {table_number}: {node.caption}'  # TODO Internationalization
        else:
            text = node.caption

        return Html(tag='caption', text=text)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __struct_table_body(node: TableNode) -> Html:
        """
        Generates table with header.

        :param node: The table node.
        """
        rows = []

        if node.column_headers:
            cells = []
            for column in node.column_headers:
                cells.append(Html(tag='th', inner=column))
            rows.append(Html(tag='tr', inner=cells))

        for row in node.rows:
            header_column_counter = 0
            for col in row:
                cells = []
                align = TableHtmlFormatter._get_align(node.alignments, header_column_counter)
                cells.append(TableHtmlFormatter.__struct_table_cell(align, col))
                header_column_counter += 1
                rows.append(Html(tag='tr', inner=cells))

        return Html(tag='body', inner=rows)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __struct_table_cell(align: str | None, cell: Any) -> Html:
        """
        Returns the 'column' with HTML data.

        :param align:
        :param cell: The column in a table.
        """
        attributes = {}

        if align:
            attributes['style'] = f'text-align: {align}'

        if isinstance(cell, str):
            html = Html.txt2html(cell)
        else:
            formatter = NodeStore.get_formatter('html', cell.name)
            html = formatter.get_html(cell)

        return Html(tag='td',
                    attr=attributes,
                    html=html)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def _get_align(align_list: List[str | None], column: int) -> List[str | None] | None:
        """
        Returns the alignment or None.

        :param align_list: The list with alignments.
        :param column: The column number.
        """
        if column in range(len(align_list)):
            return align_list[column]

        return None


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('table', 'html', TableHtmlFormatter)
