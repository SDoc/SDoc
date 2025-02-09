import unittest

from sdoc.helper.Html import Html


class HtmlTest(unittest.TestCase):
    # ------------------------------------------------------------------------------------------------------------------
    def test_html_nested_void_elements(self):
        html = Html.html_nested(Html(tag='br'))
        self.assertEqual('<br/>', html)

        html = Html.html_nested(Html(tag='img',
                                     attr={'src': '/images/logo.png',
                                           'alt': 'logo'}))
        self.assertEqual('<img src="/images/logo.png" alt="logo"/>', html)

    # ------------------------------------------------------------------------------------------------------------------
    def test_html_nested_element(self):
        html = Html.html_nested(Html(tag='a',
                                     attr={'href': 'https://github.com/PhpPlaisio/helper-html'},
                                     text='helper & html'))
        self.assertEqual('<a href="https://github.com/PhpPlaisio/helper-html">helper &amp; html</a>', html)

    # ------------------------------------------------------------------------------------------------------------------
    def test_html_nested_element_with_int_text(self):
        html = Html.html_nested(Html(tag='a',
                                     attr={'href': 'https://github.com/PhpPlaisio/helper-html'},
                                     text=123))
        self.assertEqual('<a href="https://github.com/PhpPlaisio/helper-html">123</a>', html)

    # ------------------------------------------------------------------------------------------------------------------
    def test_html_nested_element_with_html(self):
        html = Html.html_nested(Html(tag='a',
                                     attr={'href': 'https://github.com/PhpPlaisio/helper-html'},
                                     html='<b>helper-html</b>'))
        self.assertEqual('<a href="https://github.com/PhpPlaisio/helper-html"><b>helper-html</b></a>', html)

    # ------------------------------------------------------------------------------------------------------------------
    def test_html_nested_element_with_nested_elements(self):
        html = Html.html_nested(Html(tag='a',
                                     attr={'href': 'https://github.com/PhpPlaisio/helper-html'},
                                     inner=Html(tag='b',
                                                text='helper-html')))
        self.assertEqual('<a href="https://github.com/PhpPlaisio/helper-html"><b>helper-html</b></a>', html)

    # ------------------------------------------------------------------------------------------------------------------
    def test_html_nested_element_with_list_of_elements(self):
        html = Html.html_nested([Html(tag='a',
                                      attr={'href': 'https://github.com/PhpPlaisio/helper-html'},
                                      inner=Html(tag='b',         text='helper-html')),
                                 Html(tag='br')])
        self.assertEqual('<a href="https://github.com/PhpPlaisio/helper-html"><b>helper-html</b></a><br/>', html)

    # ------------------------------------------------------------------------------------------------------------------
    def test_html_nested_only_text(self):
        html = Html.html_nested(Html(text='My Text!'))
        self.assertEqual('My Text!', html)

    # ------------------------------------------------------------------------------------------------------------------
    def test_html_nested_only_html(self):
        html = Html.html_nested(Html(html='My HTML!'))
        self.assertEqual('My HTML!', html)

    # ------------------------------------------------------------------------------------------------------------------
    def test_html_nested_nothing(self):
        html = Html.html_nested(Html())
        self.assertEqual('', html)

    # ------------------------------------------------------------------------------------------------------------------
    def test_html_nested_none(self):
        html = Html.html_nested(None)
        self.assertEqual('', html)

    # ------------------------------------------------------------------------------------------------------------------
    def test_html_nested_list_none(self):
        html = Html.html_nested([None])
        self.assertEqual('', html)

    # ------------------------------------------------------------------------------------------------------------------
    def test_html_nested_table(self):
        html = Html.html_nested([Html(tag='table',
                                      attr={'class': 'test'},
                                      inner=[Html(tag='tr',
                                                  attr={'id': 'first-row'},
                                                  inner=[Html(tag='td',
                                                              text='hello'),
                                                         Html(tag='td',
                                                              attr={'class': 'bold'},
                                                              html='<b>world</b>')]),
                                             Html(tag='tr',
                                                  inner=[Html(tag='td',
                                                              text='foo'),
                                                         Html(tag='td',
                                                              text='bar')]),
                                             Html(tag='tr',
                                                  attr={'id': 'last-row'},
                                                  inner=[Html(tag='td',
                                                              text='foo'),
                                                         Html(tag='td',
                                                              text='bar')])]),
                                 Html(text='The End'),
                                 Html(html='!')])
        self.assertEqual(
            '<table class="test"><tr id="first-row"><td>hello</td><td class="bold"><b>world</b></td></tr><tr><td>foo</td><td>bar</td></tr><tr id="last-row"><td>foo</td><td>bar</td></tr></table>The End!',
            html)


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    unittest.main()
