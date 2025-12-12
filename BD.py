import pandas as pd
from faker import Faker
import os
import random
import psycopg2
import json
import time

def probar_credenciales():
    try:
        with open("CREDENCIALES_QA.json") as f:
            params = json.load(f)
        params= dict(list(params.items())[:5])

        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.close()
        conn.close()
        return 1
    except psycopg2.Error as e:
        return 0

def generar_df(n,SEED):

    fake = Faker("es_MX")
    fake.seed_instance(SEED)
    registros = []

    for _ in range(n):
        nombre = fake.first_name()
        apellido_paterno = fake.last_name()
        apellido_materno = fake.last_name()
        fecha_nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=70)
        genero = random.choice(["M", "F"])

        registros.append({
            "nombre": nombre,
            "apellido_paterno": apellido_paterno,
            "apellido_materno": apellido_materno,
            "fecha_nacimiento": fecha_nacimiento.strftime("%Y-%m-%d"),
            "genero": genero
        })

    df = pd.DataFrame(registros)
    return df

def df_to_json(df)->int:
    try:
        filename = f"Data.json"
        if os.path.exists(filename):
            os.remove(filename)
        df.to_json(filename, orient="records", indent=4, force_ascii=False)
        return 1
    except Exception as e:
        print("ERROR: ",e)
        return 0

def reg_bitacora(cevento,coperacion,nregistros,ctabla):
    try:
        with open("CREDENCIALES_QA.json") as f:
            params = json.load(f)
        params= dict(list(params.items())[:5])
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT FN_REGISTRO_BITACORA(%s, %s, %s::int, %s);",(cevento, coperacion, nregistros, ctabla))
        resultado=cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return resultado

    except psycopg2.Error as e:
        print("Error desde PostgreSQL:", e.pgerror)
        print("Código SQLSTATE:", e.pgcode)
        return e.pgerror
def cargar_DatosBase(SEED):
    try:
        with open("CREDENCIALES_QA.json") as f:
            params = json.load(f)

        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        with open(f"Data.json", "r", encoding="utf-8") as f:
            data = f.read()

        cur.execute("SELECT FN_AgregarEmpleados_JSON(%s::jsonb, %s);", (data,round(SEED,5)))

        resultado = cur.fetchone()[0]
      # Confirmar cambios
        conn.commit()
      # Cerrar conexión
        cur.close()
        conn.close()
        return resultado
    except psycopg2.Error as e:
        print("Error desde PostgreSQL:", e.pgerror)
        print("Código SQLSTATE:", e.pgcode)
        return e.pgerror


def Calcular_Lotes(N_Datos):
  LOTES=int(N_Datos/100)
  Restante=N_Datos%100
  return LOTES,Restante

def Empleados_sinteticos(N_Datos,SEED):
  try:
      df_to_json(generar_df(N_Datos,SEED))
      return cargar_DatosBase(SEED)
  except Exception as e:
      print("ERROR: ",e)
      return -1

def cargar_empleados_sinteticos(N):
  try:
    LOTES, restante=Calcular_Lotes(N)
    total=0
    for i in range(LOTES):
      res=0
      while res!=1:
        SEED=random.random()
        res=Empleados_sinteticos(100,SEED)
      total+=res
      print(total/LOTES*100,"%")
    res=0
    while res!=1:
      SEED=random.random()
      res=Empleados_sinteticos(restante,SEED)
    print("CARGA EXITOSA!!")


    if res==1:
        print("REGISTRADO!!")
        resultado=reg_bitacora('carga de datos sinteticos en QA','INSERT',N,'TAB_EMPLEADO')
    else:
        print("FALLO AL REGISTRAR!!")
        resultado=reg_bitacora('se fallo al carga de datos sinteticos en QA','INSERT',N,'TAB_EMPLEADO')
  except Exception as e:
    print("ERROR: ",e)

def cargar_puestos_sinteticos(SEED):
    try:
        with open("CREDENCIALES_QA.json") as f:
            params = json.load(f)
        params= dict(list(params.items())[:5])
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT FN_REGISTRO_BITACORA ('carga de datos sinteticos en QA'::text,'INSERT'::varchar,((SELECT COUNT(*) from TAB_EMPLEADO)-(SELECT COUNT(*) from TAB_PUESTO))::int,'TAB_PUESTO');")
        cur.execute("SELECT FN_Agregarpuestos(%s);", (round(SEED,5),))

        resultado = cur.fetchone()[0]
      # Confirmar cambios
        conn.commit()
      # Cerrar conexión
        cur.close()
        conn.close()
        if resultado==1:
            print("CARGA EXITOSA!!")
        else:
            print("CARGA FALLIDA!!")
        return resultado
    except psycopg2.Error as e:
        print("Error desde PostgreSQL:", e.pgerror)
        print("Código SQLSTATE:", e.pgcode)
        return e.pgerror

def cargar_jefes_sinteticos(NJEFES,SEED):
    try:
        with open("CREDENCIALES_QA.json") as f:
            params = json.load(f)
        params= dict(list(params.items())[:5])
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        numeros = [int(x) for x in NJEFES.split(",")]
        total = sum(numeros)
        cur.execute("SELECT FN_ACTUALIZA_JEFES(%s, %s::float);",(NJEFES,SEED))
        cur.execute("SELECT FN_REGISTRO_BITACORA('carga de datos sinteticos en QA'::text,'INSERT'::varchar,(%s)::int,'TAB_JEFESDEPARTAMENTO'::varchar);",(total,))
        resultado=cur.fetchone()[0]
      # Confirmar cambios
        conn.commit()
      # Cerrar conexión
        cur.close()
        conn.close()
        if resultado==1:
            print("CARGA EXITOSA!!")
        elif resultado==0:
            print("CARGA FALLIDA!!")
        else:
            print("Ya Hay Jefes, no puede tener mas de un jefe por departamento")
        return resultado
    except psycopg2.Error as e:
        print("Error desde PostgreSQL:", e.pgerror)
        print("Código SQLSTATE:", e.pgcode)
        return e.pgerror

def cargar_empleados_hash(SEED,N_empleados):
  try:
        with open("CREDENCIALES_QA.json") as f:
            params = json.load(f)
        params= dict(list(params.items())[:5])
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("select fn_agregar_empleados_hash(%s,%s);",(SEED,N_empleados))
        resultado=cur.fetchone()[0]
      # Confirmar cambios
        conn.commit()
      # Cerrar conexión
        cur.close()
        conn.close()
        if resultado==1:
            print("CARGA EXITOSA!!")
        elif resultado==0:
            print("CARGA FALLIDA!!")
        return resultado
  except psycopg2.Error as e:
        print("Error desde PostgreSQL:", e.pgerror)
        print("Código SQLSTATE:", e.pgcode)
        return e.pgerror


def cargar_puestos_hash(SEED,N_puestos):
  try:
        with open("CREDENCIALES_QA.json") as f:
            params = json.load(f)
        params= dict(list(params.items())[:5])
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("select fn_agregar_puestos_hash(%s,%s);",(SEED,N_puestos))
        resultado=cur.fetchone()[0]
      # Confirmar cambios
        conn.commit()
      # Cerrar conexión
        cur.close()
        conn.close()
        if resultado==1:
            print("CARGA EXITOSA!!")
        elif resultado==0:
            print("CARGA FALLIDA!!")
        return resultado
  except psycopg2.Error as e:
        print("Error desde PostgreSQL:", e.pgerror)
        print("Código SQLSTATE:", e.pgcode)
        return e.pgerror


def cargar_empleados_enmascarar(SEED, N_empleados):
  try:
        with open("CREDENCIALES_QA.json") as f:
          params = json.load(f)
        params= dict(list(params.items())[:5])
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("SELECT fn_agregar_empleados_enmascarar(%s::float,%s::int)",(SEED,N_empleados))
        resultado=cur.fetchone()[0]
      # Confirmar cambios
        conn.commit()
      # Cerrar conexión
        cur.close()
        conn.close()
        if resultado==1:
            print("CARGA EXITOSA!!")
        elif resultado==0:
            print("CARGA FALLIDA!!")
        return resultado
  except psycopg2.Error as e:
        print("Error desde PostgreSQL:", e.pgerror)
        print("Código SQLSTATE:", e.pgcode)
        return e.pgerror

def Limpiar_QA():
  try:
        with open("CREDENCIALES_QA.json") as f:
          params = json.load(f)
        params= dict(list(params.items())[:5])
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("SELECT fn_limpiartablas();")
        resultado=cur.fetchone()[0]
      # Confirmar cambios
        conn.commit()
      # Cerrar conexión
        cur.close()
        conn.close()
        if resultado==1:
            print("EXITO!!")
        elif resultado==0:
            print("Limpieza FALLIDA!!")
        return resultado
  except psycopg2.Error as e:
        print("Error desde PostgreSQL:", e.pgerror)
        print("Código SQLSTATE:", e.pgcode)
        return e.pgerror
def Limpiar_TP():
  try:
        with open("CREDENCIALES_QA.json") as f:
          params = json.load(f)
        params= dict(list(params.items())[:5])
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("SELECT fn_Limpiartp();")
        resultado=cur.fetchone()[0]
      # Confirmar cambios
        conn.commit()
      # Cerrar conexión
        cur.close()
        conn.close()
        if resultado==1:
            print("EXITO!!")
        elif resultado==0:
            print("Limpieza FALLIDA!!")
        return resultado
  except psycopg2.Error as e:
        print("Error desde PostgreSQL:", e.pgerror)
        print("Código SQLSTATE:", e.pgcode)
        return e.pgerror
def ContarNumeroDatos():
  try:
        with open("CREDENCIALES_QA.json") as f:
          params = json.load(f)
        params= dict(list(params.items())[:5])
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        cur.execute("SELECT * FROM fn_contar();")
        res=cur.fetchone()

        empleados = res[0]
        puestos   = res[1]
        jefes     = res[2]

      # Confirmar cambios
        conn.commit()
      # Cerrar conexión
        cur.close()
        conn.close()
        return empleados,puestos,jefes
  except psycopg2.Error as e:
        print("Error desde PostgreSQL:", e.pgerror)
        print("Código SQLSTATE:", e.pgcode)
        return 0,0,'0'
        