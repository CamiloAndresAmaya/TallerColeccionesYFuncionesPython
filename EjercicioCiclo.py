numero=int(input("ingrese un numero del 1 al 10\n"))

for f in range(1,11):
    print(f'{numero} x {f} = {numero*f}')
print("Tabla alrevés")
for f in range(10,0,-1):
    print(f'{numero} x {f} =  {numero * f}')