class Nodo(object):
    info, sig = None, None

aux = Nodo()
aux.info= "primer nodo"  # info = "primer nodo"
palabra = input("Ingrese una palabra: ")
naux = aux # naux.info = primer nodo, una copia de aux

print("la" , aux.info)

while(palabra != ""):# si 'palabra' no es vacio se procesa los siguientes funciones
    nodo = Nodo() # la clase nodo lo coresponde variable 'nodo'
    print(nodo)   #esta "info y sig None"
    nodo.info = palabra # info almacena la informacion de palabra y sustituye el informacion anterior
    print(nodo.info)
    print(nodo)
    naux.sig = nodo
    print(naux.sig)
    naux = nodo
    print(naux)
    palabra = input("Ingrese una palabra: ")

while (aux is not None):# procesa hasta encontrar aux = ' None '
    print(aux.info) # aux.info = "primer nodo"
    aux = aux.sig # aux = aux.sig = None, sale de while 