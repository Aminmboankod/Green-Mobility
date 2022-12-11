## GREEN MOBILITY 

Green Mobility es una propuesta desarrollada por Antonio Maroto y Amin Mustafa como alumnos del Instituto Francesc de Borja Moll presentada para el proyecto de fin de trimestre de el Grado Superior de Desarrollo Web Intensivo. 

---
### Indice 

- Introducción
- Manual
    - Requisitos
    - Instalación
- Metodología
- Desarollo
- Descripción técnica
- Diseño
- Tecnologías
- Pruebas
    - pytest
    - Coverage
- Diagrama del tiempo invertido
- Conclusiones
    - Mejoras
    - Dificultades

---

## Introducción

Green Mobility surge de la necesidad del Gobierno de las Islas Baleares de hacer frente al problema de la saturación de coches, sobretodo en temporada alta. 

Para llevar a cabo este proyecto utilizaremos MongoDB como base de datos a través de un servicio llamado Mongo Atlas. La lógica del programa se desarolla mediante Python(3.8.10).

Para la conversión y creación del sitio web estático utilizaremos Github pages.

---

## Manual

### Pre-requisitos

+ Python3
+ pip3
+ Git

---

### Instalación

Es muy recomendable realizar la instalación de todas las dependencias del programa en un entorno virtual.
Para llevar a cabo la instalación en **Linux** ejecuta los siguientes comandos:

~~~
$ sudo apt-get install python3-venv
~~~

Crea un directorio y sitúate dentro de él. Es importante crearlo pues aquí dentro se almacenará todo el código de la aplicación.

~~~
$ mkdir GreenMobility
$ cd GreenMobility
~~~

Una vez dentro del directorio clonamos el repositorio de Github.

~~~
$ git clone https://github.com/Aminmboankod/Green-Mobility.git
~~~

Se ha preparado un archivo 'setup' para descargar las dependencias necesarias. Para ejecutarlo hay que usar el comando:

~~~
$ ./setup.sh
~~~

Para activar el entorno virtual ejecuta el siguiente comando:

~~~
$ source venv/bin/activate
~~~

Para comprobar que todas las dependencias se han instalado y ver sus versiones usamos el siguiente comando:

~~~
pip3 list
~~~

---

## Desarollo

Para llevar a cabo el desarollo del programa hemos pasado por diferentes fases:

1. **MongoDB** 

El primer paso de todos fue crear una base de datos no relacional mediante MongoDB. En la base de datos almacenamos los datos de las bicicletas, usuarios y los registros del alquiler de bicicletas.

2. **Python** 

Una vez tenemos la base de datos con una buena cantidad de bicicletas almacenadas utilizamos python para diseñar el porgrama que se encarga de crear automáticamente los archivos HTML con los datos correspondientes para cada bicicleta.

3. **HTML/CSS** 

Cuando ya tenemos creados los archivos HTML que ha generado Python es hora de aplicar estilos mediante CSS.

4. **Github Pages** 

EL último paso fue utilizar github pages para indexar nuestra página web y pueda ser visitada por todo el mundo.

---

## Descripción técnica

### Arquitectura de la aplicación

![DiagramaArquitectura](/images/Arquitectura.png)

- **Data Layer:** 
    - /db es el directorio en el cual se encuentras todos los módulos que se encargan de hacer consultas especificas a la base de datos.

- **Business Layer:**
    - /logic es el directorio en el cual se encuentran todos los módulos que componen la lógica del programa y se encargan de transformar los achivos JSON que nos da la base de datos a archivos HTML.

- **Service Layer:**
    - /docs es el directorio en el cual se encuentran los archcivos que ha generado Python automáticamente y organizados para tener un estructura para posteriormente poder indexar.

- **Presentation Layer:**
    - Github pages es el servidor que usamos para alojar nuestra página web y donde el usuario interactua.

### Tecnologias usadas

- **Python:** 
    - Requests es una librería HTTP para Python usada para efectuar peticiones HTTP y hacerlas más amigables.
    - Time es una libreria que nos permite establecer tiempos de espera entre cada mensaje que sale por pantalla.
    - Subprocess es una libreria que nos permite generar nuevos procesos e interactuar con la consola.
    - JSON es una libreria que nos tratar con archivos JSON.
    - os es una libreria que nos permite interactuar con los directorios de nuestro sistema.

- **MongoDB:**
    - DataAPI Nos permite la comunicación entre dos aplicaciones, en nuestro caso Python y MongoDB.

- **Git:**
    - Realización de cambios y subida de versiones modificadas independientes, no sobrescribiendo en el archivo original.
    - Github Pages servicio empleado para la creación de sitios webs estáticos.

- **HTML/CSS:**
    - Dar diseño a la página web.

## Diseño 

![Diagrama](/images/Diagrama.png)

- **mainLogic:** Es el programa principal y se encarga de ejecutar la lógica de todos los módulos necesarios para el transcurso del programa. Se encuentra en el directorio raiz.

- **db:** Es un paquete que cotiene el programa principal que realiza el CRUD a la base de datos. Además contiene la carpeta /CRUD en la que se encuentran todos los módulos que dependientes de mainCrud.

- **logic:** Es un paquete que contiene todos los módulos que se encargan de la lógica que crea archivos HTML a partir de los datos obtenidos mediante mainCrud.

- **adminProgram:** Es un módulo que permite al usuario añadir, borrar, actualizar, y ver datos de bicicletas.

- **autoGit:** Es un módulo con la lógica para automatizar Git.

---

## Esquema de la Base de Datos

~~~
{
  "_id": {
    "$oid": "63765c8d5bcb87a948741718"
  },
  "name": "String",
  "category": "String",
  "brand": "String",
  "material": "String",
  "frame_size": "String",
  "weight": {
    "$numberDecimal": "Decimal"
  },
  "set_group": {
    "set_group_brand": "String",
    "group_type": "String",
    "speed": Int
  },
  "location": {
    "ZIP": "String",
    "street": "String",
    "number": Int
  },
  "company": {
    "company_id": "String",
    "company_name": "String"
  },
  "available": true,
  "price": {
    "$numberDecimal": "String"
  },
  "image": "String"
}
~~~





