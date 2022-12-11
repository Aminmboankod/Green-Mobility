from src.logic.createHTML import createFile
import pytest
import os

@pytest.mark.existsFileInPath
def test_createHTML():
    assert createFile("prueba.html", "prueba", "docs/", "docs/prueba.html") == True
    assert createFile("prueba.html", "prueba", "FERRARI/", "FERRARI/prueba.html") == False

