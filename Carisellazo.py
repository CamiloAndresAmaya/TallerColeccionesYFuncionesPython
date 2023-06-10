import random

seguir="s"
ValorGlobal=500

def LanzarMoneda():
    nombreJugador=input("Digite Su Nombre Para Iniciar El Juego\n")
    numero= random.randint(1, 2)
    return (numero,nombreJugador)
   

def jugar():
    numero,nombreJugador=LanzarMoneda()
    Seleccion=int(input("Digite \n1. Cara\n2. Sello\n"))
    Apuesta=int(input(f"Digite cuanto dinero va a apostar {nombreJugador}, su dinero actual es de {ValorGlobal} \n"))
    if Seleccion==1:
        print("Usted Selecciono la Opción Cara...")
    elif Seleccion==2:
        print("Usted Selecciono La Opción Sello")
    else:
        print("Opción no valida")

    if numero==1 and Seleccion==1 and Apuesta<=ValorGlobal:
        print("Salió Cara, usted escogió cara, Ganaste!...")
        ganar(ValorGlobal,Apuesta)
    elif numero==1 and Seleccion==2 and Apuesta<=ValorGlobal:
        print("Salió Cara, usted escogió Sello, Perdiste!...")
        perder(ValorGlobal,Apuesta)
    elif numero==2 and Seleccion==2 and Apuesta<=ValorGlobal:
        print("Salió Sello, usted escogió Sello, Ganaste!...")
        ganar(ValorGlobal,Apuesta)
    elif numero==2 and Seleccion==1 and Apuesta<=ValorGlobal:
        print("Salió Sello, usted escogió Cara, Perdiste!...")
        perder(ValorGlobal,Apuesta)
    elif numero!=1 or Seleccion!=2 and Apuesta<=ValorGlobal:
        print("Digitaste una opción incorrecta")
    else:
        print("Datos Incorrectos o dinero insuficiente")
    
    return (Seleccion, Apuesta)
    
def ganar(ValorGlobal,Apuesta):
    ValorGlobal=ValorGlobal+Apuesta
    print(f"El Valor Global Está En {ValorGlobal} mil pesos")
        
def perder(ValorGlobal,Apuesta):
    ValorGlobal=ValorGlobal-Apuesta
    print(f"El Valor Global Está En {ValorGlobal} mil pesos")
        
while seguir=="s":
    print("\2=============================\2")
    print("Bienvenido al juego carisellazo")
    print("\2=============================\2")
    jugar()
    seguir=input("Digite s para seguir jugando o cualquier tecla para salir\n")



