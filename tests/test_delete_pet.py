# -*- coding: utf-8 -*-
import unittest
from tests.base_tc_class import BaseApi
import utils
import req


class TestDeletePet(BaseApi):
    def test_create_and_delete_pet(self):
        initial_pet_name = 'DoGz'

        pet = utils.create_pet_object(initial_pet_name)

        response = req.add_new_pet(pet)
        self.assert_status(200, response)
        self.assertEqual(initial_pet_name, response.json()['name'])
        self.assertIsNotNone(response.json()['id'])

        pet_id = response.json()['id']

        delete_response = req.delete_pet(pet_id)
        self.assert_status(200, delete_response)

        check_response = req.find_pet_by_id(pet_id)
        self.assert_status(404, check_response)
        self.assertEqual(1, check_response.json()['code'])


if __name__ == '__main__':
    unittest.main()
