#!usr/bin/env python
'''
Y(t) = (Xt
      Zt)
F(T,Y) = (alfa*X - beta*X*Z
          -gama*Z + rhond*X*Z)
1ªderivada de Y = F
alfa => taxa crescimento presa
gama => taxa mortalidade predador
Xt => presa
Zt => cacador
ciclo => considerando passagem verao, outono, inverno, primavera
deltaT = 1 mes considerando que um ciclo = 12 meses ou seja cada estacao teria 3 meses
'''

from euler.py import euler_simple

def hunter_prey(deltaT, alfa, gama, beta, rhond, Zinitial, Xinitial, cicles):
	
	return (Zactual, Xactual)

def calculate_prey(alfa, beta, Xinitial, Zintial, deltaT):
	function_prey = "alfa*X-beta*X*Z"
	return euler_simple(deltaT, Xinitial, function_prey)

def calculate_hunter(gama, rhond, Xinitial, Zintial, deltaT):
	function_hunter = "-gama*Z+rhond*X*Z"
	return euler_simple(deltaT, )