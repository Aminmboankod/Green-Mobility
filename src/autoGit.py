import os 
import subprocess


#funcion para hacer un commit
def commitPush(message):  
    #hacer pull
    subprocess.call('git pull', shell=True)

    #hacer add de los archivos
    subprocess.call('git add .', shell=True)
    if message != "":
        #hacer commit
        subprocess.call('git commit -m "' + message + '"', shell=True)

        #hacer push
        subprocess.call('git push', shell=True)
        return True
    else:
        return False
