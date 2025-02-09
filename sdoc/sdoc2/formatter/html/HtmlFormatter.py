import abc
from typing import Any, List

from cleo.io.io import IO

from sdoc.helper.Html import Html
from sdoc.sdoc2 import in_scope, node_store, out_scope
from sdoc.sdoc2.formatter.Formatter import Formatter


class HtmlFormatter(Formatter):
    """
    Abstract parent class for all formatters for generating the output of nodes in HTML.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: IO, parent: Formatter):
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
            child_node = in_scope(node_id)

            formatter = node_store.create_formatter(self._io, child_node, self)
            inner.append(formatter.struct(child_node))

            out_scope(child_node)

        return inner

# ----------------------------------------------------------------------------------------------------------------------
