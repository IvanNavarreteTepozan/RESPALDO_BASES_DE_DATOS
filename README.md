\#README:
Requisitos:

-Sistema operatvo Windows



-Tener instalado python 3.11.9

&nbsp;	Descarga:

&nbsp;		https://www.python.org/downloads/



-Se recomienda tener pgAdmin 4 como interfaz grafica para a Base de datos

&nbsp;	Descaga:

&nbsp;		https://www.postgresql.org/ftp/pgadmin/pgadmin4/v9.11/windows/


-Además de descargar los módulos mencionados en el documento requirement.txt de esta carpeta, si no los tiene  ejecute cada una de las siguientes líneas en su CMD una vez que haya instalado Python 3.11


pip install Faker
pip install pandas
pip intall psycopg2





DESCOMPRIMA EL ARCHIVO PROYECTO.RAR, y coloque todos sus archivos en una misma carpeta, este contiene

los ejecutables para poder ejecutar las tareas.



NOTA: no es necesario que cargue un respaldo, nuestro servidor con las bases de datos de PRODUCCION y DESARROLLO se encuentra alojada en un servidor de AWS
basta con conectarse a un nuevo servidor desde pgAdmin4 con los siguientes parámetros:

CONEXIÓN CON BASE DE DATOS DESDE PgAdmin4:


"dbname": DESARROLLO,
"user": postgres,
"password": 12IvNavExp,
"host": proyectoabd.cha0oqy6crlg.us-east-2.rds.amazonaws.com
"port": 5432





Estos datos ya vienen por   defecto en el archivo CREDENCIALES\_QA.json, archivo el cual le servirá como acceso a la base y al sistema desde Python, y necesariamente debe estar en la misma carpeta del código, de lo contrario

no podrá usar el código.





LA INTERFAZ para el proyecto esta en el archivo  interfaz.py.



Una vez conectado con la base de datos, instalado python y sus respectivos módulos, descargue los archivos del proyecto en una sola carpeta de click sobre interfaz.py y ejecute con python:



DENTRO DE LA INTERFAZ:
Deberá ver  las siguientes opciones:
1. TAB\_EMPLEADO
2. TAB\_PUESTO
3. TAB\_JEFESDEPARTAMENTO
4. Configurar Métodos y tablas para autoguardado diario
0. Salir
donde podrá elegir entre nuestras 3 tablas para modificar, cada una tendrá sus respectivos métodos de enmascaramiento o generación de datos
donde podrá elegir la cantidad de datos o cargar la información  mas reciente de producción con enmascaramiento

el punto 4 corresponde al guardado diario de los datos, donde configura como quiere que se guarden los datos en cada tabla, este respaldo diario
copia la estructura de producción a diario, para mantener la información actualizada.

todos los cambios se verán guardados en una bitácora en el servidor de DESARROLLO.

consideraciones para auto-ejecución de guardado diario:
Programar tu script en Windows a

1. Abre el Programador de tareas
   • 	Presiona windows + R escribe taskschd.msc y dale Enter.
2. Crea una nueva tarea básica
   • 	En el panel derecho, selecciona Crear tarea básica.
   • 	Ponle un nombre
3. Configura el disparador (Trigger)
   • 	Elige Diariamente.
   • 	Pon la hora.
   • 	Asegúrate de que se repita todos los días.
4. Configura la acción (Action)
   • 	Selecciona Iniciar un programa.
   • 	En Programa/script, pon la ruta del ejecutable de python.
   • 	En Agregar Argumentos, pon la ruta del archivo CARGA.py
