import glob
import os
import unittest
from pathlib import Path

from cleo.application import Application
from cleo.testers.command_tester import CommandTester

from sdoc.command.SDoc1Command import SDoc1Command


class ExpressionTest(unittest.TestCase):
    """
    Test cases for SDoc1 expressions.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_debug(self):
        """
        Runs all test cases in the test/debug directory.
        """
        test_file_names = glob.glob(os.path.dirname(os.path.abspath(__file__)) + "/*.sdoc")

        for test_file_name in sorted(test_file_names):
            with self.subTest(test_file_name=test_file_name):
                text = Path(test_file_name).with_suffix('.txt').read_text()

                application = Application()
                application.add(SDoc1Command())
                command = application.find('sdoc1')
                command_tester = CommandTester(command)
                command_tester.execute(f'{test_file_name} t.sdoc2')

                self.assertTrue(command_tester.io.fetch_output().rstrip().endswith(text.strip()))

# ----------------------------------------------------------------------------------------------------------------------
