
# inicio = 2
# final = 15
def lista_de_primos(inicio, final):
    mis_primos=[]
    if inicio <= 2: #El dos lo quito por defecto
        inicio = 3
    for numero in range(inicio, final + 1):
        es_primo= True
        for numero_a_comprobar in range(2,numero):
            if numero % numero_a_comprobar == 0:
                es_primo = False
                break
        if es_primo: #este if debe ir fuera del for que recorre la lista
            mis_primos.append(numero)
    return mis_primos


print(lista_de_primos(1,510))