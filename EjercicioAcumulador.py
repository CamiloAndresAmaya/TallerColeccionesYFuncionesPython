presupuesto=100000
Inicio = int(input("Escoga el numero en que inicia el ciclo"))
Fin= int(input("Escoga el numero en que termina el ciclo"))
Transporte=0
ProfeGasto=0
Dinero=0
for i in range(Inicio,Fin):
 ChoiseUser=int(input(f"Su presupuesto es de {presupuesto} escoga que opción va a usar \n 1. Si va a pagar transporte \n 2. Si va a gastarle algo a la cucha\n 3. Si Gano dinero\n"))
 if ChoiseUser==1:
     presupuesto=presupuesto-6000
     Transporte=Transporte+1
     print("USted Gasto 6000 de su presupuesto")
 elif ChoiseUser==2:
     presupuesto=presupuesto-10000
     ProfeGasto=ProfeGasto+1
     print("USted Gasto 10000 de su presupuesto")
 elif ChoiseUser==3:
     presupuesto=presupuesto+5000
     print("USted Ganó 5000, se añadio a su presupuesto")
 else:
     print("Esa no es una opción valida")

 print("el dinero q le sobro es",presupuesto,"\n")
