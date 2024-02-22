import unittest
import pytest

from pythonProject.appiumpython.MX_player.base import base_page
from pythonProject.appiumpython.MX_player.page.album import Album
from pythonProject.appiumpython.MX_player.page.music import Music
from pythonProject.appiumpython.MX_player.base.driverpage import drivermethod
from pythonProject.appiumpython.MX_player.page.playlist import Playlist
from pythonProject.appiumpython.MX_player.page.camera import Camera
from pythonProject.appiumpython.MX_player.page.online import Online
from pythonProject.appiumpython.MX_player.utilities import loggs


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class Tests(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cm = Music(self.driver)
        self.pl = Playlist(self.driver)
        self.al = Album(self.driver)
        self.ca = Camera(self.driver)
        self.ol = Online(self.driver)

    @pytest.mark.run(order=1)
    def test_music(self):
        self.cm.music_page()
        self.cm.playlists()
        self.cm.album()

    @pytest.mark.run(order=2)
    def test_playlist(self):
        self.cm.playlists()
        loggs.allureLogs("opened playlist")
        self.pl.new_playlist()
        loggs.allureLogs("create new playlist")
        self.pl.enter_text()
        loggs.allureLogs("entered text")
        self.pl.enter_create()
        loggs.allureLogs("click create")
        self.pl.add_songs()
        loggs.allureLogs("add songs")
        self.pl.check_box()
        loggs.allureLogs("select the songs")
        self.pl.add_now()
        loggs.allureLogs("add songs")
        self.pl.play_all()
        loggs.allureLogs("play")
        self.pl.bottom_layout()
        loggs.allureLogs("click the bottom layout")
        self.pl.pause_play()
        loggs.allureLogs("pause the song")
        self.pl.play_next()
        loggs.allureLogs("play next song")
        self.pl.playback_speed()
        loggs.allureLogs("click speed")
        self.pl.speed_options("0.5x")
        loggs.allureLogs("0.5x entered")
        # assert self.get_element("0.5x","text") == "0.5x"
        # assert self.pl.is_Displayed("music_speed_tv", "id")
        self.pl.loop()
        loggs.allureLogs("click loop")
        self.pl.favourite()
        loggs.allureLogs("add favourite")
        self.pl.music_close()
        loggs.allureLogs("close the music")

        # self.cm.tracks()
        # self.cm.albums()
        # self.cm.artists()
        # self.cm.folders()

    @pytest.mark.run(order=3)
    def test_album(self):
        self.cm.music_page()
        self.cm.album()
        self.al.my_album()

    @pytest.mark.run(order=4)
    def test_video(self):
        self.ca.camera_video()
        self.ca.click_video()
        self.ca.click_center()
        self.ca.click_skip()
        self.ca.click_play()
        self.ca.click_next()
        self.ca.click_prev()
        self.ca.click_zoom()

    @pytest.mark.run(order=5)
    def test_online(self):
        self.ol.video()
        loggs.allureLogs("click on video")
        self.ol.search()
        # al("type search button")
        # self.ol.type_text()
        # al("enter text")


# d1 = drivermethod()
# # obj.click_allow()
# obj = Music(d1)
# obj.music_page()
# # obj.tracks()
# # obj.albums()
# # obj.artists()
# obj.playlists()
#
# obj = Playlist(d1)
# obj.new_playlist()
# obj.enter_text()
# obj.enter_create()
# obj.add_songs()
# obj.check_box()
# obj.add_now()


# obj.folders()
# obj.camera_video()
# d1.press_keycode(67)
