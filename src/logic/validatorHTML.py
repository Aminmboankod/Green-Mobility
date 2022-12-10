# Función que valida que el contenido de los archivos HTML sean una estructura HTML

def validatorHTML(file):

    if file.startswith('\n<!DOCTYPE html>'):
        print('La estructura del HTML es correcta')
        return True
    else:
        print('La estructura HTML no es correcta>')
        return False


