import pytest

from page.login_page import Pagelogin
def getdata():
    return [(131236546,123456),(131236546,123456)]


class TestLogin:
    def setup_class(self):
        self.page=Pagelogin()


    def teardown_class(self):
       self.page.driver.quit()

    @pytest.mark.parametrize('username,pwd',getdata())
    def test_login(self,username,pwd):
        self.page.page_login(username,pwd)