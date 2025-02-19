"""
Copyright (c) 2025-now Martian Bugs All rights reserved.
Build Date: 2025-02-10
Author: Martian Bugs
Description: 客服IM模块数据采集
"""

from DrissionPage import Chromium

from .data import Data


class Im:
    def __init__(self, browser: Chromium):
        self._browser = browser

        self._data = None

    @property
    def data(self):
        """客服数据采集"""

        if self._data is None:
            self._data = Data(self._browser)

        return self._data
