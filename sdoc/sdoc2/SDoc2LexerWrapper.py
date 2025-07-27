import re
import sys
from typing import TextIO

from antlr4.RuleContext import RuleContext

from sdoc.antlr.sdoc2Lexer import sdoc2Lexer
from sdoc.sdoc2.Position import Position


class SDoc2LexerWrapper(sdoc2Lexer):
    """

    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, input=None, output: TextIO = sys.stdout):
        """
        Object constructor.
        """
        sdoc2Lexer.__init__(self, input, output)

        self._sdoc1_file_name: str = ''
        """
        The original file name at SDoc1 level.
        """

        self._sdoc1_line: int = 0
        """
        The offset for computing the current line at SDoc1 level.
        """

        self._sdoc1_column: int = 0
        """
        The offset for computing the current column at SDoc1 level.
        """

        self._sdoc2_line: int = 0
        """
        The line position of the last position command.
        """

        self._sdoc2_column: int = 0
        """
        The last column position of the last position command.
        """

    # ------------------------------------------------------------------------------------------------------------------
    def POSITION_action(self, localctx: RuleContext, actionIndex: int) -> None:
        """
        Sets the position of the current line at SDoc1 level.

        :param localctx: Unknown.
        :param actionIndex: Unknown.
        """
        if actionIndex == 0:
            prev_length = 0
            length = 100
            while True:
                text = self._input.getText(self._input.index, self._input.index + length)
                pos = text.find('}')
                if pos != -1 or len(text) == prev_length:
                    break
                length += 100
                prev_length = len(text)

            if pos != -1:
                text = text[1:pos]
                parts = re.match(r'(.+):([0-9]+)\.([0-9]+)', text)
                if not parts:
                    return

                self._sdoc1_file_name = parts.group(1)
                self._sdoc1_line = int(parts.group(2))
                self._sdoc1_column = int(parts.group(3))
                self._sdoc2_line = self.line
                self._sdoc2_column = self.column + len(text) + 1

    # ------------------------------------------------------------------------------------------------------------------
    def get_position(self, line_number: int, column: int) -> Position:
        """
        Returns the position of the token in the original SDoc1 source file.

        """
        if self._sdoc2_line == line_number:
            column = self._sdoc1_column + (column - self._sdoc2_column)

        line_number = self._sdoc1_line + (line_number - self._sdoc2_line)

        return Position(self._sdoc1_file_name, line_number, column, -1, -1)

# ----------------------------------------------------------------------------------------------------------------------
