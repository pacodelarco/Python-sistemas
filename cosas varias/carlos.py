import pymysql
miConexion =pymysql.connect(host="localhost",user="root",passwd="user",database="python_sidaw")

menu1 = int(input("Indica: \n1-> Tabla alumnos\n2-> Tabla profesores\n3-> Tabla escuela\n4-> Tabla asignatura\n0-> salir\n"))

while menu1 != 0:
    if menu1== 1:
        menu2 = int(input("Indica: \n1-> Insertar alumno en la tabla\n2-> Buscar registro en la tabla\n3-> Actualizar registro en la tabla\n4-> Eliminar registro\n5-> volver\n"))
        while menu2 !=0:
            if menu2 == 1:
                def insertarUsuario():
                    dni = input(("Indique el dni del alumno\n"))
                    nombreA = input(("Indique el nombre del alumno\n"))
                    apellido1A = input(("Indique el primer apellido del alumno\n"))
                    apellido2A = input(("Indique el segundo apellido del alumno\n"))
                    mycursor = miConexion.cursor()
                    sql = "INSERT INTO alumno (dni, nombre,apellido1,apellido2) VALUES ('%s', '%s','%s','%s')"%(dni,nombreA,apellido1A,apellido2A)
                    mycursor.execute(sql)
                    miConexion.commit()
                    miConexion.close()
                insertarUsuario()
            if menu2==2:
                def buscarUsuario():
                    nombreA = input("Indique el nombre del usuario que quieres ver\n")
                    mycursor = miConexion.cursor()
                    sql = "select * from alumno where nombre = '%s'"%(nombreA)
                    mycursor.execute(sql)
                    resultadoA = mycursor.fetchall()
                    print(resultadoA)
                    miConexion.commit()
                    miConexion.close()
                buscarUsuario()
            if menu2==3:
                def actualizarUsuario():
                    nombreA = input("Indique el nombre de alumno que quiere modificar\n")
                    nombreAn = input("Indique el nuevo nombre para el alumno\n")
                    mycursor = miConexion.cursor()
                    sql = "Update alumno set nombre ='%s'"%(nombreAn)+"where nombre = '%s'"%(nombreA)
                    mycursor.execute(sql)
                    resultadoA = mycursor.fetchall()
                    miConexion.commit()
                    miConexion.close()
                actualizarUsuario()
            if menu2==4:
                def borrarUsuario():
                    nombreA = input("Indique el nombre del usuario que quieres borrar\n")
                    mycursor = miConexion.cursor()
                    sql = "delete from alumno where nombre = '%s'"%(nombreA)
                    mycursor.execute(sql)
                    resultadoA = mycursor.fetchall()
                    print(resultadoA)
                    miConexion.commit()
                    miConexion.close()
                borrarUsuario()
            if menu2==0:
                break;       
    if menu1==2:
        menu3 = int(input("Indica: \n1-> Insertar profesor en la tabla\n2-> Buscar registro en la tabla\n3-> Actualizar registro en la tabla\n4-> Eliminar registro\n"))
        while menu3 !=0:
                if menu3==1:
                    def insertarProfesor():
                        mycursor = miConexion.cursor()
                        dnip = input(("Indique el dni del profesor\n"))
                        nombrep = input(("Indique el nombre del profesor\n"))
                        apellido1p = input(("Indique el primer apellido del profesor\n"))
                        apellido2p = input(("Indique el segundo apellido del profesor\n"))
                        sql = "INSERT INTO profesor (dni, nombre,apellido1,apellido2) VALUES ('%s', '%s','%s','%s')"%(dnip,nombrep,apellido1p,apellido2p)
                        mycursor.execute(sql)
                        miConexion.commit()
                        miConexion.close()
                        insertarProfesor()
                if menu3==2:
                    def buscarUsuario():
                        nombreP = input("Indique el nombre del profesor que quieres ver\n")
                        mycursor = miConexion.cursor()
                        sql = "select * from profesor where nombre = '%s'"%(nombreP)
                        mycursor.execute(sql)
                        resultadoA = mycursor.fetchall()
                        print(resultadoA)
                        miConexion.commit()
                        miConexion.close()
                buscarUsuario()
                if menu3==3:
                    def actualizarUsuario():
                        nombreA = input("Indique el nombre de profesor que quiere modificar\n")
                        nombreAn = input("Indique el nuevo nombre para el profesor\n")
                        mycursor = miConexion.cursor()
                        sql = "Update profesor set nombre ='%s'"%(nombreAn)+"where nombre = '%s'"%(nombreA)
                        mycursor.execute(sql)
                        resultadoAp = mycursor.fetchall()
                        miConexion.commit()
                        miConexion.close()
                    actualizarUsuario()
                if menu3==4:
                    def borrarUsuario():
                        nombreA = input("Indique el nombre del profesor que quieres borrar\n")
                        mycursor = miConexion.cursor()
                        sql = "delete from profesor where nombre = '%s'"%(nombreA)
                        mycursor.execute(sql)
                        resultadoA = mycursor.fetchall()
                        print(resultadoA)
                        miConexion.commit()
                        miConexion.close()
                    borrarUsuario()
                if menu3==0:
                    break; 

    elif menu1==3:
        menu4 = int(input("Indica: \n1-> Insertar escuela en la tabla\n2-> Buscar registro en la tabla\n3-> Actualizar registro en la tabla\n4-> Eliminar registro\n"))
        while menu4 !=0:
            if menu4==1:
                    def insertarEscuela():
                        mycursor = miConexion.cursor()
                        id = input(("Indique el id de la escuela\n"))
                        nombreE = input(("Indique el nombre de la escuela\n"))
                        localidad = input(("Indique la localidad de la escuela\n"))
                        sql = "INSERT INTO escuela (dni, nombre,localidad) VALUES ('%s', '%s','%s')"%(id,nombreE,localidad)
                        mycursor.execute(sql)
                        miConexion.commit()
                        miConexion.close()
                    insertarProfesor()
            if menu4==2:
                    def buscarUsuario():
                        nombreP = input("Indique el nombre de la escuela que quieres ver\n")
                        mycursor = miConexion.cursor()
                        sql = "select * from escuela where nombre = '%s'"%(nombreP)
                        mycursor.execute(sql)
                        resultadoA = mycursor.fetchall()
                        print(resultadoA)
                        miConexion.commit()
                        miConexion.close()
                    buscarUsuario()
            if menu4==3:
                    def actualizarUsuario():
                        nombreA = input("Indique el nombre de la escuela que quiere modificar\n")
                        nombreAn = input("Indique el nuevo nombre para la escuela\n")
                        mycursor = miConexion.cursor()
                        sql = "Update escuela set nombre ='%s'"%(nombreAn)+"where nombre = '%s'"%(nombreA)
                        mycursor.execute(sql)
                        resultadoAp = mycursor.fetchall()
                        miConexion.commit()
                        miConexion.close()
                    actualizarUsuario()
            if menu4==4:
                    def borrarUsuario():
                        nombreA = input("Indique el nombre del escuela que quieres borrar\n")
                        mycursor = miConexion.cursor()
                        sql = "delete from escuela where nombre = '%s'"%(nombreA)
                        mycursor.execute(sql)
                        resultadoA = mycursor.fetchall()
                        print(resultadoA)
                        miConexion.commit()
                        miConexion.close()
                    borrarUsuario()
            if menu4==0:
                    break; 

    elif menu1==4:
        menu5 = int(input("Indica: \n1-> Insertar asignatura en la tabla\n2-> Buscar registro en la tabla\n3-> Actualizar registro en la tabla\n4-> Eliminar registro\n"))
        while menu2 !=0:
            if menu5==1:
                def insertarAsignatura():
                    mycursor = miConexion.cursor()
                    nombreAs = input(("Indique el nombre de la asignatura\n"))
                    clase = input(("Indique la clase donde se imparte\n"))
                    sql = "INSERT INTO asignatura (nombre,clase) VALUES ('%s', '%s')"%(nombreAs,clase)
                    mycursor.execute(sql)
                    miConexion.commit()
                    miConexion.close()
                    insertarEscuela()
            if menu5==2:
                    def buscarUsuario():
                        nombreP = input("Indique el nombre de la asignatura que quieres ver\n")
                        mycursor = miConexion.cursor()
                        sql = "select * from asignatura where nombre = '%s'"%(nombreP)
                        mycursor.execute(sql)
                        resultadoA = mycursor.fetchall()
                        print(resultadoA)
                        miConexion.commit()
                        miConexion.close()
                    buscarUsuario()
            if menu5==3:
                    def actualizarUsuario():
                        nombreA = input("Indique el nombre de la asignatura que quiere modificar\n")
                        nombreAn = input("Indique el nuevo nombre para la asignatura\n")
                        mycursor = miConexion.cursor()
                        sql = "Update asignatura set nombre ='%s'"%(nombreAn)+"where nombre = '%s'"%(nombreA)
                        mycursor.execute(sql)
                        resultadoAp = mycursor.fetchall()
                        miConexion.commit()
                        miConexion.close()
                    actualizarUsuario()
            if menu5==4:
                    def borrarUsuario():
                        nombreA = input("Indique el nombre de la asignatura que quieres borrar\n")
                        mycursor = miConexion.cursor()
                        sql = "delete from asignatura where nombre = '%s'"%(nombreA)
                        mycursor.execute(sql)
                        resultadoA = mycursor.fetchall()
                        print(resultadoA)
                        miConexion.commit()
                        miConexion.close()
                    borrarUsuario()
            if menu5==0:
                    break; 
