# Función que valida que el contenido de los archivos HTML sean una estructura HTML

def validatorHTML(file):

    if file.startswith('\n<!DOCTYPE html>'):
        print("\n" + 'The HTML structure is correct')
        return True
    else:
        print("\n" + 'The HTML structure is not correct')
        return False


