from random import randint
números = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f'Os números sorteados foram: {números[0]} {números[1]} {números[2]} {números[3]} {números[4]}')
x = sorted(números)
print(f'O maior valor foi {x[-1]}\nO menor valor foi {x[0]}')
