from antlr4.error.ErrorListener import ConsoleErrorListener

from sdoc.io.SDocIO import SDocIO
from sdoc.sdoc2.SDoc2LexerWrapper import SDoc2LexerWrapper


class SDoc2ErrorListener(ConsoleErrorListener):
    """
    An error listener for SDoc2.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, io: SDocIO) -> None:
        """
        Object constructor.

        :param io: The IO object.
        :param visitor: The visitor for SDoc level 2.
        """
        self._io: SDocIO = io
        """
        The IO object.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def syntaxError(self,
                    recognizer: SDoc2LexerWrapper,
                    offending_symbol: str,
                    line: int,
                    column: int,
                    message: str,
                    exception: Exception) -> None:
        """
        Logs a syntax error.

        :param recognizer: The SDoc2 lexer.
        :param offending_symbol: The offending symbol.
        :param line: The line number.
        :param column: The column number.
        :param message: The error message.
        :param exception: The exception.
        """
        position = recognizer.get_position(line, column)
        self._io.write_error_line(f'<error>At {position}: {message}.<error>')
        if self._io.is_very_verbose():
            stream = recognizer.inputStream
            if hasattr(stream, 'fileName'):
                filename = stream.fileName
            else:
                filename = stream.name
            self._io.write_error_line(f'  <error>At {filename}:{line}.{column + 1}.<error>')

# ----------------------------------------------------------------------------------------------------------------------
