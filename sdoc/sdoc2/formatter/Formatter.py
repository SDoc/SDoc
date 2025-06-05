import abc
from abc import ABC
from typing import Any

from sdoc.io.SDocIO import SDocIO


class Formatter(ABC):
    """
    Abstract parent class for all formatters for generating the output of nodes in a requested format.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: SDocIO, parent):
        """
        Object constructor.

        :param io: The IO object.
        :param parent: The formatter for the parent node.
        """
        self._io: SDocIO = io
        """
        The IO object.
        """

        self._parent = parent
        """
        The formatter for the parent node.

        :type: sdoc.sdoc2.formatter.Formatter.Formatter
        """

        self._errors: int = 0
        """
        The error count.
        """

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def errors(self) -> int:
        """
        Getter for the error count.
        """
        if self._parent:
            return self._parent.errors

        return self._errors

    # ------------------------------------------------------------------------------------------------------------------
    def error(self, message: str, node=None) -> None:
        """
        Logs an error.

        :param message: The error message. This message will be appended with 'at filename:line.column' ot the token.
        :param node: The node where the error occurred.
        """
        if self._parent:
            self._parent.error(message, node)
        else:
            self._errors += 1

            messages = [message]
            if node:
                filename = node.position.file_name
                line_number = node.position.start_line
                column_number = node.position.start_column + 1
                messages.append(' at {0!s}:{1:d}.{2:d}.'.format(filename, line_number, column_number))
            self._io.write_error(messages)

    # ------------------------------------------------------------------------------------------------------------------
    @abc.abstractmethod
    def generate(self, node, file: Any) -> None:
        """
        Generates the representation of a node in the requested output format.

        :param node: The node for which the output must be generated.
        :param file: The output file.
        """
        raise NotImplementedError()

# ----------------------------------------------------------------------------------------------------------------------
