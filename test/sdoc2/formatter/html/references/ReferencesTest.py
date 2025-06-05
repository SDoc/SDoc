import os
import unittest
from pathlib import Path

from cleo.application import Application
from cleo.testers.command_tester import CommandTester

from sdoc.command.SDocCommand import SDocCommand


class ReferencesTest(unittest.TestCase):
    """
    Test cases for SDoc2 references.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_references(self):
        """
        Runs all test cases in test/references directory.
        """
        folder = os.path.dirname(os.path.abspath(__file__))

        application = Application()
        application.add(SDocCommand())
        command = application.find('sdoc')
        command_tester = CommandTester(command)
        command_tester.execute(
                f'{folder + '/test_plain_references/sdoc.cfg'} {folder + '/test_plain_references/test.sdoc'}')

        actual = Path(folder + '/test_plain_references/output.html').read_text()
        expected = Path(folder + '/test_plain_references/expected.html').read_text()
        self.assertEqual(actual, expected)

# ----------------------------------------------------------------------------------------------------------------------
