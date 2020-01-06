from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout #describe things proportionally so that it works
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout # puts each child in a grid
#from kivy.uix.button import Button
"""
General notes:
The order in which you add widgets is important
"""

class ScatterTextWidget(BoxLayout):
    pass

class TutorialApp(App):
    def build(self): # you need to build the app
        b = BoxLayout(orientation = 'vertical')
        t = TextInput(font_size = 150,
                    size_hint_y = None, #for the box hint
                    height = 200,
                    text = 'default')
        f = FloatLayout() # this is the first one listed, so everything else must be a child
        s = Scatter()
        l = Label(text = "default",
                    font_size = 150,
                    ) # label inside the scatter widget
        t.bind(text = l.setter('text'))
        f.add_widget(s)
        s.add_widget(l)

        b.add_widget(t) #this displays at the top because it's first
        b.add_widget(f)
        return b




if __name__ == "__main__":
    TutorialApp().run()
