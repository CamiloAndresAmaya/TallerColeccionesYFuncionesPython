onces=["Combo hamburguesa","Sandwich","Pizza"]
onces.append("gaseosa")
onces.extend(["Malteada","Perro caliente"])
print(onces)
print("En este momento la lista tiene ",len(onces),"elementos")
for i,e in enumerate(onces):
    print(i,e)

onces.insert(2,"empanada")

for i,e in enumerate(onces):
    print(i,e)
#remover posición escrita
onces.remove("gaseosa")
#con del remueve una posición en numero
del onces[4]
#remueve ultima posición
onces.pop()

print(onces)

#Ordenar ascendentemente una lista
onces.sort()
#Ordenar descendentemente
onces.reverse()

