#Definición o delaración de la lista
numeros=[1,2,3,4]
#Mostrar contenido 
print(numeros)
#Mostrar posición particular
print(numeros[2])
#Mostrar última posición
print(numeros[-1])
#cambiar valor de una posición
numeros[1]=9
print (numeros)

#Recorrer lista
for p in numeros:
    print(p)
#Recorrer posición por posición y elemento
for i,e in enumerate(numeros):
    print(i,e)

#Iterar dos listas al mismo tiempo
generos=["Jazz","Salsa","Rock"]

for l1,l2 in zip(numeros,generos):
    print(l1,l2)

#Longitud lista
print(len(generos))

comidas=[]