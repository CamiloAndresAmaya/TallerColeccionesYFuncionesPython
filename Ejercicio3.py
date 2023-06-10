repetir="s"

while repetir=="s" or repetir=="S":

    SubidaSITP=input("Se subio al sitp? \nsi\nno\n")
    if SubidaSITP=="si":
        TipoTarjeta=input("Digite su tipo de tarjeta \nPersonalizada \nNormal\n").lower()
        SaldoTarjeta=int(input("Digite su saldo\n"))
        CantidadPasajes=int(input("Digite cuantos pasajes va a pagar\n"))
        PrecioPasaje=2900
        CantidadPasajesAcumulable=PrecioPasaje*CantidadPasajes
        SaldoTarjeta=SaldoTarjeta-CantidadPasajesAcumulable
        if TipoTarjeta=="personalizada":
            if SaldoTarjeta<PrecioPasaje and CantidadPasajes==1:
                print("Recargué la tarjeta antes de la siguiente subida",SaldoTarjeta)
            elif SaldoTarjeta>=0:
                print("Gracias..., su saldo actual es",SaldoTarjeta)
            elif SaldoTarjeta<0:
                print("Saldo insuficiente...")
            elif TipoTarjeta=="normal":
                if SaldoTarjeta<0:
                    print("Saldo Insuficiente, su saldo actual es ",SaldoTarjeta)
                elif SaldoTarjeta>=0:
                    print("Gracias..., su saldo actual es",SaldoTarjeta)
            else:
                print("Ese no es un tipo de tarjeta existente")
    else:
        print("Vayase a pie")
    repetir=input("Si va a hacer transbordo presione s, o n para salir\n")


        


