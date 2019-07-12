from v4 import page
from v4.base.base import Base


class PageLogin(Base):
    def page_input_tel(self, tel):
        self.base_input(page.login_tel, tel)

    def page_input_pwd(self, pwd):
        self.base_input(page.login_pwd, pwd)

    def page_click_btn(self):
        self.base_click(page.login_btn)

    def page_login(self, tel, pwd):
        self.page_input_tel(tel)
        self.page_input_pwd(pwd)
        self.page_click_btn()




