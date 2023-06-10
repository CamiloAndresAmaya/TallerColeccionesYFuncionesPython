onces=["combo hamburguesa","sandwich","Pizza"]
onces.append("gaseosa")
onces.extend(["malteada","perro caliente"])
onces.sort()
print(onces)
onces.insert(2,"empanada")

onces.reverse()
print(onces)

print(onces.index("gaseosa"))