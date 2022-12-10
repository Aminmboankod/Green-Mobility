from src.logic.validatorHTML import validatorHTML
import pytest

@pytest.mark.correctHTML
def test_validatorHTML():
    assert validatorHTML("<!DOCTYPE html>") == True

@pytest.mark.incorrectHTML
def test_validatorHTML():
    assert validatorHTML("Hola mundo") == False