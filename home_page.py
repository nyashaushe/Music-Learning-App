from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file('kv/home_page.kv')

class HomePage(Screen):
    def__init__(self,play):
    self.play = play
    
    
    
    
