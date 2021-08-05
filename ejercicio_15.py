import numpy as np
import matplotlib.pyplot as plt

def maxs (v):
    """ Encuentra los maximos de un array 
    v: array a obtener maximos
    b: valor en posicion anterior
    x: valor en la posicion actual
    asc: booleano para determinar si asciende o desciende 
    """
    b = 0
    first = False
    asc = True
    mxs = []
    for x in v:
        if not first:
            b = x
            first = True
            if x < v[1]:
                asc = True
            else:
                asc = False
        else:
            if x - b < 0 and asc:
                asc = False
                mxs.append(b)
            elif x - b > 0 and not asc: 
                asc = True
        b = x
    return mxs
            

signal = np.random.randn(10)
print(signal)
print(maxs(signal))

maximos = maxs(signal)
max_graf = np.empty(len(signal))
max_indx = []

for i in maximos:
    index = np.where(signal == i)[0]
    max_indx.append(index[0])

for i in max_indx:
    max_graf[i] = signal[i]

plt.plot(signal, '-b', max_indx, maximos, '.r')
plt.show()