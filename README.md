## GREEN MOBILITY 

Green Mobility es una propuesta desarrollada por Antonio Maroto y Amin Mustafa como alumnos del Instituto Francesc de Borja Moll presentada para el proyecto de fin de trimestre del Grado Superior de Desarrollo de aplicaciones Web Intensivo.

---
### Índice 

- [Introducción](#introduccion)
- [Manual](#manual)
    - [Requisitos](#requisitos)
    - [Instalación](#instalacion)
- [Desarrollo](#desarrollo)
- [Descripción técnica](#descripción-técnica)
  - [Arquitectura de la aplicación](#arquitectura-de-la-aplicación)
  - [Tecnologías usadas](#tecnlogias-usadas)
- [Diseño](#diseño)
  - [Componentes](#componentes)
- [Metodología](#metodología)
  - [OCP](#ocp)
  - [SRP](#srp)
- [Pruebas](#pruebas)
    - [Pytest](#pytest)
    - [Coverage](#coverage)
- [Diagrama del tiempo invertido](#diagrama-del-tiempo-invertido)
- [Conclusiones](#conclusiones)
    - [Mejoras](#mejoras)
    - [Dificultades](#dificultades)

---

## Introducción

Green Mobility surge como solución al problema que propone el "Product Owner" de la empresa. El contexto simulado es cubrir la necesidad del Gobierno de las Islas Baleares de hacer frente al problema de la saturación de coches, sobre todo en temporada alta. 

Como solución al problema, se propone un agregador/buscador de bicicletas de toda las disponibles para alquiler. Dando opción a que cualquier empresa pueda agregar los datos de su bicicleta y aparezca disponible en una web pública. 

De este modo, el usuario puede acceder a todo el stock de bicis disponibles desde una sola aplicación/web y alquilarlas de una forma muy sencilla.

Para llevar a cabo este proyecto utilizaremos MongoDB como base de datos a través de un servicio llamado Mongo Atlas. 

La lógica del programa se desarrolla mediante Python(3.8.10).

Para la conversión y creación del sitio web estático utilizaremos Github pages.

---

## Manual

### Requisitos

Para poder comenzar a poner en funcionamiento el programa debes tener como requisitos mínimos los siguientes:

+ Python3
+ pip3
+ Git
+ Linux
+ Clúster en MongoDB (en su defecto, pedirnos los datos de acceso al cluster, APIKEY y URL de conexión)

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

## Desarrollo

Para llevar a cabo el desarrollo del programa hemos pasado por diferentes fases:

1. **MongoDB** 

El primer paso fue crear una base de datos no relacional mediante MongoDB. En la base de datos almacenamos los datos de las bicicletas, usuarios y los registros del alquiler de bicicletas.

Hemos usado MongoDB porque dado que los datos de cada bicicleta pueden variar según sus características, necesitabamos usar una base de datos no relacional. Para ello y teniendo en cuenta que usaremos Python para desarrollarlo, Mongo es la mejor opción.

2. **Python** 

Una vez tenemos la base de datos con una buena cantidad de bicicletas almacenadas utilizamos python para diseñar el programa que se encarga de crear automáticamente los archivos HTML con los datos correspondientes para cada bicicleta.

Python es un lenguaje de programación de alto nivel que nos permite aprender a programar con más facilidad en esta fase inicial de aprendizaje.

3. **HTML/CSS** 

Cuando ya tenemos creados los archivos HTML que ha generado Python es hora de aplicar estilos mediante CSS.

4. **Github Pages** 

El último paso ha sido utilizar github pages para indexar nuestra página web y pueda ser visitada por todo el mundo.

---

## Descripción técnica

### Arquitectura de la aplicación

![DiagramaArquitectura](/images/Arquitectura.png)

- **Data Layer:** 
    - /db es el directorio en el cual se encuentran todos los módulos que se encargan de hacer consultas específicas a la base de datos.

- **Business Layer:**
    - /logic es el directorio en el cual se encuentran todos los módulos que componen la lógica del programa y se encargan de transformar los achivos JSON que nos da la base de datos a archivos HTML.

- **Service Layer:**
    - /docs es el directorio en el cual se encuentran los archcivos que ha generado Python automáticamente y organizados para tener una estructura para posteriormente poder indexar.

- **Presentation Layer:**
    - Github pages es el servidor que usamos para alojar nuestra página web y donde el usuario interactúa.

### Tecnologías usadas

- **Python:** 
    - Requests es una librería HTTP para Python usada para efectuar peticiones HTTP y hacerlas más amigables.
    - Time es una librería que nos permite establecer tiempos de espera entre cada mensaje que sale por pantalla.
    - Subprocess es una librería que nos permite generar nuevos procesos e interactuar con la consola.
    - JSON es una librería que nos permite tratar con archivos JSON.
    - os es una librería que nos permite interactuar con los directorios de nuestro sistema.

- **MongoDB:**
    - DataAPI Nos permite la comunicación entre dos aplicaciones, en nuestro caso Python y MongoDB.

- **Git:**
    - Realización de cambios y subida de versiones modificadas independientes, no sobrescribiendo en el archivo original.
    - Github Pages servicio empleado para la creación de sitios webs estáticos.

- **HTML/CSS:**
    - Dar diseño a la página web.

---

## Diseño 

![Diagrama](/images/Diagrama.png)

### Componentes

- **mainLogic:** Es el programa principal y se encarga de ejecutar la lógica de todos los módulos necesarios para el transcurso del programa. Se encuentra en el directorio raíz.

- **db:** Es un paquete que cotiene el programa principal que realiza el CRUD a la base de datos. Además, contiene la carpeta /CRUD en la que se encuentran todos los módulos que dependientes de mainCrud.

- **logic:** Es un paquete que contiene todos los módulos que se encargan de la lógica que crea archivos HTML a partir de los datos obtenidos mediante mainCrud.

- **adminProgram:** Es un módulo que permite al usuario añadir, borrar, actualizar, y ver datos de bicicletas.

- **autoGit:** Es un módulo con la lógica para automatizar Git.

---

## Metodología

A la hora de realizar el proyecto utilizamos el Open Closed Principle (OCP) y Single Responsibility Principle (SRP).

### OCP

Todos los módulos del proyecto están diseñados pensando en la metodología OCP. Creemos que es una metodología más eficiente porque nos permite implementar más funciones sin tener que modificar el código. 

### SRP

Para garantizar una buena implementación OCP, control del código y encapsular las responsabilidades de cada módulo hemos desarrollado el proyecto teniendo siempre en cuenta el SRP por ello, los módulos están divididos por ficheros que están en directorios diseñados para una capa del programa, esto permite mayor control y conocimiento de las responsabilidades de cada módulo.

---

## Pruebas

### Pytest

![pytest](/images/pytest.png)

Podemos observar como el programa pasa exitosamente todos los casos test.

### Coverage

![coverage](/images/coverage.png)

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
---

## Diagrama del tiempo invertido

![diagramaTiempo](/images/clockify.png)

Para tener bajo control el tiempo utilizado y para poder comparar nuestras estimaciones hemos usado la herramienta Clockify con las siguientes etiquetas:

Para llevar un control del tiempo invertido en el desarrollo del proyecto hemos utilizado la herramienta de [Clockify](https://clockify.me/es/) con las siguientes etiquetas:

- Test: Tiempo invertido en la creación de los casos test.
- HTML: Tiempo invertido para diseñar las plantillas.
- BBDD: Tiempo invertido en averiguar como conectar Python con la base de datos y recolectar todas las bicicletas.
- Python: Tiempo invertido en desarrollar la lógica del proyecto.
- CSS: Tiempo invertido en aplicar estilos a la página web.


---

## Conclusiones

### Mejoras

En el apartado de mejoras nos gustaría:

- Implementar [**Typer**](https://typer.tiangolo.com/) para arrancar todo el programa desde la línea de comandos y poder realizar modificaciones.

- Añadir opciones más complejas al CRUD.

### Dificultades

Nos hemos topado con diferentes problemas en el desarrollo del proyecto.

- Los casos test: Encontrar los casos test para cada función que cubra todo el código y puedan cubrir casos reales de los usuarios se nos ha complicado y hemos ido experimentando en este proyecto.




