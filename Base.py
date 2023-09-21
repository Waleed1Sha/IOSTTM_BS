from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
import pytest


class BaseTest:
    @pytest.fixture
    def driver(self, request):
        desired_caps = {
            'platformName': 'Android',
            'appium:app': "C://Users//zeesh//OneDrive//Desktop//Rakesh2.apk",
            'appium:deviceName': 'vivo 1907_19',
            'appium:platformVersion': '12.0',
            'appium:automationName': 'uiautomator2',
            'appPackage': 'com.photogauge.masterapp',
            'appActivity': 'com.photogauge.masterapp.ui.presenter.splash.LauncherActivity',
            'autoGrantPermissions': True
        }

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(10)

        def fin():
            driver.quit()

        request.addfinalizer(fin)
        return driver
