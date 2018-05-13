# -*- coding: utf-8 -*-
import unittest
from tests.base_tc_class import BaseApi
import utils
import req


class TestAddNewPet(BaseApi):
    def test_add_new_pet(self):
        pet_name = 'DoGz'
        pet = utils.create_pet_object(pet_name)

        response = req.add_new_pet(pet)
        self.assert_status(200, response)
        self.assertEqual(pet_name, response.json()['name'])
        self.assertIsNotNone(response.json()['id'])

        pet_id = response.json()['id']

        check_response = req.find_pet_by_id(pet_id)
        self.assert_status(200, response)
        self.assertEqual(pet_name, check_response.json()['name'])
        self.assertEqual(pet_id, check_response.json()['id'])


if __name__ == '__main__':
    unittest.main()
