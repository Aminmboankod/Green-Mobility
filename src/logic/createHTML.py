def createHTML(filename, content, directory, path):


    with open(path, "w+") as htmlFile:
        htmlFile.write(content)
        status = filename + " has been created in " + directory
        print(status)
    return status

    

