import kivy
kivy.require('1.7.2')
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
#setup graphics
from kivy.config import Config
Config.set('graphics','resizable',0)
#Graphics fix
from kivy.core.window import Window;
Window.clearcolor = (0,0,0,1.)
#Window.clearcolor = (1,0,0,1.)

class ButtonGrid(AnchorLayout):
    def __init__(self, **kwargs):
        super(ButtonGrid, self).__init__(**kwargs)
        self.anchor_x = 'center'
        self.anchor_y = 'center'

        self.submit = Button(text="eMac Arena", font_size=40, size_hint = (0.3, 0.3))
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)


    def pressed(self, instance):
        name = "name test"
        last = "last test"
        email = "email test"

        print("Name:", name, "Last Name:", last, "Email:", email)


class MainGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MainGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside_top = GridLayout()

        self.inside = GridLayout()
        self.inside.cols = 3

        self.inside_bottom = GridLayout()

        self.submit = Button(text="eMac Arena", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.inside.add_widget(self.submit)

        self.add_widget(self.inside_top)
        self.add_widget(self.inside)
        self.add_widget(self.inside_bottom)


    def pressed(self, instance):
        name = "name test"
        last = "last test"
        email = "email test"

        print("Name:", name, "Last Name:", last, "Email:", email)

class MyApp(App):
    def build(self):
        #this is where the root widget goes
        #should be a canvas
        #return MainGrid()
        return ButtonGrid()

if __name__ == '__main__' :
    MyApp().run()
