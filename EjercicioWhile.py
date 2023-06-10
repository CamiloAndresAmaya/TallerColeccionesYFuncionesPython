presupuesto=100000
Transporte=0
GastosTransporte=0
gastosProfe=0
SubidaDinero=0
ProfeGasto=0
Dinero=0
repetir="s"
while repetir=="s" or repetir=="S":
 ChoiseUser=int(input(f"Su presupuesto es de {presupuesto} escoga que opción va a usar \n 1. Si va a pagar transporte \n 2. Si va a gastarle algo a la cucha\n 3. Si Gano dinero\n"))
 if ChoiseUser==1:
     presupuesto=presupuesto-6000
     Transporte=Transporte+1
     GastosTransporte=GastosTransporte+6000
     print("USted Gasto 6000 de su presupuesto")

 elif ChoiseUser==2:
     presupuesto=presupuesto-10000
     ProfeGasto=ProfeGasto+1
     gastosProfe=GastosProfe=10000
     print("USted Gasto 10000 de su presupuesto")
 elif ChoiseUser==3:
     presupuesto=presupuesto+5000
     Dinero=Dinero+1
     SubidaDinero=SubidaDinero+5000
     print("USted Ganó 5000, se añadio a su presupuesto")
 else:
     print("Esa no es una opción valida")

 print("el dinero q le sobro es",presupuesto,"\n")
 repetir=input("Si desea continuar digitando s, o n para salir\n")

print("los gastos acumulados del transporte fueron de",GastosTransporte," los gastos acumulados hacia la profe fueron de ",gastosProfe," y el dinero acumulado fue de ",SubidaDinero)
print("Las veces que repitió cada opción: \n 1.Transporte: ",Transporte," \n 2.Gastos Hacia La Profe: ",ProfeGasto," \n 3.Subida De Dinero: ",Dinero)