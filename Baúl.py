baul=[]
repetir="s"
repetirarticulo="s"

while repetir=="s" or repetir=="S":
    selección=input("Digite que opción desea hacer: \n1. Agregar un artículo al baúl a voluntad(se agregara al final de la lista)\n2. listar altículos del baúl de forma ascendente\n3. Borrar el último elemento de la lista\n4. Borrar un artículo del bául, debe mostrarlos con su index y permitir escoger a un usuario cual desea borar\n")
    if selección=="1":    
        while repetirarticulo=="s" or repetirarticulo=="S":
         baul.append(input("Digite el artículo que desea agregar\n"))
         repetirarticulo=input("digite s si desea agregar mas artículos o n para salir\n")
    elif selección=="2":
        if len(baul)==0:
            print("El baúl esta vacío")
        else:
            baul.sort()
            print("Usted acaba de listar los articulos de forma ascendente\n")
            for i,e in enumerate(baul):
                print("en la posición",i,"se encuentra el elemento",e,"\n")
    elif selección=="3":
        borrarArticulo=baul.pop()
        print("Usted borró el ultimo articulo del baul el cual era ",borrarArticulo,"\n")
    elif selección=="4":
        for i,e in enumerate(baul):
            print("en la posición",i,"se encuentra el elemento",e,"\n")
        borrarSelección=input("Digite el elemento que desea borrar del\n").lower()
        baul.remove(borrarSelección)
        print("Usted borró el elemento",borrarSelección,"\n la lista quedó de la siguiente manera\n")
        for i,e in enumerate(baul):
            print("en la posición",i,"se encuentra el elemento",e,"\n")
        