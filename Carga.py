import json
import BD
import random
import os
def leer_conf_autosave(archivo="conf_autosave.json"):
    try:
        ruta_base = os.path.dirname(os.path.abspath(__file__))
        ruta_credenciales = os.path.join(ruta_base, archivo)
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
        N_empleados, N_puestos, NJEFES = BD.ContarNumeroDatos()
        print("\nContenido del archivo conf_autosave.json:\n")
        for item in datos:
            tabla = item.get("tabla", "N/A")
            metodo = item.get("metodo", "N/A")
            if tabla != "N/A" and metodo != "N/A":
                if tabla == "TAB_EMPLEADO":
                  if metodo == "datos sintéticos":
                    print(f"Tabla: {tabla}, Método: {metodo}")
                    BD.Limpiar_QA()
                    BD.cargar_empleados_sinteticos(N_puestos)
                  elif metodo == "datos hasheados":
                    print(f"Tabla: {tabla}, Método: {metodo}")
                    BD.Limpiar_QA()
                    BD.cargar_empleados_hash(random.random(), N_puestos)
                  elif metodo == "datos enmascarados":
                    print(f"Tabla: {tabla}, Método: {metodo}")
                    BD.Limpiar_QA()
                    BD.cargar_empleados_enmascarar(random.random(), N_puestos)
                elif tabla == "TAB_PUESTO":
                  if metodo == "datos sintéticos":
                    print(f"Tabla: {tabla}, Método: {metodo}")
                    BD.Limpiar_TP()
                    BD.cargar_puestos_sinteticos(random.random())
                  elif metodo == "datos hasheados":
                    print(f"Tabla: {tabla}, Método: {metodo}")
                    BD.Limpiar_TP()
                    BD.cargar_puestos_hash(random.random(), N_puestos)
                elif tabla == "TAB_JEFESDEPARTAMENTO":
                  print(f"Tabla: {tabla}, Método: {metodo}")
                  if metodo == "datos sintéticos":
                    BD.cargar_jefes_sinteticos(NJEFES, random.random())

    except FileNotFoundError:
        print(f"❌ No se encontró el archivo {archivo}")
    except json.JSONDecodeError:
        print(f"❌ Error al decodificar el archivo {archivo}")

# ==========================
# Programa principal
# ==========================
if __name__ == "__main__":
    leer_conf_autosave()