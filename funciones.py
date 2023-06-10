#Declaración de un metodo sin parametros

def sumar(n1,n2):
    #cuerpo del método
    print("este es el método sumar")
    sumar=n1+n2
    return sumar

def sumarp():
    #cuerpo del método
    seguir="s"
    suma=0
    contador=0
    while seguir=="s":
        numero=int(input("Digite un numero entero\n"))
        suma=suma+numero
        seguir=input("Si desea seguir digite s o cualquiera para salir\n").lower()
        contador=contador+1
    promedio=suma/contador
    return promedio

    
#Declaración de un metodo con parametros
def restar(n1,n2):  
    #cuerpo del método
    restar=n1-n2
    print(f"La resta entre el numero {n1} y el numero {n2} es :{restar}")
    
#Declaración método con valor de retorno    
def multiplicacion(n1,n2):  
    #cuerpo del método
    multiplicacion=n1*n2
    #Retorno del dato
    return multiplicacion

def division(n1,n2):  
    #cuerpo del método
    division=n1/n2
    print(f"La división entre el numero {n1} y el numero {n2} es :{division}")
suma=0
#Llamado o invocación del método
print("Menu opciones")

num1=int(input("Ingrese el numero 1\n"))
num2=int(input("Ingrese el numero 2\n"))

op=input("Ingrese la opción según la operación a realizar\n1. Suma\n2. Resta\n3. Multiplicación\n4. División\n5. Promedio\n6. Prom de muchos numeros\n")

if op=="1":
    #Invocar método suma
    sumar(num1,num2)
elif op=="2":
    #Invocar método con parametro
    restar(num1,num2)
elif op=="3":
    #Invocar metodo con valor de retorno
    #multiplicacion(num1,num2)
    #Directamente en una impresión
    print(f"La multiplicación entre {num1} y {num2} es {multiplicacion(num1,num2)}")
    
    #Guardar una variables para operarla en otro momento
    producto=multiplicacion(num1,num2)
    if producto<50:
        print("El producto es menor que 50")
    else:
        print("El prodcuto es mayor que 50")
elif op=="4":
    division(num1,num2)
elif op=="5":
    sumar(num1,num2) #Suma de los dos números
    promedio=sumar(num1,num2)/2
elif op=="6":
    print(f"El promedio es de {sumarp()}")
    #Se debe utilizar el metodo suma
else:
    print("Opción no valida")
    
