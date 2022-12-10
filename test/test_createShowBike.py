from src.logic.createShowBike import createShowBike
import pytest

@pytest.mark.completedBike
def test_createShowBike():

    listOfDictionaryBikes = {
  "_id": {
    "$oid": "637679dc5bcb87a948741730"
  },
  "name": "Commuter 5 WMN",
  "category": "City",
  "brand": "Canyon",
  "material": "Aluminum",
  "frame_size": "XL",
  "weight": {
    "$numberDecimal": "11.31"
  },
  "set_group": {
    "set_group_brand": "Shimano MT200",
    "group_type": "Electronic",
    "speed": 11
  },
  "location": {
    "ZIP": "07001",
    "street": "Calle Del Conquistador",
    "number": 21
  },
  "company": {
    "company_id": "C56317506",
    "company_name": "Bike Palma"
  },
  "available": False,
  "price": {
    "$numberDecimal": "20"
  },
  "image": "https://live.staticflickr.com/65535/52533656786_81e5d845a9_n.jpg"
}

    assert  createShowBike(listOfDictionaryBikes) == True
    
@pytest.mark.incompletedBike
def test_createShowBike():

    listOfDictionaryBikes = [{
  "_id": {
    "$oid": "637679dc5bcb87a948741730"
  },
  "category": "City",
  "brand": "Canyon",
  "material": "Aluminum",
  "weight": {
    "$numberDecimal": "11.31"
  },
  "set_group": {
    "set_group_brand": "Shimano MT200",
    "group_type": "Electronic",
    "speed": 11
  },
  "location": {
    "ZIP": "07001",
    "street": "Calle Del Conquistador",
    "number": 21
  },
  "company": {
    "company_id": "C56317506",
    "company_name": "Bike Palma"
  },
  "available": False,
  "price": {
    "$numberDecimal": "20"
  },
  "image": "https://live.staticflickr.com/65535/52533656786_81e5d845a9_n.jpg"
},
{
  "_id": {
    "$oid": "637679dc5bcb87a948741730"
  },
  "category": "City",
  "brand": "Canyon",
  "material": "Aluminum",
  "weight": {
    "$numberDecimal": "11.31"
  },
  "set_group": {
    "set_group_brand": "Shimano MT200",
    "group_type": "Electronic",
    "speed": 11
  },
  "location": {
    "ZIP": "07001",
    "street": "Calle Del Conquistador",
    "number": 21
  },
  "company": {
    "company_id": "C56317506",
    "company_name": "Bike Palma"
  },
  "available": False,
  "price": {
    "$numberDecimal": "20"
  },
  "image": "https://live.staticflickr.com/65535/52533656786_81e5d845a9_n.jpg"
}]


    assert  createShowBike(listOfDictionaryBikes) == False
    

