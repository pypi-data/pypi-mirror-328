class Cloudflare(object):
    """
    This is a Cloudflare object.
    """

    def change_always_use_https(self, value: str) -> tuple[int, str]:
        """
        Change always use https.
        :param str value: on|off
        :returns: [status_code, result]
        :rtype: tuple[int, str]
        .. note::
           Invoice query function first to get zone id.
        """
        pass

    def change_automatic_https_rewrites(self, value: str) -> tuple[int, str]:
        """
        Change automatic https rewrites.
        :param str value: on|off
        :returns: [status_code, result]
        :rtype: tuple[int, str]
        .. note::
           Invoice query function first to get zone id.
        """
        pass

    def change_ssl_model(self, value: str) -> tuple[int, str]:
        """
        Change ssl model.
        :param str value: off|flexible|full|strict|origin_pull
        :returns: [status_code, result]
        :rtype: tuple[int, str]
        .. note::
           Invoice query function first to get zone id.
        """
        pass

    def dns_create_record(self, _type: str, name: str, content: str, proxied: int, ttl: int) -> tuple[int, str]:
        """
        Create a dns record.
        :param str _type: The type of the dns record.
        :param str name: The name of the dns record.
        :param str content: The content of the dns record. If is mx record, content is ``content|priority``.
        :param int proxied: The dns record is proxied.
        :param int ttl: The ttl of the dns record.
        :returns: [status_code, result]
        :rtype: tuple[int,str]
        .. note::
           Invoice query function first to get zone id.
        """
        pass

    def dns_delete_record(self, record_id: str) -> tuple[int, str]:
        """
        Create a dns record.
        :param str record_id: The id of the dns record is to delete.
        :returns: [status_code, result]
        :rtype: tuple[int,str]
        .. note::
           Invoice query function first to get zone id.
        """
        pass

    def dns_ensured_record(self, domain: str, type: str, name: str, content: str, proxied: int, ttl: int, state: int,
                           solo: int) -> tuple[int, str]:
        """
        Ensure a dns record for a domain on Cloudflare.
        :param str name: www.example.com.
        :param str domain: example.com.
        :param str type: A, CNAME, TXT, AAAA.
        :param str content: 8.8.8.8. The content of the dns record. If is mx record, content is ``content|priority``.
        :param bool proxied: True|False TXT proxy should be False
        :param int ttl: 1~65535
        :param bool state: True|False
        :param bool solo: True|False
        :returns: [status_code, result]
        :rtype: tuple[int, str]
        .. note::
           Invoice query function first to get zone id.
        Examples:
        ---------
            hello world!
        """
        pass

    def fib(self, num: int) -> int:
        """
        Calculate a Fibonacci sequence.
        :param int num: The max number to calculate.
        :returns: the result of fib
        :rtype: int
        """
        pass

    def fputs(self, filename: str, content: str) -> int:
        """
        Write content to a given filename.
        :param str filename: the file to save.
        :param str content: the content to save.
        :returns: the bytes write to file.
        :rtype: int
        """
        pass

    def get(self, endpoint) -> tuple[int, str]:
        """
        Invoke a get request to cloudflare endport.

        :param str endpoint: '/zones'
        :returns: [status_code, result]
        :rtype: tuple[int, str]
        """
        pass

    def dns_get_records(self, domain: str, type: str | None = None, name: str | None = None,
                        content: str | None = None) -> tuple[int, str]:
        """
        Get a domain's dns records.
        :param str domain: The domain name to find.
        :param str type: The dns record type to search.
        :param str name: The name of the record to search.
        :param str content: The content of the record to search.
        :returns: [status_code, result]
        :rtype: tuple[int, str]
        """
        pass

    def purge_cache(self) -> tuple[int, str]:
        """
        Purge domain cache.
        :returns: [status_code, result]
        :rtype: tuple[int, str]
        .. note::
           Invoice query function first to get zone id.
        """
        pass

    def query(self, domain: str) -> tuple[int, str]:
        """
        Query a domain from cloudflare.

        :param str domain: example.com
        :returns: [status_code, result]
        :rtype: tuple[int, str]
        """
        pass

    def dns_update_record(self, record_id: str, _type: str, name: str, content: str, proxied: int, ttl: int) -> tuple[
        int, str]:
        """
        Create a dns record.
        :param str record_id: The id of the dns record is to update.
        :param str _type: The type of the dns record.
        :param str name: The name of the dns record.
        :param str content: The content of the dns record. If is mx record, content is content|priority.
        :param int proxied: The dns record is proxied.
        :param int ttl: The ttl of the dns record.
        :returns: [status_code, result]
        :rtype: tuple[int,str]
        .. note::
           Invoice query function first to get zone id.
        """
        pass

    def __init__(self, email: str, account: str, api_token: str, proxy: str | None = None, api_url: str | None = None):
        """
        Initialize a cloudflare instance.
        :param str email: account email address.
        :param str account: account id.
        :param str api_token: api token.
        :param str|None proxy: proxy address.
        :param str|None api_url: cloudflare https endpoint.
        :returns: Cloudflare Object
        :rtype: Cloudflare
        """
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    account = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Cloudflare account"""

    api_token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Cloudflare token"""

    api_url = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Cloudflare default entry point url"""

    email = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Cloudflare email"""

    zone = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    zone_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


class DingTalk(object):
    """
    DingTalk(token, salt) -> DingTalk

     DingTalk Object
    """

    def send_markdown(self, title: str, content: str, at: list | None = None) -> str:
        """
        Send markdown to ding bot.
        :param str title: Message title.
        :param str content: Message content. if at user, user should be included. @156xxxx8827
        :param at: atMobiles ["156xxxx8827", "189xxxx8325"]
        :type at: list|None = None
        :returns: Response from dingding.
        :rtype: str
        """
        pass

    def send_text(self, text: str) -> str:
        """
        Send text to ding bot.
        :param str text: The text to be sent.
        :returns: Response from dingding.
        :rtype: str
        """
        pass

    def __init__(self, token: str, salt: str) -> DingTalk:
        """
        Initialize a ding talk instance.
        :param str token: Ding bot token.
        :param str salt: Ding bot salt.
        :rtype: DingTalk
        """
        pass

    @staticmethod  # known case of __new__
    def __new__(*args, **kwargs):  # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    secret = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """DingTalk secret"""

    token = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """DingTalk token"""
