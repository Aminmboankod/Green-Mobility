import os

def createHTML(filename, content, directory, path):

    if os.path.isdir(directory) == True:

        with open(path, "w+") as htmlFile:
            htmlFile.write(content)
            status = filename + " has been created in " + directory
            print(status)
        return status

    else:
        print("directory doesn't exist")
        
