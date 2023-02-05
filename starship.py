import sqlite3

class StarShip:
    name = "StarShip"

#Metodo Constructor para la clase StarShip
    def __init__(self,shipid,shipName,country,year,fueltype):
        self.__shipid=shipid
        self.__shipName=shipName
        self.__country=country
        self.__year = year
        self.__fueltype = fueltype

    #GETTERS
    #Obtiene la informacion
    def getshipinfo(info=None):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        if info==None:
            #data to create spaceship id, shipname, country, year, fueltype, shiptype, crewmembers
            cursor.execute('SELECT * from ships')
            ships = cursor.fetchall()
            if(ships!=None):
                print("No tenemos información, por favor agregue una nave")
        else:
            cursor.execute('SELECT * from ships WHERE shiptype=?',(info,))
            ships = cursor.fetchall()
            if(ships!=None):
                print("No tenemos información, por favor agregue una nave")
        for ship in ships:
            print("---------------------------")
            print("id:",ship[0])
            print("Nombre de la nave:",ship[1])
            print("Pais de la nave:",ship[2])
            print("Año de operación:",ship[3])
            print("Tipo de Combustible:",ship[4])
            print("Tipo de nave:",ship[5])
            print("Capacidad de tripulantes:",ship[6])
            print("---------------------------")
        conn.commit()
        conn.close()

    #BEHAVIORS
    def launch():
        return "Launching"
    
    def land():
        return "Landing"
    
    def location():
        return "Position in X, Position in Y"

    def createstarship():
        shipName = input("starship Name: ")
        country = input("Country: ")
        year = int(input("Year: "))
        fueltype = input("fueltype: ")
        shiptype = int(input("Seleccione el tipo de nave 1-Lanzador 2-Nave No Tripulada 3-Nave Tripulada opción: "))
        if(shiptype==3):
            crewmembers = int(input("Indique la cantidad de tripulantes: "))
        else:
            crewmembers = 0
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        #data to create spaceship shipname, country, year, fueltype, shiptype, crewmembers
        cursor.execute("INSERT INTO ships VALUES(NULL,?,?,?,?,?,?)",(shipName,country,year,fueltype,shiptype,crewmembers))
        conn.commit()
        conn.close()
        return "Nave creada correctamente"

class Launcher(StarShip):
    def decoupling():
        return "Desacople Exitoso"
    
    def createstarship():
        shipName = input("starship Name: ")
        country = input("Country: ")
        year = int(input("Year: "))
        fueltype = input("fueltype: ")
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        #data to create spaceship shipname, country, year, fueltype, shiptype, crewmembers
        cursor.execute("INSERT INTO ships VALUES(NULL,?,?,?,?,?,?)",(shipName,country,year,fueltype,1,0))
        conn.commit()
        conn.close()
        return "Nave creada correctamente"

    def activateignition():
        return "Ignicion activada Exitosamente"

class noncrew(StarShip):
    def getprobe():
        return "Muestra tomada exitosamente"
    
    def createstarship():
        shipName = input("starship Name: ")
        country = input("Country: ")
        year = int(input("Year: "))
        fueltype = input("fueltype: ")
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        #data to create spaceship shipname, country, year, fueltype, shiptype, crewmembers
        cursor.execute("INSERT INTO ships VALUES(NULL,?,?,?,?,?,?)",(shipName,country,year,fueltype,2,0))
        conn.commit()
        conn.close()
        return "Nave creada correctamente"
    
class crew(StarShip):
    def getmanualcontrol():
        return "Control Manual activado"
    
    def createstarship():
        shipName = input("starship Name: ")
        country = input("Country: ")
        year = int(input("Year: "))
        fueltype = input("fueltype: ")
        crewmates = int(input("Crewmates: "))
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        #data to create spaceship shipname, country, year, fueltype, shiptype, crewmembers
        cursor.execute("INSERT INTO ships VALUES(NULL,?,?,?,?,?,?)",(shipName,country,year,fueltype,3,crewmates))
        conn.commit()
        conn.close()
        return "Nave creada correctamente"
