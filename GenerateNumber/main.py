# import kivy
from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import random


class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()

    def generate_number(self):
        self.random_label.text = str(random.randint(0, 2000))


class MyApp(App):
    def build(self):
        return MyRoot()


randomApp = MyApp()
randomApp.run()
