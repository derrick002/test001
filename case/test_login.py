import os
import sys
sys.path.append(os.getcwd())
from v4.page.page_login import PageLogin
import pytest


def build_data():
    return [(13800001111, 123456), (13800001112, 12345)]


class TestLogin(object):

    def setup_class(self):
        self.login = PageLogin()

    def teardown_class(self):
        self.login.driver.quit()

    @pytest.mark.parametrize("tel,pwd", build_data())
    def test_login(self, tel, pwd):
        self.login.page_login(tel, pwd)
