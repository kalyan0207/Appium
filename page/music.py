from pythonProject.appiumpython.MX_player.page.launch import Launch
from pythonProject.appiumpython.MX_player.base.driverpage import drivermethod
from pythonProject.appiumpython.MX_player.base.base_page import BasePage
from pythonProject.appiumpython.MX_player.utilities.loggs import allureLogs as al


class Music(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def music_page(self):
        self.click_element("Music", "text")
        al("opened music page")

    # def tracks(self):
    #     self.click_element("Tracks", "text")

    def playlists(self):
        self.click_element("Playlists", "text")

    def album(self):
        self.click_element("Albums", "text")

    # def artists(self):
    #     self.click_element("Artists", "text")

    # def folders(self):
    #     self.click_element("Folders", "text")

# d1 = drivermethod()
#
# obj = Launch(d1)
# obj.click_allow()
# time.sleep(5)
#
# obj.music()
# time.sleep(5)
