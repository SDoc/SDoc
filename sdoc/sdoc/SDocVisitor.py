# ----------------------------------------------------------------------------------------------------------------------

from antlr4.Token import CommonToken
from cleo.io.io import IO


class SDocVisitor:
    """
    Parent visitor for SDoc level 1 & 2.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: IO):
        """
        Object constructor.
        """

        self._io: IO = io
        """
        Styled output formatter.
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
        return self._errors

    # ------------------------------------------------------------------------------------------------------------------
    def _error(self, message: str, token: CommonToken | None = None) -> None:
        """
        Logs an error.

        :param message: The error message.This message will be appended with 'at filename:line.column' ot the token.
        :param token: The token where the error occurred.
        """
        self._errors += 1

        filename = token.getInputStream().fileName  # Replace fileName with get_source_name() when implemented in ANTLR.
        line_number = token.line
        column_number = token.column + 1
        messages = [message]
        if token:
            messages.append('Position: {0!s}:{1:d}.{2:d}'.format(filename, line_number, column_number))
        self._io.write_error(messages)

# ----------------------------------------------------------------------------------------------------------------------
