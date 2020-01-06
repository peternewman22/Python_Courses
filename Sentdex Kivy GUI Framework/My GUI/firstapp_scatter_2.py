from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout #describe things proportionally so that it works
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout # puts each child in a grid
#from kivy.uix.button import Button
import random
"""
General notes:
The order in which you add widgets is important
"""

class ScatterTextWidget(BoxLayout):
    def change_label_colour(self, *args):
        colour = [random.random() for i in range(3)] + [1]
        label = self.ids['my_label'] #refer to any id from the python side
        label.color = colour

class TutorialApp(App):
    def build(self): # you need to build the app
        return ScatterTextWidget()




if __name__ == "__main__":
    TutorialApp().run()
