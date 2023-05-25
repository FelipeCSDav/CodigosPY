opc=0
opc2=0


CP=250000
ID=475000
OB=800000

TrAux=0.15
TrAdm=0.10
TrDoc=0.05

contcarillas=0
contimplante=0
contortodoncia=0

total=0

while opc!=3:
    opc2=0
    print("\nBienvenido a El Diente de Oro")
    print("")
    print("1) Realizar cotizacion")
    print("2) Reiniciar cotizacion   ")
    print("3) Salir")
    while True:
        try:
            opc=int(input("Ingrese la opcion: "))
            if 1<= opc <= 3:
                break
            else:
                print("La opcion no esta dentro del rango\n")
        except:
            print("Error de valor ingresado, intenta nuevamente\n")

    if opc == 1:
        while opc2!=4:
            

            print("\nLos tratamientos son\n")
            print(f"1) Carillas Porcelana = ${CP}")
            print(f"2) Implantes Dentales = ${ID}")
            print(f"3) Ortodoncia Brackets = ${OB}")  
            print("4) Terminar cotizacion")
            while True:
                try:
                    opc2=int(input("Ingresar eleccion: "))
                    if 1<= opc2<=4:
                        break
                    else:
                        print("La opcion no esta dentro del rango\n")
                except:
                    print("Error de valor ingresado, intenta nuevamente\n")
            
            if opc2==1:
                contcarillas+=1
                total+=CP
            elif opc2==2:
                contimplante+=1
                total+=ID
            elif opc2==3:
                contortodoncia+=1
                total+=OB

            if opc2==4:
                print("\nTipo de Trabajador\n")
                print("1) Trabajador Auxiliar")
                print("2) Trabajador Administrativo")
                print("3) Trabajador Docente")
                while True:
                    try:
                        tipo=int(input("Ingresar opcion: "))
                        if 1 <= tipo <=3:
                            break
                        else:
                            print("La opcion no esta dentro del rango\n")
                    except:
                        print("Error de valor ingresado, intenta nuevamente\n")
                
                
                
                if tipo==1:
                    totalfinal = total*(1-TrAux)
                elif tipo== 2:
                    totalfinal = total*(1-TrAdm)
                elif tipo== 3:
                    totalfinal = total*(1-TrDoc)
                
                print("Cotizacion")
                print("-"*50)
                if contcarillas>0:
                    print(f"{contcarillas} Tratamiento Carillas Porcelana ${CP*contcarillas}")
                if contimplante>0:
                    print(f"{contimplante} Implantes Dentales ${ID*contimplante}")
                if contortodoncia>0:
                    print(f"{contortodoncia} Ortodoncia de Brackets ${OB*contortodoncia}")
                print("-"*50)
                print(f"SubTotal: {total}")
                if tipo == 1:
                    print(f"Descuento aplicado {TrAux*100}%   ${round(total-totalfinal)}")
                elif tipo== 2:
                    print(f"Descuento aplicado {TrAdm*100}%   ${round(total-totalfinal)}")
                elif tipo== 3:
                    print(f"Descuento aplicado {TrDoc*100}%   ${round(total-totalfinal)}")
                print("-"*50)
                print(f"Total: ${round(totalfinal)}")
                print("-"*50)
                print(f"Son 12 cuotas de: ${round(totalfinal/12)}")
                print("")
                print("Sonria Bonito :)\n")
                
                
    if opc==2:
        print("Valores reiniciados")
        total=0
        contcarillas=0
        contimplante=0
        contortodoncia=0
                

    
