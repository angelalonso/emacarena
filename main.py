import kivy
kivy.require('1.7.2')
from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
#setup graphics
from kivy.config import Config
Config.set('graphics','resizable',0)
#Graphics fix
from kivy.core.window import Window;
Window.clearcolor = (0,0,0,1.)
#Window.clearcolor = (1,0,0,1.)


Builder.load_string('''
<SimpleButton>:
    on_press: self.fire_popup()
<SimplePopup>:
    id:pop
    size_hint: .4, .4
    auto_dismiss: False
    title: 'Aaaaargh!!'
    Button:
        text: 'Dismiss'
        on_press: pop.dismiss()
''')

class SimplePopup(Popup):
    pass

class MainGrid(AnchorLayout):
    def __init__(self, **kwargs):
        super(MainGrid, self).__init__(**kwargs)
        self.anchor_x = 'center'
        self.anchor_y = 'center'

        self.submit = Button(text="eMac Arena", font_size=40, size_hint = (0.3, 0.3))
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
        #self.sound = SoundLoader.load('sounds/eMacArena.wav')
        #self.sound.seek(0)


    def pressed(self, instance):
        print("Aaaaargh!!")
        #self.play_audio()
        self.sound = SoundLoader.load('sounds/eMacArena.wav')
        if self.sound:
            print("Sound found at %s" % self.sound.source)
            print("Sound is %.3f seconds" % self.sound.length)
            self.sound.play()


    def play_audio(self):
        if self.sound:
            print("Sound found at %s" % self.sound.source)
            print("Sound is %.3f seconds" % self.sound.length)
            self.sound.play()

class MyApp(App):
    def build(self):
        return MainGrid()

if __name__ == '__main__' :
    MyApp().run()
