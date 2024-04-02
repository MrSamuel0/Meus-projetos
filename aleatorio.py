# algorítmo 1
"""

mas = float(input('Digite a sua massa corporal (em quilogramas): '))
alt = float(input('Digite a sua altura (metros): '))

imc = mas / alt ** 2

#

print(f'o seu indíce de massa corporal é: {imc: .1f}')

n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))

media = (n1 + n2) / 2

#

print(f'sua media é: {media: .1f}')

bar = float(input('Tamanho da barra (em cm): '))

inch = bar / 2.54
ft = bar / 30.48

print(f'o tamanho da barra em cm é: {bar: .2f}, em polegadas: {inch: .2f} e em pés: {ft: .0f}')

#

mon = float(input('Insira o montante em reais:  '))

dol = mon / 5.06
lb = mon / 6.34
eur = mon / 5.43

print(f'O montante em reais representa: {dol: .2f}$, {lb: .2f}£ e {eur: .2f}€.')

"""

import math

b = int(input('Insira o valor de b: '))
c = int(input('insira o valor de c: '))

hip = float(math.sqrt((b ** 2) + (c ** 2)))

print(f'O valor da hipotenusa é: {hip: .3f}')