"""
 python -m PyInstaller main.spec

"""
from kivy.uix.button import Button
from kivy.uix.label import Label
import sqlite3
import sqlalchemy
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import os, sys
from kivy.resources import resource_add_path, resource_find
from random import randint
import file_opening
from db_section import add_record
from os import path
path_to_data = path.abspath(path.join(path.dirname(__file__)))

Builder.load_file("main.kv")

class MenuScreen(Screen):
    pass


class AddNewList(Screen):
    pass


class ViewLists(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(AddNewList(name='add_list'))
sm.add_widget(ViewLists(name='view_list'))


class MainApp(App):
    def build(self):
        return sm

    def save(self, name, plate, date):
        add_record(name, plate, date)

    def read(self):
        file_opening.get_template(randint(1, 100))

if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    MainApp().run()
