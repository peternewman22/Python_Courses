import kivy

from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.base import runTouchApp # quick example
from kivy.lang import Builder #parses Kivy language

# so we can put everying in the one file
Builder.load_string("""
<ScrollableLabel>:
    text: str('some really really really long string') * 10
    font_size: 50
    text_size: self.size
""")

class ScrollableLabel(Label):
    pass

runTouchApp(ScrollableLabel)
