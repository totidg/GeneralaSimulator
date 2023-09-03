def escalera(tupla):
    tupla_ordenada = sorted(tupla)
    i = 0
    if tupla_ordenada[0] == 1 or tupla_ordenada[0] == 2:
        while i < len(tupla) and tupla.count(tupla[i]) == 1:
            i+=1
    return len(tupla) == i

def generala(tupla):
    i=0
    while i < len(tupla) and  tupla.count(tupla[i]) != 5:
        i+=1
    return len(tupla) != i

def poker(tupla):
    i=0
    while i < len(tupla) and tupla.count(tupla[i]) != 4:
        i+=1
    return len(tupla) != i

def full(tupla):
    i=0     
    while i < len(tupla) and (tupla.count(tupla[i]) == 2 or tupla.count(tupla[i]) == 3):
        i+=1
    return len(tupla) == i

def porcentaje(cantidad,total):
    return cantidad / total * 100

def simulador():   
    contador_escalera = 0
    contador_generala = 0
    contador_poker = 0
    contador_full = 0
    contador_ninguno = 0
    contador_tiradas = 0

    import random
    for i in range(1000):
        tirada = random.choices([1, 2, 3, 4, 5, 6], k=5)
        contador_tiradas += 1

        if escalera(tirada):
            contador_escalera += 1
        elif generala(tirada):
            contador_generala += 1
        elif poker(tirada):
            contador_poker += 1
        elif full(tirada):
            contador_full += 1
        else:
            contador_ninguno += 1

    porcentaje_escalera = porcentaje(contador_escalera , contador_tiradas)
    porcentaje_generala = porcentaje(contador_generala , contador_tiradas)
    porcentaje_poker = porcentaje(contador_poker , contador_tiradas)
    porcentaje_full = porcentaje(contador_full , contador_tiradas)
    porcentaje_ninguno = porcentaje(contador_ninguno , contador_tiradas)
    
    print('Total de tiradas:', contador_tiradas)
    print('Escaleras:', contador_escalera,'(',porcentaje_escalera,'% )')
    print('Generalas:', contador_generala,'(',porcentaje_generala,'% )')
    print('Poker:', contador_poker,'(',porcentaje_poker,'% )')
    print('Full:', contador_full,'(',porcentaje_full,'% )')
    print('Ningún Juego:', contador_ninguno,'(',porcentaje_ninguno,'% )')

simulador()


















    
