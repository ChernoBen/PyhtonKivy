#coding: utf-8

from kivy.app import App
from kivy.uix.label import Label


def build():
    return Label(text = "Curso Python e Kivy",italic = True,font_size=50)

app = App()
app.build = build


app.run()