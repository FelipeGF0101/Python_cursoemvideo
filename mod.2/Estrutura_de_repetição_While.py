"""
Exemplo:

c  = 1
while c < 10:
    print(c)
    c = c + 1
print('Fim')
==================
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('Fim')
==================
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('Fim')

=================

n = 1
while n != 0:
    n = int(input('DIgite um valor: '))
"""
n = 1
par = 0
impar = 0

while n != 0:
    n = int(input('DIgite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print(f'Você digitou {par} números pares e {impar} números ímpares!')
