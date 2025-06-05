from typing import Iterable, Union

from cleo.io.io import IO

from sdoc.io.Terminal import Terminal


class SDocIO(IO):
    """
    IO object with title.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __block(self, block_type: str, messages: Union[str, Iterable[str]]) -> None:
        """
        Writes a block message to the output.

        :param messages: The title of a section.
        """
        terminal_width = Terminal().width

        if not isinstance(messages, list):
            messages = [messages]

        lines = ['<{}></>'.format(block_type)]
        for key, message in enumerate(messages):
            if key == 0:
                text = ' [{}] {}'.format(block_type, self.output.formatter.format(message))
            else:
                text = ' {}'.format(self.output.formatter.format(message))
            line = '<{}>{}{}'.format(block_type, text, ' ' * (terminal_width - len(text)))
            lines.append(line)
        lines.append('<{}></>'.format(block_type))

        self.output.write_line(lines)

    # ------------------------------------------------------------------------------------------------------------------
    def title(self, message: str) -> None:
        """
        Writes a title to the output.

        :param message: The title of a section.
        """
        self.write_line([f'<title>{message}</title>',
                         f'<title>{'=' * len(message)}</>',
                         ''])

    # ------------------------------------------------------------------------------------------------------------------
    def warning(self, messages: Union[str, Iterable[str]]) -> None:
        """
        Writes a warning message to the output.

        :param messages: The title of a section.
        """
        self.__block('WARNING', messages)

# ----------------------------------------------------------------------------------------------------------------------
