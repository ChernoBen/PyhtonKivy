#coding: utf-8

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

def click():
    print(ed.text)

'''definindo componentes de tela na função build'''
def build():

    '''instanciando gerenciador de layout'''
    layout = FloatLayout()
    # Definir essa variavel global é uma péssima prática
    global ed
    '''criando componente entrada de texto e botão'''
    ed = TextInput(text = "Entrada de dados Kivy")

    # resetando dimensões do componente
    ed.size_hint = None,None
    # definindo dimensão do widget
    ed.height = 300
    ed.width = 400
    #distancia do topo
    ed.y = 250
    # distancia da lateral
    ed.x = 60

    bt = Button(text="click me")
    bt.size_hint = None,None
    bt.width = 200
    bt.heigth = 50
    bt.y = 250
    bt.x = 300
    #definindo evento do botão
    bt.on_press = click

    '''adicionando widgets ao leyout'''
    layout.add_widget(ed)
    layout.add_widget(bt)

    return layout

janela = App()
#alterando titulo da janela
janela.title = "Anaconda Kivy"
'''alterando dimensão da janela'''
from kivy.core.window import Window

Window.size = 1024,800

janela.build = build
janela.run()