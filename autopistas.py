vehiculos={"auto":20,"moto":10,"camion":25}

def imprimir_ticket(vehiculo):
    price=vehiculos[vehiculo]
    print("el vheviculo",vehiculo,"tiene una tarifa de",price)
def user_menu():
    while True :
        print("opciones:")
        print("1-auto")
        print("2- camion")
        print("3-moto")
        opcion = input("eliga una opcion:")
        if opcion == "1":
            imprimir_ticket("auto")
        elif opcion=="2":
            imprimir_ticket("camion")
        elif opcion =="3":
            imprimir_ticket("moto")
        else:
            print("opcion invalida")

user_menu()




