## GREEN MOBILITY 

Green Mobility es una propuesta desarrollada por Antonio Maroto y Amin Mustafa como alumnos del Instituto Francesc de Borja Moll presentada para el proyecto de fin de trimestre de el Grado Superior de Desarrollo Web Intensivo. 

---
### Indice 

- Introducción
- Manual
    - Requisitos
    - Instalación
    - Uso
- Metodología
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
$ mkdir ./GreenMobility-library
$ cd GreenMobility-library

~~~
Una vez dentro del directorio clonamos el repositorio de Github.
~~~
$ git clone https://github.com/Aminmboankod/Green-Mobility.git
~~~

Se ha preparado un archivo 'setup' para descargar las dependencias necesarias. Para ejecutarlo hay que usar el comando:

~~~
$ python3 setup.py
~~~

Para activar el entorno virtual ejecuta el siguiente comando:

~~~
$ source venv/bin/activate
~~~
