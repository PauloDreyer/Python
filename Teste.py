
# -*- coding: utf-8 -*-

def soma( p1,  p2 ):
  x = int(p1) 
  y = int(p2)
  return x + y

print("Informe o valor para a variável X")
x = input()
print("O valor de X é:" + x)
print("Informe o valor para a variável Y")
y = input()
print("O valor de Y é:" + y)
print("soma de X + Y é:" + soma(x, y))
