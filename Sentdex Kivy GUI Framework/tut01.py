import kivy
from kivy.app import App
from kivy.uix.label import Label # so you can add text
kivy.require("1.11.1") #consistency
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # run the init method from GridLayout
        self.cols = 2
        # get IP
        self.add_widget(Label(text="IP:"))
        self.ip = TextInput(multiline=False)
        self.add_widget(self.ip)
        # get port
        self.add_widget(Label(text="port:"))
        self.port = TextInput(multiline=False)
        self.add_widget(self.port)
        # get username
        self.add_widget(Label(text="Username:"))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)


class EpicApp(App):
    def build(self): # initialization
        return ConnectPage()



if __name__ == "__main__":
    EpicApp().run()
