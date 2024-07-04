import os
import helpers
import database as db

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("============================== ")
        print("     Bienvenido al Gestor      ")
        print("============================== ")
        print("   [1] Listar los clientes     ")
        print("   [2] Buscar un cliente       ")
        print("   [3] Añadir los clientes     ")
        print("   [4] Modificar los clientes  ")
        print("   [5] Borrar los clientes     ")
        print("   [6] Cerrar el Gestor        ")
        print("============================== ")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Listando los clientes...\n")
            for cliente in db.Clientes.lista:
                print(cliente)

        if opcion == '2':
            print("Buscando los clientes...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 INT y 1 CHAR)").upper()
            cliente = db.Clientes.buscar(dni)
            print(cliente) if cliente else print("Cliente no encontrado.")

        if opcion == '3':
            print("Añadir los clientes...\n")
            
            dni = None
            while True:
                dni = helpers.leer_texto(3, 3, "DNI (2 INT y 1 CHAR)").upper()
                if helpers.dni_valido(dni, db.Clientes.lista):
                    break

            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 CHAR)").capitalize()
            apellido = helpers.leer_texto(2, 30, "Apellido (de 2 a 30 CHAR)").capitalize()
            db.Clientes.crear(dni, nombre, apellido)
            print("Cliente añadido correctamente.")

        if opcion == '4':
            print("Modificar los clinetes...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 INT y 1 CHAR)").upper()
            cliente = db.Clientes.buscar(dni)
            if cliente:
                nombre = helpers.leer_texto(2, 30, f"Nombre (de 2 a 30 CHAR) [{cliente.nombre}] ").capitalize()
                apellido = helpers.leer_texto(2, 30, f"Apellido (de 2 a 30 CHAR) [{cliente.apellido}] ").capitalize()
                db.Clientes.modificar(cliente.dni, nombre, apellido)
                print("Cliente modificado correctamente")
            else:
                print("Cliente no encontrado")
            

        if opcion == '5':
            print("Borrar los clinetes...\n")
            dni = helpers.leer_texto(3, 3, "DNI (2 INT y 1 CHAR)").upper()
            print("Cliente borrado correctamente.") if db.Clientes.borrar(dni) else print("Cliente no encontrado.")

        if opcion == '6':
            print("Saliendo...\n")
            break

        input("\nPresiona ENTER para continuar...")