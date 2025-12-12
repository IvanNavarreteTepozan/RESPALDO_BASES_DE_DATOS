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
de click sobre interfaz.py y deberia de ejecutarse sin problemas:

DENTRO DE LA INTERFAZ:
  debera ver 
