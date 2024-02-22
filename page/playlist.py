from pythonProject.appiumpython.MX_player.base.base_page import BasePage

_click_element = "New Playlist"
_enter_text = "Enter Playlist Name"
_enter_create = "Create"
_add_songs = "ADD SONGS"
_check_box = "check_box"
_add_now = "Add Now (1)"
_play_now = "Play All"
_bottom_layout = "music_bottom_layout"
_pause_play = "music_play"
_play_next = "music_next"
_play_backspeed = "music_speed_img"


class Playlist(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def new_playlist(self):
        self.click_element(_click_element, "text")

    def enter_text(self):
        self.send_text("Kalyan", _enter_text, "text")

    def enter_create(self):
        self.click_element(_enter_create, "text")

    def add_songs(self):
        self.click_element(_add_songs, "text")

    def check_box(self):
        self.click_element(_check_box, "id")

    def add_now(self):
        self.click_element(_add_now, "text")

    def play_all(self):
        self.click_element(_play_now, "text")

    def bottom_layout(self):
        ele = self.get_element(_bottom_layout, "id")
        self.tap_element(ele, 1)

    def pause_play(self):
        self.click_element(_pause_play, "id")

    def play_next(self):
        self.click_element(_play_next, "id")

    def playback_speed(self):
        self.click_element(_play_backspeed, "id")

    def speed_options(self, options):
        self.click_element(options, "text")

    def loop(self):
        self.click_element("music_rotate", "id")

    def favourite(self):
        self.click_element("favourite_img", "id")

    def music_close(self):
        self.click_element("usic_close", "id")
