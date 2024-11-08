from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader

Builder.load_file('kv/play_page.kv')

class PlayPage(Screen):
    def play_music(self, music_path):
        sound = SoundLoader.load(music_path)
        if sound:
            sound.play()
        else:
            return sound

      
class ()