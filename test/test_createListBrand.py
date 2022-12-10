from src.logic.createListBrand import listofBikesForBrand
import pytest

@pytest.mark.correctList
def listofBikesForBrand(listOfDictionaryBikes):

    listsOfBrands = [{"_id": "Cube", "_id": "Canyon", "_id": "Bianchi", "_id": "Cannodale", "_id":"Giant","_id":"BH"}]

    assert listofBikesForBrand(listOfDictionaryBikes, listsOfBrands) == True

@pytest.mark.incorrectList
def listofBikesForBrand(listOfDictionaryBikes):

    listsOfBrands = [{"_id": "Alpino", "_id": "Motorola", "_id": "Bianchi", "_id": "Hacendado", "_id":"Nvidia","_id":"123"}]

    assert listofBikesForBrand(listOfDictionaryBikes, listsOfBrands) == False