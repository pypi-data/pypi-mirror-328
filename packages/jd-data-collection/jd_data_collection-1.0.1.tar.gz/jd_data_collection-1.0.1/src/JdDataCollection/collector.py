"""
Copyright (c) 2025-now Martian Bugs All rights reserved.
Build Date: 2025-02-11
Author: Martian Bugs
Description: 数据采集器
"""

from DrissionPage import Chromium, ChromiumOptions

from .customer_service.customer_service import CustomerService


class Collector:
    """采集器. 使用之前请先调用 `connect_browser` 方法连接浏览器."""

    def __init__(self):
        self._service = None

        self._customer_service = None

    def connect_browser(self, port: int):
        """
        连接浏览器

        Args:
            port: 浏览器调试端口号
        """

        chrome_options = ChromiumOptions(read_file=False)
        chrome_options.set_local_port(port=port)

        self.browser = Chromium(addr_or_opts=chrome_options)

    @property
    def customer_service(self):
        """采集客服模块数据"""

        if self._customer_service is None:
            self._customer_service = CustomerService(self.browser)

        return self._customer_service
