from src.logic.createHTML import createHTML
import pytest
import os


def test_createHTML():
    assert createHTML(filename="prueba.html", content="prueba", directory="docs/", path="docs/prueba.html") == "prueba.html has been created in docs/"

    
