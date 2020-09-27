#coding: utf-8
'''entrada de texto com kivy'''

from kivy.app import App
from kivy.uix.textinput import TextInput

def build():
    return TextInput(text="Componente TextInput")

janela = App()
janela.build = build
janela.run()
