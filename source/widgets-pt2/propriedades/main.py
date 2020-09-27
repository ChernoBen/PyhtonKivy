from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

'''classe que contém o gerenciador de layout'''
class RootWidget(FloatLayout):
    pass

'''classe da aplicação'''
class MedidaApp(App):
    def build(self):
        return RootWidget()


MedidaApp().run()