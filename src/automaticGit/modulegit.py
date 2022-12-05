from git import Repo

# Ruta de la carpeta donde se encuentra el repositorio
repo = Repo("reto/Gree-Mobility")

# Agregar todos los archivos
repo.git.add(u=True)

# Realizar un nuevo commit
repo.git.commit(m='Nuevo commit de actualización')

# Empujar el código al repositorio remoto
repo.git.push()