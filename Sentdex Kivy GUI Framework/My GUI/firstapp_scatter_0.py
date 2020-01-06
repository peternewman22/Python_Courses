from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout #describe things proportionally so that it works
#from kivy.uix.button import Button
class TutorialApp(App):
    def build(self): # you need to build the app
        f = FloatLayout() # this is the first one listed, so everything else must be a child
        s = Scatter()
        l = Label(text = "Hello!",
                    font_size = 150) # label inside the scatter widget

        f.add_widget(s)
        s.add_widget(l)
        return f



if __name__ == "__main__":
    TutorialApp().run()
