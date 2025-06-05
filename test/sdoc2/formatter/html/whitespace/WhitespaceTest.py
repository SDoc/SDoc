import os
import unittest
from pathlib import Path

from cleo.application import Application
from cleo.testers.command_tester import CommandTester

from sdoc.command.SDocCommand import SDocCommand


class WhitespaceTest(unittest.TestCase):
    """
    Test cases for whitespace in SDoc2.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_whitespace_in_sentence(self):
        """
        Test whitespace in a sentence.
        """
        folder = os.path.dirname(os.path.abspath(__file__))

        application = Application()
        application.add(SDocCommand())
        command = application.find('sdoc')
        command_tester = CommandTester(command)
        command_tester.execute(
                f'{folder + '/test_whitespace_in_sentence/sdoc.cfg'} {folder + '/test_whitespace_in_sentence/test.sdoc'}')

        actual = Path(folder + '/test_whitespace_in_sentence/output.html').read_text()
        expected = Path(folder + '/test_whitespace_in_sentence/expected.html').read_text()
        self.assertEqual(actual, expected)

    # ------------------------------------------------------------------------------------------------------------------
    def test_whitespace_in_item(self):
        """
        Test whitespace in an item.
        """
        folder = os.path.dirname(os.path.abspath(__file__))

        application = Application()
        application.add(SDocCommand())
        command = application.find('sdoc')
        command_tester = CommandTester(command)
        command_tester.execute(
                f'{folder + '/test_whitespace_in_item/sdoc.cfg'} {folder + '/test_whitespace_in_item/test.sdoc'}')

        actual = Path(folder + '/test_whitespace_in_item/output.html').read_text()
        expected = Path(folder + '/test_whitespace_in_item/expected.html').read_text()
        self.assertEqual(actual, expected)


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
