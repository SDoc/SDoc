from sdoc import sdoc2
from sdoc.helper.Html import Html
from sdoc.helper.RenderWalker import RenderWalker
from sdoc.sdoc2.formatter.html.HtmlFormatter import HtmlFormatter
from sdoc.sdoc2.node.DocumentNode import DocumentNode
from sdoc.sdoc2.NodeStore import NodeStore


class DocumentHtmlFormatter(HtmlFormatter):
    """
    HtmlFormatter for generating HTML code for document node.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def struct(self, node: DocumentNode) -> Html:
        """
        Generates the HTML code for heading node.

        :param node: The document node.
        """
        walker = RenderWalker('sdoc-document')

        body = []

        inner1 = []
        if node.title_node_id:
            title_node = sdoc2.in_scope(node.title_node_id)
            inner1.append(Html(tag='h1', text=title_node.argument))
            sdoc2.out_scope(title_node)

        inner2 = []
        if node.date_node_id:
            date_node = sdoc2.in_scope(node.date_node_id)
            if date_node.argument:
                inner2.append(Html(tag='span',
                                   attr={'class': walker.get_classes('date')},
                                   text=date_node.argument))
            sdoc2.out_scope(date_node)

        if node.version_node_id:
            version_node = sdoc2.in_scope(node.version_node_id)
            if version_node.argument:
                inner2.append(Html(tag='span',
                                   attr={'class': walker.get_classes('version')},
                                   text=version_node.argument))
            sdoc2.out_scope(version_node)

        if inner2:
            inner1.append(Html(tag='div',
                               attr={'class': walker.get_classes('title-inner')},
                               inner=inner2))

        if inner1:
            body.append(Html(tag='div',
                             attr={'class': walker.get_classes('title-outer')},
                             inner=inner1))

        body += self._struct_inner(node)

        return Html(inner=body)


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_formatter('document', 'html', DocumentHtmlFormatter)
