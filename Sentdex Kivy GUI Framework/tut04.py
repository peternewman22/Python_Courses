"""
Scheduling
"""

import kivy
import os
from kivy.app import App
from kivy.uix.label import Label # so you can add text
kivy.require("1.11.1") #consistency
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import socket_client
import sys


class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # run the init method from GridLayout
        self.cols = 2
        # get IP
        if os.path.isfile("prev_details.text"):
            with open("prev_details.text","r") as f:
                d = f.read().split(",")
                prev_ip = d[0]
                prev_port = d[1]
                prev_username = d[2]
        else:
            prev_ip = ""
            prev_port = ""
            prev_username = ""

        self.add_widget(Label(text="IP:"))
        self.ip = TextInput(text = prev_ip, multiline=False)
        self.add_widget(self.ip)
        # get port
        self.add_widget(Label(text="port:"))
        self.port = TextInput(text = prev_port,multiline=False)
        self.add_widget(self.port)
        # get username
        self.add_widget(Label(text="Username:"))
        self.username = TextInput(text = prev_username,multiline=False)
        self.add_widget(self.username)
        # add Button
        self.join = Button(text = "Join")
        self.join.bind(on_press = self.join_button)
        self.add_widget(Label())
        self.add_widget(self.join)

    def join_button(self, instance):
        # everything is running live
        # scheduling comes later
        port = self.port.text
        ip = self.ip.text
        username = self.username.text
        #print(f"Attempting to join {ip}:{port} as {username}")
        with open("prev_details.text", "w") as f:
            f.write(f"{ip},{port},{username}")
        # when someone clicks join...
        info = f"Attempting to join {ip}:{port} as {username}"
        # update the info page
        chat_app.info_page.update_info(info)
        #then switch screens to the info page
        chat_app.screen_manager.current = "Info"
        Clock.schedule_once(self.connect, 1)

    def connect(self, _): #_ passes instance AND the seconds in the schedule from start
    # could schedule on a cycle
        port = int(self.port.text)
        ip = self.ip.text
        username = self.username.text

        if not socket_client.connect(ip, port, username, show_error):
            return

        chat_app.create_chat_page()
        chat_app.screen_manager.current = "Chat"

class InfoPage(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs) # run the init method from GridLayout
        self.cols = 1
        self.message = Label(halign = "center", valign = "middle", font_size=30)
        #need to bind a message to it
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)

    def update_info(self, message):
        self.message.text = message

    def update_text_width(self, *_):
        # take up 90% of the box
        self.message.text_size = (self.message.width*0.9, None)

class ChatPage(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs) # run the init method from GridLayout
        self.cols = 1
        self.add_widget(Label(text = "Hey at least it worked up to this point"))

class EpicApp(App):
    def build(self): # initialization
        #return ConnectPage()
        self.screen_manager  = ScreenManager()
        # add our pages/screens
        self.connect_page = ConnectPage()
        screen = Screen(name="Connect")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        # setting up the next page, Info
        self.info_page = InfoPage()
        screen  = Screen(name = "Info")
        screen.add_widget(self.info_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

    def creat_chat_page(self):
        self.chat_page = ChatPage()
        screen = Screen(name = "Chat")
        screen.add_widget(self.chat_page)
        self.screen_manager.add_widget(screen)

def show_error(message):
    chat_app.info_page.update_info(message)
    chat_all.screen_manager.current = "Info"
    Clock.schedule_once(sys.exit, 10)

if __name__ == "__main__":
    chat_app = EpicApp()
    chat_app.run()
