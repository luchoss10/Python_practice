"""
Ejercicio 13

Calcula el factor primo del valor indicado

"""

num = int(float(input('Ingrese su número para la descomposición: ')))

def descomponer(n):

    primos=[]

    for i in range(2, n+1):
        while n % i == 0:
            primos.append(i)
            n = n/i
    return primos

#if __name__ == '__main__':

print(descomponer(num))
