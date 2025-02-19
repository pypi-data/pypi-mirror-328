# -*- coding: utf-8 -*-
"""
    proxy.py
    ~~~~~~~~
    ⚡⚡⚡ Fast, Lightweight, Pluggable, TLS interception capable proxy server focused on
    Network monitoring, controls & Application development, testing, debugging.

    :copyright: (c) 2013-present by Abhinav Singh and contributors.
    :license: BSD, see LICENSE for more details.
"""
import time
from typing import Any, Optional

from proxy import Proxy
from proxy.core.base import BaseTcpTunnelHandler
from proxy.http.responses import (
    PROXY_TUNNEL_UNSUPPORTED_SCHEME, PROXY_TUNNEL_ESTABLISHED_RESPONSE_PKT,
)


class HttpsConnectTunnelHandler(BaseTcpTunnelHandler):
    """A https CONNECT tunnel."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def handle_data(self, data: memoryview) -> Optional[bool]:
        # Queue for upstream if connection has been established
        if self.upstream and self.upstream._conn is not None:
            self.upstream.queue(data)
            return None

        # Parse client request
        self.request.parse(data)

        # Drop the request if not a CONNECT request
        if not self.request.is_https_tunnel:
            self.work.queue(PROXY_TUNNEL_UNSUPPORTED_SCHEME)
            return True

        # CONNECT requests are short and we need not worry about
        # receiving partial request bodies here.
        assert self.request.is_complete

        # Establish connection with upstream
        self.connect_upstream()

        # Queue tunnel established response to client
        self.work.queue(PROXY_TUNNEL_ESTABLISHED_RESPONSE_PKT)

        return None


def main() -> None:
    # This example requires `threadless=True`
    with Proxy(
        work_klass=HttpsConnectTunnelHandler,
        threadless=True,
        num_workers=1,
        port=12345,
    ):
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass


if __name__ == '__main__':
    main()
