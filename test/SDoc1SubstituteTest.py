import glob
import os
import re
import unittest

from cleo import Application, CommandTester

from sdoc.command.SDoc1Command import SDoc1Command


class SDoc1SubstitutionTest(unittest.TestCase):
    """
    Test cases for SDoc1 expressions.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_substitute(self):
        """
        Runs all test cases in the test/debug directory.
        """
        test_file_names = glob.glob(os.path.dirname(os.path.abspath(__file__)) + "/substitute/*.sdoc1")

        for test_file_name in sorted(test_file_names):
            with self.subTest(test_file_name=test_file_name):
                pre, ext = os.path.splitext(test_file_name)
                text_file_name = pre + '.sdoc2'
                with open(text_file_name, 'r') as file:
                    expected = file.read()

                application = Application()
                application.add(SDoc1Command())

                command = application.find('sdoc1')
                command_tester = CommandTester(command)
                command_tester.execute([('command', command.get_name()),
                                        ('main.sdoc', test_file_name),
                                        ('output.sdoc2', 't.sdoc2')])

                with open('t.sdoc2', 'r') as file:
                    actual = file.read()
                    actual = re.sub(r'\\position\{[^\}]*\}', '', actual)

                self.assertEqual(expected.strip(), actual.strip())

# ----------------------------------------------------------------------------------------------------------------------
