from src.autoGit import commitPush
import pytest

@pytest.mark.correctCommit
def test_commitPush():
    assert commitPush("Commit test correct") == True

@pytest.mark.IncorrectCommit
def test_commitPush():
    assert commitPush("") == False