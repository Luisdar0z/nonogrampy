#ejemplo de ingreso de datos: 12 2 3 4 44, 123 3 32 2 323, 23 23
columna = input("ingrese columnas(solo separado por , sin espacio) \n")
col = columna.split(", ")
print(col)
print("imprimiendo posicion valor 2 posicion 1", col[1])
print(type(col[1][1]))

#ejemplo de ingreso de datos: 12 2 3 4 44, 123 3 32 2 323, 23 23
fila = input("ingrese filas (solo separado por , sin espacio)\n")
fil = fila.split(",")
print(fil)
print("imprimiento posicion 3", fil[1])