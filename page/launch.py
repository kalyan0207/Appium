import time
from appium.webdriver.common.appiumby import AppiumBy
from pythonProject.appiumpython.MX_player.base.driverpage import drivermethod
from pythonProject.appiumpython.MX_player.base.base_page import BasePage
from pythonProject.appiumpython.MX_player.utilities.loggs import customLogger as cl

d1 = drivermethod()
b1 = BasePage(d1)

log = cl()
log.info("launch")


class Launch(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

     # def click_allow(self):
     #    self.click_element("Allow", "text")

    # def music(self):
    #     self.click_element("Music", "text")
    #
    # def search(self):
    #     self.click_element("search", "id")


    # def tracks(self):
    #  self.click_element("Tracks","text")

# class Launch:
#     def click_allow(self):
#         ele_id = d1.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Allow")')
#         ele_id.click()
#         time.sleep(5)
