import os 
import subprocess

#cambiar al directorio del repositorio
os.chdir('/Escritorio/Reto/Green-Mobility/')

#funcion para hacer un commit
def commit(message):                               
    #hacer add de los archivos
    subprocess.call('git add .', shell=True)

    #hacer commit
    subprocess.call('git commit -m "' + message + '"', shell=True)

#funcion para pushear al repositorio remoto
def push():
    #hacer push
    subprocess.call('git push', shell=True)

