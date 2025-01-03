from typing import Dict


class Html:
    """
    Utility class with functions for generating HTML code.
    """

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def escape(text: str, quote: bool = True) -> str:
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
    def generate_attribute(name: str, value: str) -> str:
        """
        Returns a string proper conversion of special characters to HTML entities of an attribute of a HTML tag.

        :param name: The name of the attribute.
        :param value: The value of the attribute.
        """
        html = ''

        # Boolean attributes.
        if name in ('autofocus',
                    'checked',
                    'disabled',
                    'hidden',
                    'ismap',
                    'multiple',
                    'novalidate',
                    'readonly',
                    'required',
                    'selected',
                    'spellcheck'):
            if value:
                html += ' '
                html += name
                html += '="'
                html += name
                html += '"'

        # Annoying boolean attribute exceptions.
        elif name in ('draggable', 'contenteditable'):
            if value is not None:
                html += ' '
                html += name
                html += '="true"' if value else '="false"'

        elif name == 'autocomplete':
            if value is not None:
                html += ' '
                html += name
                html += '="on"' if value else '="off"'

        elif name == 'translate':
            if value is not None:
                html += ' '
                html += name
                html += '="yes"' if value else '="no"'

        else:
            if value is not None and value != '':
                html += ' '
                html += Html.escape(name)
                html += '="'
                html += Html.escape(value)
                html += '"'

        return html

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def generate_element(tag_name: str,
                         attributes: Dict[str, str] | None = None,
                         inner_text: str = '',
                         is_html: bool = False) -> str:
        """
        Generates HTML code for an element.

        Note: tags for void elements such as '<br/>' are not supported.

        :param tag_name: The name of the tag, e.g., a, form.
        :param dict[str,str]|None attributes: The attributes of the tag. Special characters in the attributes will be
                                              replaced with HTML entities.
        :param inner_text: The inner text of the tag.
        :param bool is_html: If set the inner text is a HTML snippet, otherwise special characters in the inner text
                             will be replaced with HTML entities.
        """
        html = Html.generate_tag(tag_name, attributes)
        html += inner_text if is_html else Html.escape(inner_text)
        html += '</'
        html += tag_name
        html += '>'

        return html

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def generate_tag(tag_name: str, attributes: Dict[str, str] | None = None) -> str:
        """
        Generates HTML code for a start tag of an element.

        :param tag_name: The name of the tag, e.g. a, form.
        :param dict[str,str]|None attributes: The attributes of the tag. Special characters in the attributes will be
                                              replaced with HTML entities.
        """
        html = '<'
        html += tag_name
        for key in sorted(attributes):
            html += Html.generate_attribute(key, attributes[key])
        html += '>'

        return html

    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def generate_void_element(tag_name: str, attributes: Dict[str, str] | None = None) -> str:
        """
        Generates HTML code for an element.

        Note: tags for void elements such as '<br/>' are not supported.

        :param tag_name: The name of the tag, e.g., a, form.
        :param dict[str,str]|None attributes: The attributes of the tag. Special characters in the attributes will be
                                              replaced with HTML entities.
        """
        html = '<'
        html += tag_name
        for key in sorted(attributes):
            html += Html.generate_attribute(key, attributes[key])
        html += '/>'

        return html

# ----------------------------------------------------------------------------------------------------------------------
