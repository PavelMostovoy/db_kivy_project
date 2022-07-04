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
from db_section import add_record


Builder.load_file("main.kv")
# Builder.load_string("""<MenuScreen>:
#     BoxLayout:
#         Button:
#             text: 'Add New List'
#             on_press: root.manager.current = 'add_list'
#         Button:
#             text: 'View Staff Profile'
#             on_press : root.manager.current  ='view_list'
#         Button:
#             text: 'Salary report'
#
# <AddNewList>:
#     name: str(name_input)
#     date: date
#     plate: plate
#     number: number
#     GridLayout:
#         cols: 2
#         Label:
#             text: 'Name'
#         TextInput:
#             id: name_input
#             multiline: False
#         Label:
#             text: 'Plate'
#         TextInput:
#             id: plate
#         Label:
#             text: 'Date'
#         TextInput:
#             id: date
#         Label:
#             text: 'Number'
#         TextInput:
#             id: number
#         Button:
#             text: 'Back to menu'
#             on_press: root.manager.current = 'menu'
#         Button:
#             text: 'Save'
#             on_press: app.save(name_input.text, plate.text, date.text)
#             on_release:
#                 name_input.text = ""
#                 date.text = ""
#                 plate.text = ""
#                 number.text = ""
#
#
# <ViewLists>:
#     name: driver_name
#     plate: plate_number
#     list: list_number
#     data: list_date
#     GridLayout:
#         cols: 2
#         Label:
#             text: 'Driver Name'
#             multiline: False
#         TextInput:
#             id: driver_name
#             multiline: False
#         Label:
#             text: 'Plate Number'
#         TextInput:
#             id: plate_number
#         Label:
#             text: 'List Number'
#         TextInput:
#             id: list_number
#         Label:
#             text: 'Date'
#         TextInput:
#             id: list_date
#         Button:
#             text: 'Back to menu'
#             on_press: root.manager.current = 'menu'
#         Button:
#             text: 'Show'
#             on_press: app.read()""")


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
        pass

if __name__ == '__main__':
    MainApp().run()
