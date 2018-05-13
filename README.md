# devchallenge.it---qa---1

Solution for dev challenge 12 qa task.

Written in Python. Tested with python 2.7 and python 3.6.3.

### Dependencies: 
* requests
* pytest

### To install dependencies:
#### for python 2:
* `pip install requests`
* `pip install pytest`

#### for python 3:
* `pip3 install requests`
* `pip3 install pytest`

### To run tests:
* cd into project folder
* run `python -m pytest`

If you have both python 2 and python 3 installed and want to run tests with python 3, use command `python3 -m pytest`

### Project structure:
```
+-- config.py - file with constants used in project, like server url and api version
+-- utils.py - file with utility methods that are used in tests
+-- req.py - file with request methods
+-- tests/
  +-- base_tc_class.py - basic class inherited from unittest.TestCase. Other test classes inherits from this class
  +-- test_add_new_pet.py - test for adding new pet.
  +-- test_change_pet_name.py - test for changing pet name
  +-- test_create_delete_update_pet.py - negative test that checks for updating deleted pet
  +-- test_delete_pet.py - test for deleting fo pet
  +-- test_find_order.py - tests for /order endpoint
  +-- test_upload_image.py - test for image uploading
```

### Tests description:
Due to inability of DB access, tests are not atomic. 
For example after new pet is created I need to send request to get pet info by id to make sure that it actually exists.

* `test_add_new_pet` - sends request to create new pet, then sends request to get pet by id. Contains assertions for both requests.
* `test_change_pet_name` - sends request to create new pet (because we have to make sure that pet exists before changing it's name), next sends request to update pet object and finally sends request to get pet by id to make sure changes were made. Contains assertions for all requests.
* `test_create_delete_update_pet` - Negative test for "/pet" endpoint. Sends request to create new pet, next sends request to delete it and finally sends request to update deleted pet. Contains assertions for all requests.
* `test_delete_pet` - sends request to create new pet, next sends request to delete it and finally sends request to get pet by id to check that such pet doesn't exist anymore. Contains assertions for all requests.
* `test_find_order` - Tests for "/store" endpoint. First gets info for existing order, second tries to get info for not existing order. Contains assertions for all requests.
* `test_upload_image` - Additional test. Uploads an image for pet.
