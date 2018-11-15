#Alexys Martín Coate Reyes
#Descripción:


def extraerPares(lista):
    copiaLista = lista[:]
    for valor in lista:
        if valor%2 != 0:
            copiaLista.remove(valor)

    return copiaLista


def extraerMayoresPrevio(lista):
    copiaLista = lista[:]
    indiceMenor = -1
    for valor in lista:
        if indiceMenor == -1:
            copiaLista.remove(valor)
            indiceMenor += 1
        elif indiceMenor >= 0:
            if lista[indiceMenor] > valor:
                copiaLista.remove(valor)
            indiceMenor += 1

    return copiaLista


def intercambiarParejas(lista):
    nuevaLista = []
    impares = 1
    pares = 0
    for x in range(0, len(lista)//2):
        nuevaLista.append(lista[impares])
        nuevaLista.append(lista[pares])
        if impares < len(lista) or pares < len(lista):
            impares += 2
            pares += 2
    if len(lista)%2 != 0:
        nuevaLista.append(lista[-1])

    return nuevaLista


def intercambiarMM(lista):
    copiaLista = lista[:]
    if len(lista) > 0:
        copiaLista[lista.index(min(lista))] = max(lista)
        copiaLista[lista.index(max(lista))] = min(lista)

    lista = copiaLista
    return lista

def promediarCentro(lista):
    copiaLista = lista[:]
    promedioCentro = 0
    if len(lista) > 0:
        copiaLista.remove(min(lista))
        copiaLista.remove(max(lista))
        if len(copiaLista) != 0:
            promedioCentro = int(sum(copiaLista)/len(copiaLista))

    return promedioCentro


def calcularEstadistica(lista):
    listaDesviacion = []
    promedio = 0
    if len(lista) != 0:
        promedio = sum(lista)/len(lista)
        for x in lista:
            sumaDesviacion = (x-promedio)**2
            listaDesviacion.append(sumaDesviacion)
    desviacion = ((sum(listaDesviacion))/(len(lista)-1))**.5
    resultado = (promedio, desviacion)

    return resultado


def calcularSuma(lista):
    copiaLista = lista[:]
    eliminar = []
    for valor in lista:
        if valor == 13:
            if len(lista) == 1:
                copiaLista = []
            if len(lista) == 2:
                copiaLista.pop(lista.index(valor)-1)
                copiaLista.pop(lista.index(valor)-1)
            elif len(lista) > 2:
                eliminar.append(lista[lista.index(valor)])
                eliminar.append(lista[lista.index(valor)+1])
                eliminar.append(lista[lista.index(valor)-1])

    for dato in eliminar:
        if dato in copiaLista:
            copiaLista.remove(dato)

    suma = sum(copiaLista)

    return suma


def main():
    lista0 = []
    lista = [1,2,3,2,4,60,5,8,3,22,44,55]
    lista2 = [3, 5, 7]
    lista3 = [5,4,3,2]
    lista4 = [1,2,3]
    lista5 = [7]
    lista6 = [5,9,3,22,19,31,10,7]

    lista7 = [70,80,90]
    lista8 = [95,21,73,24,15,69,71,80,49,100,85]
    lista9 = [20,55,30,5,55,5]
    lista10 = [5,9,1,8]
    lista11 = [5,8]

    lista12 = [1,2,3,4,5,6]

    lista13 = [5,2,13,4,1,6,1,8,4,1,5]
    lista14 = [5,2,13,4,1,6,1,8,4,13,1]
    lista15 = [13,49]

    print("""Probelma 1. Regresa una lista con los valores pares de la lista original.
    Con la lista {}, regresa {}
    Con la lista {}, rergesa {}
    Con la lista {}, rergesa {}
    """.format(lista, extraerPares(lista), lista2, extraerPares(lista2), lista0, extraerPares(lista0)))

    print("""Probelma 2. Regresa una lista con los valores que son mayores  un elemento previo.
        Con la lista {}, regresa {}
        Con la lista {}, rergesa {}
        Con la lista {}, rergesa {}
        """.format(lista, extraerMayoresPrevio(lista), lista3, extraerMayoresPrevio(lista3), lista0, extraerMayoresPrevio(lista0)))

    print("""Probelma 3. Regresa una nuevalista con las parejas intercambiadas.
        Con la lista {}, regresa {}
        Con la lista {}, rergesa {}
        Con la lista {}, rergesa {}
        Con la lista {}, rergesa {}
        """.format(lista, intercambiarParejas(lista), lista4, intercambiarParejas(lista4),lista5, intercambiarParejas(lista5), lista0, intercambiarParejas(lista0)))

    print("""Probelma 4. Intercambia el menor y el mayor número de una lista.
        Con la lista {}, regresa {}
        Con la lista {}, rergesa {}
        Con la lista {}, rergesa {}
        """.format(lista6, intercambiarMM(lista6), lista4, intercambiarMM(lista4), lista0, intercambiarMM(lista0)))

    print("""Probelma 5. Regresa el promedio 'centro' de los valores
           Con la lista {} el promedio centro es: {}
           Con la lista {} el promedio centro es: {}
           Con la lista {} el promedio centro es: {}
           Con la lista {} el promedio centro es: {}
           Con la lista {} el promedio centro es: {}
           """.format(lista7, promediarCentro(lista7), lista8, promediarCentro(lista8), lista9,
                      promediarCentro(lista9), lista10, promediarCentro(lista10), lista11, promediarCentro(lista11)))

    print("""Probelma 6. Intercambia el menor y el mayor número de una lista.
           Con la lista {}, la media y la desviación estandar son: {}
           Con la lista {}, la media y la desviación estandar son: {}
           Con la lista {}, la media y la desviación estandar son: {}
           """.format(lista12, calcularEstadistica(lista12), lista8, calcularEstadistica(lista8), lista0, calcularEstadistica(lista0)))

    print("""Probelma 7. Calcula la suma de números a exepción de los que estén al lado de un 13.
              Con la lista {}, la suma es: {}
              Con la lista {}, la suma es: {}
              Con la lista {}, la suma es: {}
              Con la lista {}, la suma es: {}
              Con la lista {}, la suma es: {}
              """.format(lista12, calcularSuma(lista12), lista13, calcularSuma(lista13), lista14,
                         calcularSuma(lista14), lista15, calcularSuma(lista15), lista0, calcularSuma(lista0)))


main()