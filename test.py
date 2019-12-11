"""
F = int(input("Numero de filas:\n"))
C = int(input("Numero de Columnas:\n"))
"""


#ejemplo de ingreso de datos: 12 2 3 4 44, 123 3 32 2 323, 23 23
columna = input("ingrese columnas(solo separado por , sin espacio) \nR: ")
col = columna.split(", ")
print(col)
#print("imprimiendo posicion valor 2 posicion 1: ", col[1])
#print(type(col[1][1]))

#ejemplo de ingreso de datos: 12 2 3 4 44, 123 3 32 2 323, 23 23
fila = input("\ningrese filas (solo separado por , sin espacio)\nR: ")
fil = fila.split(", ")
print(fil)
#print("imprimiento posicion 3", fil[1])


i = 0
acol = []
ecol = []
icol = []

while i < len(col):
    #creamos una lista de listas llamada "acol" con los datos de "col"
    acol.append(col[i].split(" "))
    #print("+acol: ", acol[i])
    #convertimos a enteros los elementos de una lista de "acol" y los pasamos a la lista "icol"
    for j in acol[i]:
       icol.append(int(j)) 
       #print("-icol: ", icol)
    #pasamos la lista "icol" como un elemento de la lista "ecol" y reiniciamos la lista "icol"
    ecol.append(icol)
    icol = []
    #print("•ecol: ", ecol)
    i += 1

print("\nValor columnas: ")
print(ecol)

i = 0
afil = []
efil = []
ifil = []

while i < len(fil):
    #creamos una lista de listas llamada "afil" con los datos de "fil"
    afil.append(fil[i].split(" "))
    #print("+afil: ", afil[i])
    #convertimos a enteros los elementos de una lista de "afil" y los pasamos a la lista "ifil"
    for h in afil[i]:
       ifil.append(int(h)) 
       #print("-ifil: ", ifil)
    #pasamos la lista "ifil" como un elemento de la lista "efil" y reiniciamos la lista "ifil"
    efil.append(ifil)
    ifil = []
    #print("•efil: ", efil)
    i += 1

print("\nValor filas: ")
print(efil)


"""

print('\n')
print('   1 1 1 ')
print(' 3 1 1 1 1')
print(' 1 1 1 1 3')
print('╔═╦═╦═╦═╦═╗')
print('║■║■║■║■║■║ 5')
print('╠═╬═╬═╬═╬═╣')
print('║■║ ║ ║ ║ ║ 1')
print('╠═╬═╬═╬═╬═╣')
print('║■║■║■║■║■║ 5')
print('╠═╬═╬═╬═╬═╣')
print('║ ║ ║ ║ ║■║ 1')
print('╠═╬═╬═╬═╬═╣')
print('║■║■║■║■║■║ 5')
print('╚═╩═╩═╩═╩═╝')
"""