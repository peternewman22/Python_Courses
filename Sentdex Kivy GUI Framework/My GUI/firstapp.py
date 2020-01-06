from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
#from kivy.uix.button import Button
class TutorialApp(App):
    def build(self): # you need to build the app
        # put a main widget in, and everything else is a subwidget
        return Button(text = "Hello!",
                    background_color = (0, 0, 1, 1), # RBG values
                    font_size = 150
                    )


if __name__ == "__main__":
    TutorialApp().run()
