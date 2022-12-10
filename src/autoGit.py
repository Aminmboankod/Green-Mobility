import os 
import subprocess


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

commit("Commit de prueba para testear funcion Autogit")