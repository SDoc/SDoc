import glob
import os
import re
import unittest
from pathlib import Path

from cleo.application import Application
from cleo.testers.command_tester import CommandTester

from sdoc.command.SDoc1Command import SDoc1Command


class SubstitutionTest(unittest.TestCase):
    """
    Test cases for SDoc1 expressions.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_substitute(self):
        """
        Runs all test cases in the test/debug directory.
        """
        test_file_names = glob.glob(os.path.dirname(os.path.abspath(__file__)) + "/*.sdoc1")

        for test_file_name in sorted(test_file_names):
            with self.subTest(test_file_name=test_file_name):
                application = Application()
                application.add(SDoc1Command())
                command = application.find('sdoc1')
                command_tester = CommandTester(command)
                command_tester.execute(f'{test_file_name} t.sdoc2')

                actual = Path('t.sdoc2').read_text()
                actual = re.sub(r'\\position\{[^}]*}', '', actual)
                expected = Path(test_file_name).with_suffix('.sdoc2').read_text()

                self.assertEqual(expected.strip(), actual.strip())

# ----------------------------------------------------------------------------------------------------------------------
