

# * conexion a la base de datos

# definicion de funciones

# codigo principal
# menu
# opcion - llamada a las funciones
# que tabla - insertar, actualizar, select, borrar
# *salir - Desconexion

from tkinter import E, W
from warnings import catch_warnings
from prompt_toolkit import VERSION
import pymysql

class Acciones:
    def insertCompeticion():                
        nombre=input("Indica nombre de la competicion\n")
        numeroPremios=input("Indica cuantas carreras se corren\n")
        numeroPilotos=input("Indica cuantos pilotos compiten\n")
        cursor=connection.cursor()
        sql="INSERT INTO Competicion (nombre, numeroPremios, numeroPilotos) VALUES ('%s','%s','%s')"%(nombre,numeroPremios,numeroPilotos)
        cursor.execute(sql)
        connection.commit()
       

    def insertEquipo():                
        nombre=input("Indica nombre del equipo\n")
        empleados=input("Indica cuantos empleados tiene el equipo \n")
        presupuesto=input("Indica el presupuesto del equipo\n")
        cursor=connection.cursor()
        sql="INSERT INTO equipo (nombre, empleados, presupuesto) VALUES ('%s','%s','%s')"%(nombre,empleados,presupuesto)
        cursor.execute(sql)
        connection.commit()
       

    def insertFabricante():                
        nombre=input("Indica nombre del fabricante\n")
        numeroMotos=input("Indica cuantas motos tiene el fabricante en el campeonato \n")
        cilindrada=input("Indica el la cilidrada de las motos del campeonato\n")
        cursor=connection.cursor()
        sql="INSERT INTO fabricante (nombre, numeroMotos, cilindrada) VALUES ('%s','%s','%s')"%(nombre,numeroMotos,cilindrada)
        cursor.execute(sql)
        connection.commit()
    
    def insertPiloto():                
        nombre=input("Indica nombre del piloto\n")
        dorsal=input("Indica el numero del piloto\n")
        cursor=connection.cursor()
        sql="INSERT INTO piloto (nombre, dorsal) VALUES ('%s','%s','%s')"%(nombre,dorsal)
        cursor.execute(sql)
        connection.commit()
       

    def selectCompeticion():
        nombre = input("Indique el nombre de la competicion a mostrar\n")
        cursor=connection.cursor()
        sql = "select * from competicion where nombre = '%s'"%(nombre)
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print(resultado)
       

    def selectEquipo():
        nombre = input("Indique el nombre del equipo a mostrar\n")
        cursor=connection.cursor()
        sql = "select * from equipo where nombre = '%s'"%(nombre)
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print(resultado)
       
        
    def selectFabricante():
        nombre = input("Indique el nombre del fabricante a mostrar\n")
        cursor=connection.cursor()
        sql = "select * from fabricante where nombre = '%s'"%(nombre)
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print(resultado)
       
    def selectPiloto():
        nombre = input("Indique el nombre del piloto a mostrar\n")
        cursor=connection.cursor()
        sql = "select * from piloto where nombre = '%s'"%(nombre)
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print(resultado)
    
    def updateCompeticion():
        nombre = input("Indique el nombre de la competicion a modificar\n")
        nombreNuevo = input("Indique el nuevo nombre para la competicion\n")
        cursor=connection.cursor()
        sql = "Update competicion set nombre ='%s'"%(nombreNuevo)+"where nombre = '%s'"%(nombre)
        cursor.execute(sql)
        resultado = cursor.fetchall()
        connection.commit()
       

    def updateEquipo():
        nombre = input("Indique el nombre del equipo a modificar\n")
        nombreNuevo = input("Indique el nuevo nombre del equipo\n")
        cursor=connection.cursor()
        sql = "Update equipo set nombre ='%s'"%(nombreNuevo)+"where nombre = '%s'"%(nombre)
        cursor.execute(sql)
        resultado = cursor.fetchall()
        connection.commit()
       

    def updateFabricante():
        nombre = input("Indique el nombre del fabricante a modificar\n")
        nombreNuevo = input("Indique el nuevo nombre del equipo\n")
        cursor=connection.cursor()
        sql = "Update equipo set nombre ='%s'"%(nombreNuevo)+"where nombre = '%s'"%(nombre)
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print(resultado)
        connection.commit()

    def updatePiloto():
        nombre = input("Indique el nombre del piloto a modificar\n")
        nombreNuevo = input("Indique el nuevo nombre del piloto\n")
        cursor=connection.cursor()
        sql = "Update piloto set nombre ='%s'"%(nombreNuevo)+"where nombre = '%s'"%(nombre)
        cursor.execute(sql)
        resultado = cursor.fetchall()
        print(resultado)
        connection.commit()
       

    def borrarCompeticion():
        nombre = input("Indique el nombre de la competicion a borrar\n")
        cursor=connection.cursor()
        sql = "delete from competicion where nombre = '%s'"%(nombre)
        cursor.execute(sql)
        cursor=connection.cursor()
        resultado = cursor.fetchall()
        print(resultado)
        connection.commit()
       

    def borrarEquipo():
        nombre = input("Indique el nombre del equipo a borrar\n")
        cursor=connection.cursor()
        sql = "delete from equipo where nombre = '%s'"%(nombre)
        cursor=connection.cursor()
        resultado = cursor.fetchall()
        print(resultado)
        connection.commit()

    def borrarFabricante():
        nombre = input("Indique el nombre del fabricante a borrar\n")
        cursor=connection.cursor()
        sql = "delete from fabricante where nombre = '%s'"%(nombre)
        cursor=connection.cursor()
        resultado = cursor.fetchall()
        print(resultado)
        connection.commit()

    def borrarFabricante():
        nombre = input("Indique el nombre del piloto a borrar\n")
        cursor=connection.cursor()
        sql = "delete from piloto where nombre = '%s'"%(nombre)
        cursor=connection.cursor()
        resultado = cursor.fetchall()
        print(resultado)
        connection.commit()
       


connection= pymysql.connect(host="localhost",user="root",passwd="user",database="python_sidaw")

 


try:
    tablaElegida = int(input("Elige la tabla sobre la que hacer la consulta: \n\t1 - Competicion\n\t2 - Equipo\n\t3 - Fabricante\n\t4 - Piloto\n\t0 - salir\n\n"))
    while tablaElegida !=0:
        if tablaElegida == 1:
            Salir=True
            while Salir:
                opcionElegida = int(input("\tTABLA COMPETICION\n1 - Insertar registro\n2 - Mostrar registro\n3 - Actualizar registro\n4 - Borrar registro \n\n"))
                if opcionElegida == 1:             
                    Acciones.insertCompeticion()
                    opcionElegida=7
                
                if opcionElegida == 2:             
                    Acciones.selectCompeticion()
                    opcionElegida=-1

                if opcionElegida == 3:             
                    Acciones.updateCompeticion()
                    opcionElegida=-1

                if opcionElegida == 4:             
                    Acciones.borrarCompeticion()
                    opcionElegida=-1

                if opcionElegida == 5:
                    Salir=False
                    break
        
        elif tablaElegida == 2:
            Salir=True
            while Salir:
                opcionElegida = int(input("\tTABLA EQUIPO\n1 - Insertar registro\n2 - Mostrar registro\n3 - Actualizar registro\n4 - Borrar registro \n\n"))

                if opcionElegida == 1:             
                    Acciones.insertEquipo()
                    opcionElegida=-1
                
                if opcionElegida == 2:             
                    Acciones.selectEquipo()
                    opcionElegida=-1

                if opcionElegida == 3:             
                    Acciones.updateEquipo()
                    opcionElegida=-1

                if opcionElegida == 4:             
                    Acciones.borrarEquipo()
                    opcionElegida=-1

                if opcionElegida == 5:
                    Salir=False
                    break

        elif tablaElegida == 3:
            Salir=True
            while Salir:
                opcionElegida = int(input("\tTABLA FABRICANTE \n1 - Insertar registro\n2 - Mostrar registro\n3 - Actualizar registro\n4 - Borrar registro \n\n"))

                if opcionElegida == 1:             
                    Acciones.insertFabricante()
                    opcionElegida=-1
                
                if opcionElegida == 2:             
                    Acciones.selectFabricante()
                    opcionElegida=-1

                if opcionElegida == 3:             
                    Acciones.updateFabricante()
                    opcionElegida=-1

                if opcionElegida == 4:             
                    Acciones.borrarFabricante()
                    opcionElegida=-1

                if opcionElegida == 5:
                    Salir=False
                    break
        
        elif tablaElegida == 4:
            Salir=True
            while Salir:
                opcionElegida = int(input("\tTABLA PILOTO \n1 - Insertar registro\n2 - Mostrar registro\n3 - Actualizar registro\n4 - Borrar registro \n\n"))

                if opcionElegida == 1:             
                    Acciones.insertPiloto()
                    opcionElegida=-1
                
                if opcionElegida == 2:             
                    Acciones.selectPiloto()
                    opcionElegida=-1

                if opcionElegida == 3:             
                    Acciones.updatePiloto()
                    opcionElegida=-1

                if opcionElegida == 4:             
                    Acciones.borrarPiloto()
                    opcionElegida=-1

                if opcionElegida == 5:
                    Salir=False
                    break


        elif tablaElegida == 5:
            break

        
                        










        # insert


        # select



    # update

    # delete


    connection.close()
