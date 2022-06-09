

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

connection= pymysql.connect(host="localhost",user="root",passwd="user",database="python_sidaw")



tablaElegida = int(input("Elige la tabla sobre la que hacer la consulta: \n\t1 - Competicion\n\t2 - Equipo\n\t3 - Fabricante\n\t4 - Piloto\n\t0 - salir\n\n"))
while tablaElegida !=0:
    if tablaElegida == 1:
        opcionElegida = int(input("\tTABLA COMPETICION\n1 - Insertar registro\n2 - Mostrar registro\n3 - Actualizar registro\n4 - Borrar registro \n\n"))
        while opcionElegida !=0:
            if opcionElegida == 1:
                def insertCompeticion():
                    
                    nombre=input("Indica nombre de la competicion\n")
                    numeroPremios=input("Indica cuantas carreras se corren\n")
                    numeroPilotos=input("Indica cuantos pilotos compiten\n")
                    cursor=connection.cursor()
                    sql="INSERT INTO Competicion (nombre, numeroPremios, numeroPilotos) VALUES ('%s','%s','%s')"%(nombre,numeroPremios,numeroPilotos)
                    cursor.execute(sql)
                    connection.commit()
                    connection.close()
                insertCompeticion()













# insert


# select



# update

# delete


connection.close()
