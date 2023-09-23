import math as m

ang = float(input('Digite angulo em graus: '))
rang = ang * 3.14 / 180
if((rang > 3.14/2 and rang <= 3.14) or (rang > 3 * 3.14/2 and  rang <=2*3.14)):
    print(f'Seno: {m.sin(rang):.2f}')
else:
    print(f'Co-seno: {m.cos(rang):.2f}')
