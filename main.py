from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screenclear
from home_page import HomePage
from scan_page import ScanPage
from play_page import PlayPage

class MusicApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomePage(name='home'))
        sm.add_widget(ScanPage(name='scan'))
        sm.add_widget(PlayPage(name='play'))
        return sm

if __name__ == '__main__':
    MusicApp().run()
c





