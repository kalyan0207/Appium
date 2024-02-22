import json
from appium import webdriver


def drivermethod():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['deviceName'] = 'Mi A3'
    desired_caps['udid'] = 'emulator-5554'
    # desired_caps['udid'] = 'c2a7fb793471'  #'ZF6224GFW3'  # '93JAY0BVHM'
    desired_caps['app'] = 'C:\\Users\\kosaikal\\Downloads\\MX Player_1.70.2_Apkpure.apk'
    desired_caps['appPackage'] = 'com.mxtech.videoplayer.ad'
    desired_caps['appActivity'] = 'com.mxtech.videoplayer.ad.ActivityWelcomeMX'
    desired_caps['noReset'] = True

    driver = webdriver.Remote("http://127.0.0.1:4724/wd/hub", desired_caps)

    # allure.attach(json.dumps(desired_caps, indent=2), name="Desired Capabilities",
    #               attachment_type=allure.attachment_type.JSON)

    # return driver

    # def create_driver():
    #    desired_caps = drivermethod()
    #    allure.attach(json.dumps(desired_caps, indent=2), name="Desired Capabilities",
    #                  attachment_type=allure.attachment_type.JSON)
    #    return webdriver.Remote("http://127.0.0.1:4727/wd/hub", desired_caps)

    # Call the create_driver function to create your driver instance
    # driver = create_driver()
    return driver
