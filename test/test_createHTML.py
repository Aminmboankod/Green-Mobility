from src.logic.createHTML import createFile
import pytest
import os

@pytest.mark.createHTML
def test_createHTML():
    assert createFile("prueba.html", "prueba", "docs/", "docs/prueba.html") == "prueba.html has been created in docs/"

@pytest.mark.errorContentHTML
def test_createHTML():
    assert createFile("prueba.html", 1, "docs/", "docs/prueba.html") == None

@pytest.mark.errorPath
def test_createHTML():
    assert createFile("prueba.html","prueba","prueba/", "prueba/prueba.html") == "Directory doesn't exist"

@pytest.mark.existsFileInPath
def test_createHTML():
    assert os.path.exists("docs/index.html") == True

