import random
import math
def uniforme_discreta(a,b):
    return int(a + (b+1-a)*random.random())

def bernoulli(p,v1,v2):
    if random.random() < p:
        return v1
    return v2

def Triangular(valor_min,valor_maxim,valor_probable):
    if 0 <= random.random() < (valor_probable-valor_min)/(valor_maxim-valor_min):
        return valor_min+math.sqrt((valor_maxim-valor_min)*(valor_probable-valor_min)*random.random())
    else:
        return valor_maxim-math.sqrt((valor_maxim-valor_min)*(valor_maxim-valor_probable)*(1-random.random()))
    
def exponencial(a):
    return -(1/a)*math.log(random.random())
def uniforme_continua(a,b):
    return a + (b-a)*random.random()
