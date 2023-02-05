from starship import StarShip, Launcher, crew, noncrew


if __name__=="__main__":
    exit = 'N'
    while(exit=='n'or exit=='N'):
        option = int(input("""\nBienvenido, Menú principal.\nSeleccione una opción:
        \n1- Mostrar naves
        \n2- Crear nave
        \n3- Buscar nave
        \n4- Realizar accion sobre nave
        \n5- Salir
        \nopción: """))
        if(option==1):
            StarShip.getshipinfo()
            input("Presione Enter para continuar")
        elif(option==2):
            shiptype = int(input("Por favor escoja el tipo de nave 1-Lanzador, 2-Nave no tripulada, 3-Nave tripulada opción: "))
            if(shiptype==1):
                Launcher.createstarship()
            elif(shiptype==2):
                noncrew.createstarship()
            elif(shiptype==3):
                crew.createstarship()
        elif(option==3):
            shiptype = int(input("Por favor escoja el tipo de nave 1-Lanzador, 2-Nave no tripulada, 3-Nave tripulada opción: "))
            if(shiptype==1):
                Launcher.getshipinfo(1)
            elif(shiptype==2):
                noncrew.getshipinfo(2)
            elif(shiptype==3):
                crew.getshipinfo(3)
            input("Presione Enter para continuar")
        elif(option==4):
            shiptype = int(input("Por favor escoja el tipo de nave 1-Lanzador, 2-Nave no tripulada, 3-Nave tripulada opción: "))
            if(shiptype==1):
                action=int(input("Seleccione el tipo de accion que desea realizar la nave 1-Despegar, 2-Aterrizar, 3-Desacoplarse, 4-Activar Ignición 5-Dar Ubicacion opción:"))
                if(action==1):
                    print(Launcher.launch())
                    input("Presione Enter para continuar")
                elif(action==2):
                    print(Launcher.land())
                    input("Presione Enter para continuar")
                elif(action==3):
                    print(Launcher.decoupling())
                    input("Presione Enter para continuar")
                elif(action==4):
                    print(Launcher.activateignition())
                    input("Presione Enter para continuar")
                elif(action==5):
                    print(Launcher.location())
                    input("Presione Enter para continuar")
                else:
                    print("Opción no habilitada")
            elif(shiptype==2):
                action=int(input("Seleccione el tipo de accion que desea realizar la nave 1-Despegar, 2-Aterrizar, 3-Tomar Muestra, 4- Dar Ubicación opción: "))
                if(action==1):
                    print(noncrew.launch())
                    input("Presione Enter para continuar")
                elif(action==2):
                    print(noncrew.land())
                    input("Presione Enter para continuar")
                elif(action==3):
                    print(noncrew.getprobe())
                    input("Presione Enter para continuar")
                elif(action==4):
                    print(noncrew.location())
                    input("Presione Enter para continuar")
                else:
                    print("Opción no habilitada")
            elif(shiptype==3):
                action=int(input("Seleccione el tipo de accion que desea realizar la nave 1-Despegar, 2-Aterrizar, 3-Tomar Control Manual, 4-Dar Ubicación opción: "))
                if(action==1):
                    print(crew.launch())
                    input("Presione Enter para continuar")
                elif(action==2):
                    print(crew.land())
                    input("Presione Enter para continuar")
                elif(action==3):
                    print(crew.getmanualcontrol())
                    input("Presione Enter para continuar")
                elif(action==4):
                    print(crew.location())
                    input("Presione Enter para continuar")
                else:
                    print("Opción no habilitada")
        elif(option==5):
            exit = input("Está seguro que desea Salir? [n, y] opción: ")
        
        
