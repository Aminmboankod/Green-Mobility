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

## Descripción técnica

### Arquitectura de la aplicación

![DiagramaArquitectura](poner enlace)

- **Data Layer:** 
    - /db es el directorio en el cual se encuentras todos los módulos que se encargan de hacer consultas especificas a la base de datos.

- **Business Layer:**
    - /logic es el directorio en el cual se encuentran todos los módulos que componen la lógica del programa y se encargan de transformar los achivos JSON que nos da la base de datos a archivos HTML.

- **Service Layer:**
    - /docs es el directorio en el cual se encuentran los archcivos que ha generado Python automáticamente y organizados para tener un estructura para posteriormente poder indexar.

-**Presentation Layer:**
    - Github pages es el servidor que usamos para alojar nuestra página web y donde el usuario interactua.

### Diseño 

![Diagrama](https://live.staticflickr.com/65535/52556747464_22f90d5ac2_t.jpg)

