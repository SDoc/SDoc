from dataclasses import dataclass
from io import StringIO
from typing import Any, Dict, List


@dataclass(frozen=True)
class Html:
    """
    Utility class with functions for generating HTML code.
    """
    # ------------------------------------------------------------------------------------------------------------------
    tag: str | None = None
    """
    The tag of the HTML element.
    """

    attr: Dict[str, str | List[str]] | None = None
    """
    The attributes of the HTML element.
    """

    inner: Any = None
    """
    The inner elements of the HTML element. A list of HTML objects.
    """

    html: str | None = None
    """
    The inner HTML code of the HTML element. It is upto the caller to make sure the HTML code is correct.
    """

    text: Any = None
    """
    The inner text of the HTML element. Special characters will be converted to HTML entities.
    """

    # ------------------------------------------------------------------------------------------------------------------
    @property
    def is_not_empty(self) -> bool:
        """
        Returns whether this HTML element is not empty.
        """
        return self.tag or self.attr or self.inner or self.html or self.text

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def txt2html(value: Any) -> str:
        """
        Returns a string with special characters converted to HTML entities.

        :param value: The string with optionally special characters.
        """
        if type(value) is str:
            return Html.__escape(value)

        if type(value) is int or type(value) is float:
            return str(value)

        if value is None:
            return ''

        if value == True:
            return '1'

        if value == False:
            return '0'

        raise ValueError(value)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def html_nested(struct) -> str:
        """
        Returns the HTML code of nested elements.

        :param struct: The structure of the nested elements.
        """
        html = StringIO()
        Html.__html_nested_helper(struct, html)

        return html.getvalue()

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __escape(text: str, quote: bool = True) -> str:
        """
        Returns a string with special characters converted to HTML entities.

        :param text: The string with optionally special characters.
        :param bool quote: Whether the quotation characters, both double quote (") and single quote (')
                           characters are also translated.
        """
        text = text.replace("&", "&amp;")  # Must be done first!
        text = text.replace("<", "&lt;")
        text = text.replace(">", "&gt;")
        if quote:
            text = text.replace('"', "&quot;")
            text = text.replace('\'', "&#x27;")

        return text

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __html_nested_helper(struct, html: StringIO) -> None:
        """
        Helper method for method generateNested().

        :param struct: The (nested) structure of the HTML code.
        :param html: The generated HTML code.
        """
        if struct is not None:
            if type(struct) is list:
                #  Structure is a list of elements.
                for element in struct:
                    Html.__html_nested_helper(element, html)

            elif struct.tag is not None:
                if struct.inner is not None:
                    Html.__html_tag_helper(struct.tag, struct.attr, html)
                    Html.__html_nested_helper(struct.inner, html)
                    html.write(f'</{struct.tag}>')

                elif struct.text is not None:
                    Html.__html_tag_helper(struct.tag, struct.attr, html)
                    html.write(Html.txt2html(struct.text))
                    html.write(f'</{struct.tag}>')

                elif struct.html is not None:
                    Html.__html_tag_helper(struct.tag, struct.attr, html)
                    html.write(struct.html)
                    html.write(f'</{struct.tag}>')

                else:
                    Html.__html_void_element_helper(struct.tag, struct.attr, html)

            elif struct.inner is not None:
                Html.__html_nested_helper(struct.inner, html)

            elif struct.text is not None:
                html.write(Html.txt2html(struct.text))

            elif struct.html is not None:
                html.write(struct.html)

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __html_tag_helper(tag: str, attr: Dict[str, str | List[str]] | None, html: StringIO) -> None:
        """
        Generates the HTML code for a start tag of an element.

        :param tag: The name of the tag, e.g., a, form.
        :param attr: The attributes of the tag.
                     Special characters in the attributes will be replaced with HTML entities.
        :param html: The generated HTML code.
        """
        html.write('<')
        html.write(tag)
        if attr is not None:
            for name, value in attr.items():
                Html.__html_attribute_helper(name, value, html)
        html.write('>')

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __html_attribute_helper(name: str, value: Any, html: StringIO) -> None:
        """
        Returns a string with proper conversion of special characters to HTML entities of an attribute of an HTML tag.

        :param name: The name of the attribute.
        :param value: The value of the attribute.
        :param html: The generated HTML code.
        """
        if name in ['autofocus',
                    'checked',
                    'disabled',
                    'hidden',
                    'ismap',
                    'multiple',
                    'novalidate',
                    'readonly',
                    'required',
                    'selected',
                    'spellcheck']:
            # Boolean attributes.
            if value:
                html.write(f'< {name}="{name}">')

        elif name == 'draggable':
            if value is not None:
                if value == 'auto':
                    html.write(' draggable="auto"')
                elif not value or value == 'false':
                    html.write(' draggable="false"')
                else:
                    html.write(' draggable="true"')

        elif name == 'contenteditable':
            if value is not None:
                if value:
                    html.write(' contenteditable="true"')
                else:
                    html.write(' contenteditable="false"')

        elif name == 'autocomplete':
            if value is not None:
                if value:
                    html.write(' autocomplete="on"')
                else:
                    html.write(' autocomplete="off"')

        elif name == 'translate':
            if value is not None:
                if value:
                    html.write(' translate="yes"')
                else:
                    html.write(' translate="no"')

        elif name == 'class':
            classes = Html.__clean_classes(value)
            if classes:
                html.write(' class="')
                html.write(' '.join(classes))
                html.write('"')

        else:
            if value is not None and value != '':
                html.write(f' {Html.txt2html(name)}="{Html.txt2html(value)}"')

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __html_void_element_helper(tag: str, attr: Dict[str, str] | None, html: StringIO) -> None:
        """
        Generates the HTML code for a void element.

        :param tag: The name of the tag, e.g., img, link.
        :param attr: The attributes of the tag.
                     Special characters in the attributes will be replaced with HTML entities.
        :param html: The generated HTML code.
        """
        html.write('<')
        html.write(tag)
        if attr is not None:
            for name, value in attr.items():
                Html.__html_attribute_helper(name, value, html)
        html.write('/>')

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def __clean_classes(classes: Any) -> List[str]:
        """
        Removes empty and duplicate classes from a list of classes.

        :param classes: The list of classes.
        """
        clean = set()

        if type(classes) is list:
            for cls in classes:
                cls = Html.txt2html(cls).strip()
                if cls != '':
                    clean.add(cls)
        else:
            cls = Html.txt2html(classes).strip()
            if cls != '':
                clean.add(cls)

        clean = list(clean)
        clean.sort()

        return clean

# ----------------------------------------------------------------------------------------------------------------------
