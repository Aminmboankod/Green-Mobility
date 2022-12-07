import os

def deleteFiles():

    path = 'docs/pages/'
    for files in os.walk(path):
        for f in files:
            os.unlink(os.path.join(files, f))