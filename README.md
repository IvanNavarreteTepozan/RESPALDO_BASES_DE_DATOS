#README:
Requisitos:

  -sistema operatvo windows
  - tener instalado python 3.11.9
  - se recomienda tener pgAdmin 4 como interfaz grafica para a Base de datos
  -Ademas de descargar los modulos mencionados en el documento requirement.txt en esta carpeta, si no los tiene  ejecute cada una de las siguientes lineas en su CMD
    pip install Faker
    pip install pandas
    pip intall psycopg2


NOTA: no es necesario que cargue un respaldo, nuestro servidor con las bases de datos de PRODUCCION y DESARROLLO se encuentra alojada en un servidor de AWS
basta con conectarse a un nuevo servidor desde pgAdmin4 con los sigueintes parámetros:

CONEXIÓN CON BASE DE DATOS DESDE PgAdmin4: 
  "dbname": DESARROLLO,
  "user": postgres,
  "password": 12IvNavExp,
  "host": proyectoabd.cha0oqy6crlg.us-east-2.rds.amazonaws.com
  "port": 5432

Estos datos ya vienen por   defecto en el archivo CREDENCIALES_QA.json, archivo el cua le servira como acceso a la base y al sistema desde python

Una vez conectado con la base de datos, instalado python y sus respectivos modulos, descargue los archivos del proyecto en una sola carpeta
de click sobre interfaz.py y ejecute con python:

DENTRO DE LA INTERFAZ:
  Debera ver  las siguientes opciones:
    1. TAB_EMPLEADO
    2. TAB_PUESTO
    3. TAB_JEFESDEPARTAMENTO
    4. Configurar Metodos y tablas para autoguardado diario
    0. Salir
donde podra elejir entre nuestras 3 tablas para modificar, cada una tendra sus respectivos metodos de enmascaramiento o generacion de datos
donde podra elegir la cantidad de datos o cargar la información  mas reciente de poducción con enmascaramiento

el punto 4 corresponde al guardado diario de los datos, donde configura como quiere que se guarden los datos en cada tabla, este respaldo diario
copia la estructura de producción a diario, para mantener la informacion actualizada.

todos los cambios se veran guardados en una bitacora en el servidor de DESARROLLO.

consideraciones para aunto-ejecución de guardado diario:
 Programar tu script en Windows a 
1. 	Abre el Programador de tareas
• 	Presiona windows + R escribe taskschd.msc y dale Enter.
2. 	Crea una nueva tarea básica
• 	En el panel derecho, selecciona Crear tarea básica.
• 	Ponle un nombre
3. 	Configura el disparador (Trigger)
• 	Elige Diariamente.
• 	Pon la hora.
• 	Asegúrate de que se repita todos los días.
4. 	Configura la acción (Action)
• 	Selecciona Iniciar un programa.
• 	En Programa/script, pon la ruta del ejecutable de python.
• 	En Agregar Argumentos, pon la ruta del archivo CARGA.py






  
