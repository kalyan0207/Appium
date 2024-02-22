from pythonProject.appiumpython.MX_player.base.base_page import BasePage


class Album(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def my_album(self):
        ele = self.get_element("0", "index")
        self.tap_element(ele, 1)

        # ele = self.get_element("android.view.ViewGroup", "class")
        # self.tap(ele, 1)
