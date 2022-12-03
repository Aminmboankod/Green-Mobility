def createHTML(filename, content, directory, path):

    assert isinstance(filename, str), "filename no es un string"
    assert isinstance(content, str)
    assert isinstance(directory, str)
    assert isinstance(path, str)

    with open(path, "w+") as htmlFile:
        htmlFile.write(content)
    print(filename + " has been created in " + directory)