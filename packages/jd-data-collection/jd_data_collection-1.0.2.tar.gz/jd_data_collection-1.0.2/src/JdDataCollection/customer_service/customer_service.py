"""
Copyright (c) 2025-now Martian Bugs All rights reserved.
Build Date: 2025-02-11
Author: Martian Bugs
Description: 客服模块数据采集
"""

from DrissionPage import Chromium

from .reception_data import ReceptionData


class CustomerService:
    def __init__(self, browser: Chromium):
        self._browser = browser

        self._reception_data = None

    @property
    def reception_data(self):
        if self._reception_data is None:
            self._reception_data = ReceptionData(self._browser)

        return self._reception_data
