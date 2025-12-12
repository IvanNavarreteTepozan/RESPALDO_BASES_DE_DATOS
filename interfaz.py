import os
import random
import BD
import json


# ==========================
# Funciones auxiliares
# ==========================

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

def pedir_entero(mensaje, minimo=1, maximo=None):
    """
    Solicita un número entero al usuario con validación.
    - mensaje: texto mostrado al usuario
    - minimo: valor mínimo permitido (default=1)
    - maximo: valor máximo permitido (default=None, sin límite)
    """
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo:
                print(f"⚠️ El valor debe ser mayor o igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"⚠️ El valor debe ser menor o igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("⚠️ Entrada inválida. Ingresa un número entero.")
            
            

# ==========================
# Menú de selección de tablas y métodos (sin librerías externas)
# ==========================

def menu_tablas_metodos():
    tablas_metodos = {
        "TAB_EMPLEADO": ["datos sintéticos", "datos hasheados", "datos enmascarados"],
        "TAB_PUESTO": ["datos sintéticos", "datos hasheados"],
        "TAB_JEFESDEPARTAMENTO": ["datos sintéticos"]
    }

    resultados = []

    for tabla, metodos in tablas_metodos.items():
        limpiar_pantalla()
        print(f"\nSelecciona método para la tabla: {tabla}")
        for i, metodo in enumerate(metodos, start=1):
            print(f"{i}. {metodo}")
        opcion = input("Escriba su opción (número): ")

        try:
            idx = int(opcion) - 1
            if 0 <= idx < len(metodos):
                resultados.append({"tabla": tabla, "metodo": metodos[idx]})
            else:
                print("Opción inválida, se omite esta tabla.")
        except ValueError:
            print("Entrada inválida, se omite esta tabla.")

    # Guardamos en JSON
    ruta_base = os.path.dirname(os.path.abspath(__file__))
    ruta = os.path.join(ruta_base,"conf_autosave.json" )
    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=4)

    print("\n✅ Archivo 'conf_autosave.json' generado con éxito.")
    input("Presione enter para continuar...")


# ==========================
# Menús originales
# ==========================

def menu_empleado():
    while True:
        limpiar_pantalla()
        print("\n\n\nMetodos para TAB_EMPLEADO:")
        print("1. cargar_empleados_sinteticos")
        print("2. cargar_empleados_hash")
        print("3. cargar_empleados_enmascarar")
        print("0. Regresar")
        opcion2 = input("Escriba su opcion(numero): ")

        if opcion2 == "0":
            break
        elif opcion2 == "1":
            print("\n\n\nEmpleados a cargar:")
            print("1. Decidir cantidad")
            print("2. misma cantidad que en PRODUCCION")
            opcion3 = input("Escriba su opcion(numero): ")
            if opcion3 == "1":
                N_empleados = int(pedir_entero("Cantidad de empelados: "))
                BD.cargar_empleados_sinteticos(N_empleados)
            elif opcion3 == "2":
                N_empleados, N_puestos, NJEFES = BD.ContarNumeroDatos()
                BD.Limpiar_QA()
                BD.cargar_empleados_sinteticos(N_empleados)
        elif opcion2 == "2":
            print("\n\n\nEmpleados a cargar:")
            print("1. Decidir cantidad")
            print("2. ACTUALIZAR como PRODUCCION")
            opcion3 = input("Escriba su opcion(numero): ")
            if opcion3 == "1":
                N_empleados = int(pedir_entero("Cantidad de empelados: "))
                BD.cargar_empleados_hash(random.random(), N_empleados)
            elif opcion3 == "2":
                N_empleados, N_puestos, NJEFES = BD.ContarNumeroDatos()
                BD.Limpiar_QA()
                BD.cargar_empleados_hash(random.random(), N_empleados)
        elif opcion2 == "3":
            print("\n\n\nEmpleados a cargar:")
            print("1. Decidir cantidad")
            print("2. ACTUALIZAR como PRODUCCION")
            opcion3 = input("Escriba su opcion(numero): ")
            if opcion3 == "1":
                N_empleados = int(pedir_entero("Cantidad de empelados: "))
                BD.cargar_empleados_enmascarar(random.random(), N_empleados)
            elif opcion3 == "2":
                N_empleados, N_puestos, NJEFES = BD.ContarNumeroDatos()
                BD.Limpiar_QA()
                BD.cargar_empleados_enmascarar(random.random(), N_empleados)


def menu_puesto():
    while True:
        limpiar_pantalla()
        print("\n\n\nMetodos para TAB_PUESTO:")
        print("1. cargar_puestos_sinteticos")
        print("2. cargar_puestos_hash")
        print("0. Regresar")
        opcion2 = input("Escriba su opcion(numero): ")

        if opcion2 == "0":
            break
        elif opcion2 == "1":
            N_empleados, N_puestos, NJEFES = BD.ContarNumeroDatos()
            BD.Limpiar_TP()
            BD.cargar_puestos_sinteticos(random.random())
        elif opcion2 == "2":
            print("\n\n\nPuestos a cargar:")
            print("1. Decidir cantidad")
            print("2. ACTUALIZAR como PRODUCCION")
            opcion3 = input("Escriba su opcion(numero): ")
            if opcion3 == "1":
                N_puestos = int(pedir_entero("Cantidad de puestos: "))
                BD.cargar_puestos_hash(random.random(), N_puestos)
            elif opcion3 == "2":
                N_empleados, N_puestos, NJEFES = BD.ContarNumeroDatos()
                BD.Limpiar_TP()
                BD.cargar_puestos_hash(random.random(), N_puestos)


def menu_jefes():
    while True:
        limpiar_pantalla()
        print("\n\n\n Metodos para TAB_JEFESDEPARTAMENTO:")
        print("1. cargar_jefes_sinteticos")
        print("0. Regresar")
        opcion2 = input("Escriba su opcion(numero): ")

        if opcion2 == "0":
            break
        elif opcion2 == "1":
            print("\n\n\nJefes a cargar:")
            print("1. Decidir cantidad")
            print("2. ACTUALIZAR como PRODUCCION")
            opcion3 = input("Escriba su opcion(numero): ")
            if opcion3 == "1":
                jefes = []
                for i in range(1, 10):
                    jefes.append(int(pedir_entero(f"Cantidad de jefes del departamento {i}: ")))
                NJEFES = ",".join(map(str, jefes))
                BD.cargar_jefes_sinteticos(NJEFES, random.random())
            elif opcion3 == "2":
                N_empleados, N_puestos, NJEFES = BD.ContarNumeroDatos()
                BD.cargar_jefes_sinteticos(NJEFES, random.random())


def menu_principal():
    while True:
        limpiar_pantalla()
        print("\n\n\n\n Menu Principal")
        print("Tablas a modificar:")
        print("1. TAB_EMPLEADO")
        print("2. TAB_PUESTO")
        print("3. TAB_JEFESDEPARTAMENTO")
        print("4. Configurar Metodos y tablas para autoguardado diario")
        print("0. Salir")
        opcion = input("Escriba su opcion(numero): ")

        if opcion == "0":
            break
        elif opcion == "1":
            menu_empleado()
        elif opcion == "2":
            menu_puesto()
        elif opcion == "3":
            menu_jefes()
        elif opcion == "4":
            menu_tablas_metodos()
        else:
            print("Opcion no valida")
            input("Presione enter para continuar...")


# ==========================
# Programa principal
# ==========================

if __name__ == "__main__":
    while BD.probar_credenciales() == 0:
        print("Credenciales incorrectas")
        input("Presione enter para continuar")
        limpiar_pantalla()
    menu_principal()