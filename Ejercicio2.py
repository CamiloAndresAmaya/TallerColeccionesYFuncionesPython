TipoGasolina=input("Cual es su tipo de gasolina : \ncorriente:10.800 \ndiesel=9.800 \n").lower()
ValorTanqueo=int(input("Digite el valor a tanquear\n"))

if TipoGasolina=="corriente":
    CantidadGaleones=ValorTanqueo/10800
else :
    CantidadGaleones=ValorTanqueo/9800

print("La cantidad de galeones que tanqueo es de ",CantidadGaleones)
