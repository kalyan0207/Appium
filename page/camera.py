from pythonProject.appiumpython.MX_player.base.driverpage import drivermethod
from pythonProject.appiumpython.MX_player.base.base_page import BasePage
from pythonProject.appiumpython.MX_player.utilities.loggs import customLogger as cl


class Camera(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def camera_video(self):
        self.click_element("Camera", "text")

    def click_video(self):
        self.click_element("origin_ui_container", "id")

    def click_skip(self):
        self.click_element("Skip", "text")

    def click_center(self):
        self.tap(414, 1218, 1)

    def click_play(self):
        self.click_element("playpause", "id")

    def click_next(self):
        self.click_element("next", "id")

    def click_prev(self):
        self.click_element("prev", "id")

    def click_zoom(self):
        self.click_element("zb_left", "id")
