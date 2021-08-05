ndup = int(input('Ingrese el número de druplos: '))
nann = int(input('Ingrese el número de años: '))

def druplos(ndup, nann):
    if ndup > 0:
        if ndup == 1:
            ndup = 2
            nann = nann - 1
    
        ndup_act = ndup

        for i in range(nann):
            ndup_act = ndup_act**2
    
        return ndup_act

    else:
        print('¡Es un numero negativo o cero!')


#if __name__ == '__main__':


drup =  druplos(ndup,nann)
print('En el ultimo año hay un total de {} Druplos'.format(drup))       
