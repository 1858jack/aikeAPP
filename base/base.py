from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def __init__(self):
        # 定义空字典
        desired_caps = {}
        # 指定平台名称 必须写对
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        # 不能为空，可以随便写
        desired_caps['deviceName'] = 'emulator-5554'
        # 包名/
        desired_caps['appPackage'] = 'com.vcooline.aike'
        # 启动名
        desired_caps['appActivity'] = '.umanager.LoginActivity'

        # 声明机驱动对象
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # 隐式等待
        self.driver.implicitly_wait(10)


    # 获取元素
    def base_find(self,lco):
        return WebDriverWait(self.driver
                             ,timeout=30,
                             poll_frequency=0.5).until(lambda x:x.find_element(*lco))
    # 点击
    def base_click(self,lco):
        self.base_find(lco).click()

    # 输入
    def base_input(self,lco,value):
        ru=self.base_find(lco)
        ru.clear()
        ru.send_keys(value)

if __name__ == '__main__':
    Base()