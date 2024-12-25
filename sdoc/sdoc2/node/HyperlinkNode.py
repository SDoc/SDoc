from typing import Dict
from urllib import request

import httplib2
from cleo.io.io import IO

from sdoc.sdoc2.node.Node import Node
from sdoc.sdoc2.NodeStore import NodeStore


class HyperlinkNode(Node):
    """
    SDoc2 node for hyperlinks.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def __init__(self, *, io: IO, options: Dict[str, str], argument: str):
        """
        Object constructor.

        :param io: The IO object.
        :param options: The options of the hyperlink.
        :param argument: Not used.
        """
        Node.__init__(self, io=io, name='hyperlink', options=options, argument=argument)

    # ------------------------------------------------------------------------------------------------------------------
    def get_html_attributes(self) -> Dict[str, str]:
        """
        Checks valid HTML attributes for hyperlinks and returns a list of attributes.
        """
        valid_html_attributes = ('href', 'class', 'id', 'download', 'hreflang', 'media', 'rel', 'target', 'type')
        attributes_dict = {}

        for key, value in self._options.items():
            if key in valid_html_attributes:
                attributes_dict[key] = value

        return attributes_dict

    # ------------------------------------------------------------------------------------------------------------------
    def prepare_content_tree(self) -> None:
        """
        Prepares the content of the node. Checks URL of 'href' attribute. Sets if needed.
        """
        if 'href' in self._options:
            self.set_scheme(self._options['href'])
        else:
            self.set_scheme(self.argument)

        # Trying to connect
        self.try_connect()

    # ------------------------------------------------------------------------------------------------------------------
    def set_scheme(self, url: str):
        """
        Checks if we haven't got a scheme. Sets the scheme if needed.

        :param url: The URL with scheme or without.
        """
        if not request.urlparse(url).scheme:
            if url.startswith('ftp.'):
                url = 'ftp://{0!s}'.format(url)
                self._options['href'] = url
            else:
                url = 'http://{0!s}'.format(url)
                self._options['href'] = url

    # ------------------------------------------------------------------------------------------------------------------
    def try_connect(self) -> None:
        """
        Tries to connect to the URL. On a successful connection, checks for a redirect. If redirected to protocol https
        and host is the same, updates the protocol in the URL.
        """
        try:
            response = request.urlopen(self._options['href'])

            # Check if we can connect to host.
            if response.getcode() not in range(200, 400):
                self.io.warning("Cannot connect to: '{0!s}'".format(self._options['href']))
            else:
                # If we connected, check the redirect.
                url = self._options['href'].lstrip('(http://)|(https://)')
                split_url = url.split('/')

                host = split_url[0]
                address = '/'.join(split_url[1:])

                connection = httplib2.HTTPConnectionWithTimeout(host)
                connection.request('HEAD', address)
                response = connection.getresponse()

                if response.status in range(301, 304):
                    # If host of redirected is the same, reset 'href' option
                    if response.getheader('Location').startswith('https://' + url):
                        self._options['href'].replace('http://', 'https://')

        except Exception as exception:
            self.io.warning("Unable to retrieve URL: '{0!s}'".format(self._options['href']))
            self.io.warning(str(exception.__class__))
            self.io.warning(str(exception))

    # ------------------------------------------------------------------------------------------------------------------
    def is_phrasing(self) -> bool:
        """
        Returns True.
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    def is_inline_command(self) -> bool:
        """
        Returns True.
        """
        return True

    # ------------------------------------------------------------------------------------------------------------------
    def is_block_command(self) -> bool:
        """
        Returns False.
        """
        return False


# ----------------------------------------------------------------------------------------------------------------------
NodeStore.register_inline_command('hyperlink', HyperlinkNode)
