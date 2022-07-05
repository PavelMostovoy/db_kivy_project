"""
 python -m PyInstaller main.spec

"""
import json

from kivy.properties import StringProperty
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
from db_section import add_record, get_all_records_by_id
from os import path

path_to_data = path.abspath(path.join(path.dirname(__file__)))

Builder.load_file("main_screen.kv")


class MenuScreen(Screen):
    pass


class AddNewList(Screen):
    pass


class ViewLists(Screen):
    pass


class ViewReport(Screen):
    default_txt = StringProperty('Click to Show report')
    pass


sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(AddNewList(name='add_list'))
sm.add_widget(ViewLists(name='view_list'))
sm.add_widget(ViewReport(name='view_report'))


class MainApp(App):
    def build(self):
        return sm

    __last_result = {}

    def save(self, name, plate, date):
        add_record(name, plate, date)
        file_opening.get_template(randint(1, 100))

    def read(self, driver_name, plate_number, list_number):
        # file_opening.get_template(randint(1, 100))
        data = get_all_records_by_id(driver_name, plate_number, list_number)
        self.__last_result = data


    def last_result(self):
        data = json.dumps(self.__last_result)
        return data


if __name__ == '__main__':
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    MainApp().run()
