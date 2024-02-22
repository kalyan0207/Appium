import json

import allure
import selenium
from allure_commons.types import AttachmentType
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, \
    NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from pythonProject.appiumpython.MX_player.utilities.loggs import customLogger as cl
import time
from pythonProject.appiumpython.MX_player.base.driverpage import drivermethod


class BasePage:
    log = cl()

    def __init__(self, driver):
        self.drivermethod = None
        self.driver = driver
        self.action = TouchAction(self.driver)

    def wait_for_element(self, locator_value, locator_type):
        locator_type = locator_type.lower()
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        if locator_type == "id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ID, locator_value))
            return element
        elif locator_type == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locator_value))
            return element
        elif locator_type == "des":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                                         'UiSelector().description("%s")' % locator_value))
            return element
        elif locator_type == "index":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(%d)" % int(locator_value)))
            return element
        elif locator_type == "text":
            element = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("%s")' % locator_value))
            return element
        elif locator_type == "xpath":
            element = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '%s' % locator_value))
            return element
        else:
            self.log.info("Locator value " + locator_value + "not found")
            self.screenShot("screenshot_wait_for_element")

        return element

    def get_element(self, locator_value, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.wait_for_element(locator_value, locator_type)
            self.log.info(
                "Element found with LocatorType: " + locator_type + " with the locatorValue :" + locator_value)
        except (ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, TimeoutException):
            self.screenShot("screenshot_element_not_found")

            self.log.info(
                "Element not found with LocatorType: " + locator_type + " and with the locatorValue :" + locator_value)

        return element

    def click_element(self, locator_value, locator_type="id"):
        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator_value, locator_type)
            element.click()
            self.log.info(
                "Clicked on Element with LocatorType: " + locator_type + " and with the locatorValue :" + locator_value)
        except (TypeError, ElementNotSelectableException, NoSuchElementException, TimeoutException, AttributeError):
            self.screenShot("screenshot_element_not_clickable")
            self.log.info(
                "Unable to click on Element with LocatorType: " + locator_type + " and with the locatorValue :" + locator_value)
            self.takeScreenshot(locator_type)
            assert False

    def get_text(self, locator_value, locator_type="id"):
        text = ""
        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator_value, locator_type)
            text = element.text
            self.log.info(
                "Text got on Element with LocatorType: " + locator_type + " and with the locatorValue :" + locator_value)

        except (TypeError, TimeoutException, AttributeError):
            self.screenShot("screenshot_element_not_clickable")
            self.log.info(
                "Unable to get Text on Element with LocatorType: " + locator_type + " and with the locatorValue :" + locator_value)
        return text

    def send_text(self, text, locator_value, locator_type="id"):
        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator_value, locator_type)
            element.send_keys(text)
            self.log.info(
                "Send text  on Element with LocatorType: " + locator_type + " and with the locatorValue :" + locator_value)
        except(selenium.common.exceptions.InvalidElementStateException, ElementNotVisibleException,
               ElementNotSelectableException, NoSuchElementException, TimeoutException, AttributeError):
            self.screenShot("screenshot_send_text")
            self.log.info(
                "Unable to send text on Element with LocatorType: " + locator_type + " and with the locatorValue :" + locator_value)

    def tap_coordiantes(self, x, y, number):

        try:
            # self.action.tap(ele, number).perform()
            self.action.tap(None, int(x), int(y), number)
            self.log.info(f"Tap Successful on x : {x} and y : {y} coordinates")
        except(ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, TimeoutException):
            self.screenShot("screenshot_tap")
            self.log.info(f"Tap UnSuccessful on coordinates")

    def tap_element(self, element, number):

        try:
            self.action.tap(element, number).perform()
            self.log.info(f"Tap Successful on element")
        except(ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, TimeoutException):
            self.screenShot("screenshot_tap")
            self.log.info(f"Tap UnSuccessful on element")

    def long_press(self, locator_value, locator_type="id"):

        try:
            locator_type = locator_type.lower()
            element = self.get_element(locator_value, locator_type)
            self.action.long_press(element, 5).perform()
            self.log.info(
                "long press on Element with LocatorType: " + locator_type + " and with the locatorValue :" + locator_value)
        except(ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, TimeoutException):
            self.screenShot("screenshot_long_press")
            self.log.info(
                "unable to long press on Element with LocatorType: " + locator_type + " and with the locatorValue :" + locator_value)

    def Swap_left_to_right(self):
        try:
            # Get Screen Size
            screen_size = self.driver.get_window_size()
            screen_width = screen_size["width"]
            screen_height = screen_size["height"]
            # Swap Left to right
            start_x = screen_width * 8 / 9
            start_y = screen_height / 2
            start_x2 = screen_width / 9

            self.action.long_press(None, start_x, start_y).move_to(None, start_x2, start_y).release().perform()
            self.log.info("Successfully Swapped from left to right")

        except (ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, TimeoutException):
            self.screenShot("screenshot_scroll_element")
            self.log.info("unSuccessfully Swapped from left to right")

    def Swap_right_to_left(self):
        try:
            # Get Screen Size
            screen_size = self.driver.get_window_size()
            screen_width = screen_size["width"]
            screen_height = screen_size["height"]

            # Swap right to left
            start_x2 = screen_width / 9
            end_x2 = screen_width * 8 / 9
            start_y2 = screen_height / 2
            end_y2 = screen_height / 2

            self.action.long_press(None, start_x2, start_y2).move_to(None, end_x2, end_y2).release().perform()
            self.log.info("Successfully Swapped from  right to left")

        except (ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, TimeoutException):
            self.screenShot("screenshot_scroll_element")
            self.log.info("unSuccessfully Swapped from right to left")

    def Swap_Bottom_to_top(self):
        try:
            screen_size = self.driver.get_window_size()
            screen_width = screen_size["width"]
            screen_height = screen_size["height"]

            start_x = screen_width / 2
            start_y = screen_height * 8 / 9
            start_x2 = screen_width / 2
            start_y2 = screen_height * 2 / 9

            self.action.long_press(None, start_x, start_y).move_to(None, start_x2, start_y2).release().perform()
            self.log.info("Successfully Swapped from  Bottom to Top")

        except (ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, TimeoutException):
            self.screenShot("screenshot_Bottom_to_top")
            self.log.info("unSuccessfully Swapped from  Bottom to Top")

    def Swap_top_to_Bottom(self):
        try:
            screen_size = self.driver.get_window_size()
            screen_width = screen_size["width"]
            screen_height = screen_size["height"]

            start_x2 = screen_width / 2
            end_x2 = screen_width / 2
            start_y2 = screen_height * 2 / 9
            end_y2 = screen_height * 8 / 9

            self.action.long_press(None, start_x2, start_y2).move_to(None, end_x2, end_y2).release().perform()
            self.log.info("Successfully Swapped from Top To Bottom")

        except (ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, TimeoutException):
            self.screenShot("screenshot_Top To Bottom")
            self.log.info("unSuccessfully Swapped from  Top To Bottom")

    # def drag_and_drop(self, element_locator_value, element_locator_type, layout_locator_value,
    #                   layout_locator_type="id"):
    #     try:
    #         element_locator_type = element_locator_type.lower()
    #         layout_locator_type = layout_locator_type.lower()
    #
    #         element = self.get_element(element_locator_value, element_locator_type)
    #         layout_element = self.get_element(layout_locator_value, layout_locator_type)
    #
    #         self.action.long_press(element).move_to(layout_element).release().perform()
    #         self.log.info(
    #             f"Successfully drag the Element with  locator type {element_locator_type} with the locator value of{element_locator_value}")
    #
    #     except (ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, TimeoutException):
    #         self.screenShot("screenshot_drag_and_drop")
    #         self.log.info(
    #             f"unSuccessfully drag the Element with  locator type {element_locator_type} with the locator value of{element_locator_value}")

    def screenShot(self, screenshot_name):
        file_name = screenshot_name + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshot_directory = "../screenshots/"
        screenshot_path = screenshot_directory + file_name
        try:
            self.driver.save_screenshot(screenshot_path)
            self.log.info("Screenshot save to Path : " + screenshot_path)

        except(ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, TimeoutException):
            self.log.info("Unable to save Screenshot to the Path : " + screenshot_path)

    def takeScreenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def scroll_to_element(self, locator_value, locator_id="text"):

        locator_id = locator_id.lower()
        try:
            scrollable_container = self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                                            'new UiScrollable(new UiSelector())')
            element = scrollable_container.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                                        f'new UiScrollable(new UiSelector()).scrollIntoView({locator_id}("{locator_value}"))')
            element.click()
            self.log.info("Scrolled to element with text: " + locator_value)
        except (ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException, TimeoutException):
            self.screenShot("screenshot_scroll_element")
            self.log.info("Unable to scroll to element with text: " + locator_value)

    def is_Displayed(self, locator_Value, locator_Type="id"):

        try:
            locator_Type = locator_Type.lower()
            element = self.get_element(locator_Value, locator_Type)
            element.is_displayed()
            self.log.info(
                " Element with LocatorType: " + locator_Type + " and with the locatorValue :" + locator_Value + "is displayed ")
            return True
        except:

            self.log.info(
                " Element with LocatorType: " + locator_Type + " and with the locatorValue :" + locator_Value + " is not displayed")
            return False

    def add_desired_capabilities_to_report(self, text):
        with allure.step("Desired Capabilities"):
            allure.attach(json.dumps(self.drivermethod, indent=2), name="Desired Capabilities",
                          attachment_type=AttachmentType.TEXT)
