from base.base import Base
import page

class Pagelogin(Base):
    def page_click(self):
       self.base_click(page.tiyan)
    def page_input_usernaem(self,username):
        self.base_input(page.login_username,username)
    def page_input_pwd(self,pwd):
        self.base_input(page.login_pwd,pwd)
    def page_click_btn(self):
        self.base_click(page.login_btn)

    def page_login(self,username,pwd):
        self.page_input_usernaem(username)
        self.page_input_pwd((pwd))
        self.page_click_btn()


