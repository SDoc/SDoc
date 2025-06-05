import os
import unittest
from pathlib import Path

from cleo.application import Application
from cleo.testers.command_tester import CommandTester

from sdoc.command.SDocCommand import SDocCommand


class TableHtmlFormatterTest(unittest.TestCase):
    """
    Test cases for formatting table in HTML.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_table(self):
        """
        Tets with a plain table.
        """
        folder = os.path.dirname(os.path.abspath(__file__))

        application = Application()
        application.add(SDocCommand())
        command = application.find('sdoc')
        command_tester = CommandTester(command)
        command_tester.execute(f'{folder + '/test_plain_table/sdoc.cfg'} {folder + '/test_plain_table/test.sdoc'}')

        actual = Path(folder + '/test_plain_table/output.html').read_text()
        expected = Path(folder + '/test_plain_table/expected.html').read_text()
        self.assertEqual(actual, expected)

# ----------------------------------------------------------------------------------------------------------------------
