from pythonProject.appiumpython.MX_player.base.base_page import BasePage


class Online(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def video(self):
        self.click_element("online", "id")

    def search(self):
        self.click_element("go_to_search","id")

    def type_text(self):
        self.send_text("the fast and furious", "search_title", "id")

