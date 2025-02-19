# -*- coding: utf-8 -*-
"""
    proxy.py
    ~~~~~~~~
    ⚡⚡⚡ Fast, Lightweight, Pluggable, TLS interception capable proxy server focused on
    Network monitoring, controls & Application development, testing, debugging.

    :copyright: (c) 2013-present by Abhinav Singh and contributors.
    :license: BSD, see LICENSE for more details.
"""
import re
import socket
import binascii

import unittest

from proxy.socks import Socks4Packet, socks4Operations


def unhexlify(raw: str) -> bytes:
    return binascii.unhexlify(re.sub(r'\s', '', raw))


# Examples taken from https://en.wikipedia.org/wiki/SOCKS
CLIENT_CONNECT_REQ = unhexlify('04 01 00 50 42 66 07 63 46 72 65 64 00')
SERVER_CONNECT_OK = unhexlify('00 5A')


class TestSocks4Packet(unittest.TestCase):

    def test_pack(self) -> None:
        pkt = Socks4Packet()
        pkt.vn = 4
        pkt.cd = socks4Operations.CONNECT
        pkt.dstport = 80
        pkt.dstip = socket.inet_aton('66.102.7.99')
        pkt.userid = b'Fred'
        self.assertEqual(
            pkt.pack(),
            CLIENT_CONNECT_REQ,
        )

    def test_parse(self) -> None:
        wiki = memoryview(CLIENT_CONNECT_REQ)
        pkt = Socks4Packet()
        pkt.parse(wiki)
        self.assertEqual(pkt.vn, 4)
        self.assertEqual(pkt.cd, socks4Operations.CONNECT)
        self.assertEqual(pkt.dstport, 80)
        assert pkt.dstip
        self.assertEqual(socket.inet_ntoa(pkt.dstip), '66.102.7.99')
        self.assertEqual(pkt.userid, b'Fred')
