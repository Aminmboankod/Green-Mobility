from src.logic.validatorHTML import validatorHTML
import pytest

@pytest.mark.correctHTML
def test_validatorHTML():
    assert validatorHTML("\n<!DOCTYPE html>") == True

@pytest.mark.incorrectHTML
def test_validatorHTML():
    assert validatorHTML("Hola mundo") == False
    assert validatorHTML("<ppp!DOCTYPE html>") == False