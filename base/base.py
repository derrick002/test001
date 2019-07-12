from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class Base(object):

    def __init__(self):

        desired_caps = {}

        # 设备信息
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.220.101:5555'
        # app信息
        # com.vcooline.aike/.umanager.LoginActivity
        desired_caps['appPackage'] = 'com.vcooline.aike'
        desired_caps['appActivity'] = 'umanager.LoginActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def base_find(self, loc, time=20, poll=0.5):
        return WebDriverWait(self.driver, timeout=time, poll_frequency=poll).until \
            (lambda x: x.find_element(*loc))

    def base_input(self, loc, values):
        ele = self.base_find(loc)
        ele.clear()
        ele.send_keys(values)

    def base_click(self, loc):
        self.base_find(loc).click()
