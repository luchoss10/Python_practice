"""
Ejercicio 07

Calcula el numero de digitos del numero entero Ingresado

"""

def num_digitos(num):
    if num < 0:
        num = num*(-1)
    
    i = 0

    while num >= 10**i:
        i +=1
    
    return(i)

#if __name__ == '__main__':

i = num_digitos(int(input('Ingrese un numero entero: ')))

print('El numero de digitos es: {}'.format(i))   
