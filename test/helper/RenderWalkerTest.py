import unittest

from sdoc.helper.RenderWalker import RenderWalker


class RenderWalkerTest(unittest.TestCase):
    """
    Unit tests for class RenderWalker.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def test_get_classes1(self) -> None:
        """
        Test get_classes without submodule class.
        """
        walker = RenderWalker('foo')

        self.assertEqual([], walker.get_classes())

    # ------------------------------------------------------------------------------------------------------------------
    def test_get_classes3(self) -> None:
        """
        Test get_classes with submodule class and without prevailing module classes.
        """
        walker = RenderWalker('foo', 'bar')

        self.assertEqual(['bar'], walker.get_classes())
        self.assertEqual(['bar', 'foo-eggs'], walker.get_classes('eggs'))
        self.assertEqual(['bar', 'foo-eggs', 'foo-spam'], walker.get_classes(['eggs', 'spam']))
        self.assertEqual(['bar', 'foo-eggs', 'is-test'], walker.get_classes('eggs', 'is-test'))
        self.assertEqual(['bar', 'foo-eggs', 'is-test', 'is-unit'], walker.get_classes('eggs', ['is-test', 'is-unit']))
        self.assertEqual(['bar',
                          'foo-eggs',
                          'foo-spam',
                          'is-test',
                          'is-unit'], walker.get_classes(['eggs', 'spam'], ['is-test', 'is-unit']))


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
