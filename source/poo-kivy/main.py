#coding: utf8

from kivy.app import App
from kivy.uix.label import Label

'''implementação de forma orientada a objetos'''
class MeuPrograma(App):
    def build(self):
        return Label()


MeuPrograma().run()