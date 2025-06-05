import abc
from typing import Any, List

from sdoc import sdoc2
from sdoc.helper.Html import Html
from sdoc.io.SDocIO import SDocIO
from sdoc.sdoc2.formatter.Formatter import Formatter


class HtmlFormatter(Formatter):
    """
    Abstract parent class for all formatters for generating the output of nodes in HTML.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: SDocIO, parent: Formatter):
        """
        Object constructor.

        :param io: The IO object.
        :param parent: The formatter for the parent node.
        """
        Formatter.__init__(self, io, parent)

    # ------------------------------------------------------------------------------------------------------------------
    def generate(self, node, file: Any) -> None:
        """
        Generates the representation of a node in the requested output format.

        :param node: The node for which the output must be generated.
        :param file: The output file.
        """
        struct = self.struct(node)
        file.write(Html.html_nested(struct))

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def struct(self, node) -> Html:
        raise NotImplementedError

    # ------------------------------------------------------------------------------------------------------------------
    def _struct_inner(self, node) -> List[Html]:
        """

        :param node:
        """
        inner = []
        for node_id in node.child_nodes:
            child_node = sdoc2.in_scope(node_id)

            formatter = sdoc2.node_store.create_formatter(self._io, child_node, self)
            struct = formatter.struct(child_node)
            if struct.is_not_empty:
                inner.append(struct)

            sdoc2.out_scope(child_node)

        return inner

# ----------------------------------------------------------------------------------------------------------------------
