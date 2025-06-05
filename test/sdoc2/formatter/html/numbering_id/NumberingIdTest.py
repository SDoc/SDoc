import os
import unittest
from pathlib import Path

from cleo.application import Application
from cleo.testers.command_tester import CommandTester

from sdoc.command.SDocCommand import SDocCommand


class NumberingIdTest(unittest.TestCase):
    """
    Test cases for SDoc2 id numbers.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_plain_ids(self):
        """
        Runs all test cases in test/id directory.
        """
        folder = os.path.dirname(os.path.abspath(__file__))

        application = Application()
        application.add(SDocCommand())
        command = application.find('sdoc')
        command_tester = CommandTester(command)
        command_tester.execute(f'{folder + '/test_plain_ids/sdoc.cfg'} {folder + '/test_plain_ids/test.sdoc'}')

        actual = Path(folder + '/test_plain_ids/output.html').read_text()
        expected = Path(folder + '/test_plain_ids/expected.html').read_text()
        self.assertEqual(actual, expected)


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
