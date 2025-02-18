"""
Copyright (c) 2025-now Martian Bugs All rights reserved.
Build Date: 2025-02-10
Author: Martian Bugs
Description: 服务数据模块采集
"""

from DrissionPage import Chromium

from .customer_service import CustomerService


class Service:
    def __init__(self, browser: Chromium):
        self._browser = browser

        self._customer_service = None

    @property
    def customer_service(self):
        """客服数据模块采集"""

        if self._customer_service is None:
            self._customer_service = CustomerService(self._browser)

        return self._customer_service
