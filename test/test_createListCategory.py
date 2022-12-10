from src.logic.createListcategory import listofBikesForCategory
import pytest

@pytest.mark.correctList
def test_listofBikesForCategory():
    listOfDictionaryBikes = [{
  "_id": {
    "$oid": "637f9abf9ab86906b4452783"
  },
  "name": "Bad Boy",
  "category": "City",
  "brand": "Cannondale",
  "material": "Aluminum",
  "frame_size": "M",
  "weight": {
    "$numberDecimal": "11.59"
  },
  "set_group": {
    "set_group_brand": "Shimano MT400 ",
    "group_type": "Electronic",
    "speed": 12
  },
  "location": {
    "ZIP": "07013",
    "street": "Calle Balanguera ",
    "number": 33
  },
  "company": {
    "company_id": "B80661085",
    "company_name": "Ride Mallorca"
  },
  "available": True,
  "price": {
    "$numberDecimal": "20"
  },
  "image": "https://live.staticflickr.com/65535/52534134125_83d11eacf7_n.jpg"
},
{
  "_id": {
    "$oid": "637f9abf9ab86906b4452783"
  },
  "name": "Bad Boy",
  "category": "City",
  "brand": "Cannondale",
  "material": "Aluminum",
  "frame_size": "M",
  "weight": {
    "$numberDecimal": "11.59"
  },
  "set_group": {
    "set_group_brand": "Shimano MT400 ",
    "group_type": "Electronic",
    "speed": 12
  },
  "location": {
    "ZIP": "07013",
    "street": "Calle Balanguera ",
    "number": 33
  },
  "company": {
    "company_id": "B80661085",
    "company_name": "Ride Mallorca"
  },
  "available": True,
  "price": {
    "$numberDecimal": "20"
  },
  "image": "https://live.staticflickr.com/65535/52534134125_83d11eacf7_n.jpg"
}]

    category = "City"

    assert listofBikesForCategory(listOfDictionaryBikes, category) == True

@pytest.mark.incorrectList
def test_listofBikesForBrand():
    listOfDictionaryBikes = [{
  "_id": {
    "$oid": "637f9abf9ab86906b4452783"
  },
  "name": "Bad Boy",
  "category": "City",
  "brand": "Cannondale",
  "material": "Aluminum",
  "frame_size": "M",
  "weight": {
    "$numberDecimal": "11.59"
  },
  "set_group": {
    "set_group_brand": "Shimano MT400 ",
    "group_type": "Electronic",
    "speed": 12
  },
  "location": {
    "ZIP": "07013",
    "street": "Calle Balanguera ",
    "number": 33
  },
  "company": {
    "company_id": "B80661085",
    "company_name": "Ride Mallorca"
  },
  "available": True,
  "image": "https://live.staticflickr.com/65535/52534134125_83d11eacf7_n.jpg"
},
{
  "_id": {
    "$oid": "637f9abf9ab86906b4452783"
  },
  "name": "Bad Boy",
  "category": "City",
  "brand": "Cannondale",
  "material": "Aluminum",
  "frame_size": "M",
  "weight": {
    "$numberDecimal": "11.59"
  },
  "set_group": {
    "set_group_brand": "Shimano MT400 ",
    "group_type": "Electronic",
    "speed": 12
  },
  "location": {
    "ZIP": "07013",
    "street": "Calle Balanguera ",
    "number": 33
  },
  "company": {
    "company_id": "B80661085",
    "company_name": "Ride Mallorca"
  },
  "available": True,
  "price": {
    "$numberDecimal": "20"
  },
  "image": "https://live.staticflickr.com/65535/52534134125_83d11eacf7_n.jpg"
}]


    category = 2

    assert listofBikesForCategory(listOfDictionaryBikes, category) == False