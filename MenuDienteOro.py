menu1=0
menu2=0
total=0
#Costos de Tratamientos
Val_Car=250000
Val_Imp=475000
Val_Ort=800000
#Descuentos de Trabajadores 
TrAux=0.15
TrAdm=0.10
TrDoc=0.05
#Contadores de Tratamientos
ContCar=0
ContImp=0
ContOrt=0

#Menu 1
while menu1!=3:
    menu2=0
    print("-"*35)
    print("    Bienvenido a El Diente de Oro\n")
    print("1) Realizar cotizacion")
    print("2) Reiniciar valores de cotizacion")
    print("3) Cerrar cotizacion")
    print("-"*35)
    while True:
        try:
            menu1=int(input("Ingrese una opcion: "))
            if 1<=menu1<=3:
                break
            else:
                print("La opcion no esta dentro del rango\n")
        except:
            print("Error de valor ingresado, intenta nuevamente.\n")
#Menu 2
    if menu1==1:
        while menu2!=4:
            print("-"*35)
            print("      Tratamientos Dentales\n")
            print(f"1) Carillas Porcelana   =  ${Val_Car}")
            print(f"2) Implantes Dentales   =  ${Val_Imp}")
            print(f"3) Ortodoncia Brackets  =  ${Val_Ort}")  
            print("4) Terminar cotizacion")
            print("-"*35)
            while True:
                try:
                    menu2=int(input("Ingresar tratamientos a comprar: "))
                    if 1<=menu2<=4:
                        break
                    else:
                        print("La opcion no esta dentro del rango\n")
                except:
                    print("Error de valor ingresado, intenta nuevamente.\n")
            if 1<=menu2<=3:
                while True:
                    try:
                        cantidad=int(input("¿Cuantos desea cotizar?: "))
                        if cantidad>=0:
                            break
                        else:
                            print("La cantidad debe ser igual o mayor a 0")
                    except:
                        print("Error de valor ingresado, intenta nuevamente.\n")
#Contadores y totales
                if menu2==1:
                    ContCar+=cantidad
                    total+=Val_Car*ContCar
                elif menu2==2:
                    ContImp+=cantidad
                    total+=Val_Imp*ContImp
                elif menu2==3:
                    ContOrt+=cantidad
                    total+=Val_Ort*ContOrt
#Menu (Tipo de Trabajador)
            if menu2==4:
                print("-"*50)
                print("           Tipo de Trabajador\n")
                print("1) Trabajador Auxiliar         Descuento: 15%")
                print("2) Trabajador Administrativo   Descuento: 10%")
                print("3) Trabajador Docente          Descuento: 5%")
                print("-"*50)
                while True:
                    try:
                        tipo=int(input("Ingresar el tipo de trabajador: "))
                        if 1<=tipo<=3:
                            print("Descuento aplicado")
                            break
                        else:
                            print("La opcion no esta dentro del rango\n")
                    except:
                        print("Error de valor ingresado, intenta nuevamente\n")
#Costo totla final con descuentos aplicados
                if tipo==1:
                    totalfinal = total*(1-TrAux)
                elif tipo==2:
                    totalfinal = total*(1-TrAdm)
                elif tipo==3:
                    totalfinal = total*(1-TrDoc)
#Detalle de cotizacion
                print("\n\n             *Detalle de cotizacion*")
                print("-"*50)
                if ContCar>0:
                    print(f"{ContCar} Tratamiento Carillas Porcelana  ${Val_Car*ContCar}")
                if ContImp > 0:
                    print(f"{ContImp} Implantes Dentales              ${Val_Imp*ContImp}")
                if ContOrt > 0:
                    print(f"{ContOrt} Ortodoncia de Brackets          ${Val_Ort*ContOrt}")
                if total> 0:
                    print("-"*50)
                print(f"SubTotal: ${total}")
                if tipo == 1 :
                    print(f"Descuento aplicado {round(TrAux*100)}%   -${round(total-totalfinal)}")
                elif tipo == 2 :
                    print(f"Descuento aplicado {round(TrAdm*100)}%   -${round(total-totalfinal)}")
                elif tipo == 3 :
                    print(f"Descuento aplicado {round(TrDoc*100)}%   -${round(total-totalfinal)}")
                print("-"*50)
                print(f"Total: ${round(totalfinal)}")
                print(f"Son 12 cuotas de: ${round(totalfinal/12)}")
                print("-"*50)
                print("Sonria Bonito :)\n\n\n")
#Reinicio de valores de la cotizacion                         
    if menu1==2:
        print("Valores reiniciados")
        total=0
        ContCar=0
        ContImp=0
        ContOrt=0
