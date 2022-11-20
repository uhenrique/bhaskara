import math
import time

def solve(a, b, c):
    """Resolve equações do segundo grau"""
    if b**2 - 4*a*c < 0:
        print('Não há soluções reais.')
        return None, None

    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

    return x1, x2

confirm = 'S'

while confirm == 'S':
    a = float(input('Digite o coeficiente a: '))
    b = float(input('Digite o coeficiente b: '))
    c = float(input('Digite o coeficiente c: '))

    x1, x2 = solve(a, b, c)

    print(f'Solução 1: {x1}')
    print(f'Solução 2: {x2}')
    
    time.sleep(2)
    confirm = input('Quer continuar? [S/N] ').upper()
    
print('Encerrando...')
time.sleep(1)