#coding: utf-8

from kivy.app import App
from kivy.uix.label import Label

N = 32  # dimensao do tabuleiro
linha = [False] * N
diagAsc = [False] * (2 * N - 1)
diagDesc = [False] * (2 * N - 1)
numSol = 0
solucao = [0] * N


def rainha(col):
    gabarito = []
    if col < N:
        for lin in range(N):
            if linha[lin] or diagAsc[lin + col] or diagDesc[lin - col + N - 1]:
                continue
            solucao[col] = lin
            linha[lin] = diagAsc[lin + col] = diagDesc[lin - col + N - 1] = True
            rainha(col + 1)
            linha[lin] = diagAsc[lin + col] = diagDesc[lin - col + N - 1] = False
    else:
        gabarito.append(solucao)
        print(solucao)
        global numSol
        numSol = numSol + 1
        if len(gabarito) == numSol - 1:
            return gabarito


sol = rainha(0)
print("Num.Solucoes= ", numSol)

def build():
    lb = Label()
    lb.text = "Primeiros passos com kivy"
    lb.italic = True
    lb.font_size = 50
    return lb

app = App()
app.build = build


app.run()