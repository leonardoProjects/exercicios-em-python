"""
EXERCÍCIO 047: Contagem de Pares
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""

for x in range(1,51):
    if x % 2 == 0:
        print(x, end=' ')
