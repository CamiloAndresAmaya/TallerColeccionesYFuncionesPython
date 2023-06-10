persona = {
    "firstname": "Andres",
    "lastname":"Castaneda",
    "age": 18,
    "id": 1234567890,
    "state": True
}
#Muestra contenido integro
print(persona)
#Muestra el valor de un key en particular
print(persona["firstname"])
#Muestra el valor de un key en particular con metodo get
print(persona.get("lastname"))

#Acceder a un elemento para modificarlo a través del key
persona["firstname"]= "Lorenzo"
print(persona["firstname"])
#Agregar una nueva key con su valor
persona["title"]="Ingeniero De Sistemas"
print(persona)
#Acceder a un elemento
persona.update({"firstname":"Neider Huberty"})
print(persona)

persona.pop("title")
print(persona)

del persona["firstname"]
#Muestra los key del diccionario
for k in persona:
    print(k)
#Muestra los value del dicionario
for h in persona:
    print(persona[h])
for a,b in persona.items():
    print(a, " = ",b)