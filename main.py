import kivy
kivy.require('1.7.2')
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
#setup graphics
from kivy.config import Config
Config.set('graphics','resizable',0)
#Graphics fix
from kivy.core.window import Window;
Window.clearcolor = (0,0,0,1.)
#Window.clearcolor = (1,0,0,1.)

class GUI(Widget):
    #this is the main widget that contains the game
    def __init__(self, **kwargs):
        super(GUI, self).__init__(**kwargs)
        l = Label(text='Not Your first Kivy App!') 
        l.x = Window.width/2 - l.width/2
        l.y = Window.height/2
        self.add_widget(l)   

class ClientApp(App):
    def build(self):
        #this is where the root widget goes
        #should be a canvas
        app = GUI()
        return app    
if __name__ == '__main__' :
    ClientApp().run()
