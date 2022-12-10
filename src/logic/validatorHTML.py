from bs4 import BeautifulSoup

# Función que valida que el contenido de los archivos HTML sean una estructura HTML

def validatorHTML(file):

    try:
        soup = BeautifulSoup(file, 'html.parser')
        return True
    except:
        return False

