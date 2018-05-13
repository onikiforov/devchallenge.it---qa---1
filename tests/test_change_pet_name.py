# -*- coding: utf-8 -*-
import unittest
from tests.base_tc_class import BaseApi
import utils
import req


class TestChangePetName(BaseApi):
    def test_create_and_change_pet_name(self):
        initial_pet_name = 'DoGz'
        updated_pet_name = 'new_dog'

        new_pet = utils.create_pet_object(initial_pet_name)

        response = req.add_new_pet(new_pet)
        self.assert_status(200, response)
        self.assertEqual(initial_pet_name, response.json()['name'])
        self.assertIsNotNone(response.json()['id'])

        initial_pet = response.json()

        updated_pet = initial_pet.copy()

        updated_pet['name'] = updated_pet_name
        updated_pet_id = updated_pet['id']

        response = req.update_pet(updated_pet)
        self.assert_status(200, response)
        self.assertEqual(updated_pet_name, response.json()['name'])
        self.assertEqual(updated_pet_id, response.json()['id'])

        check_response = req.find_pet_by_id(updated_pet_id)
        self.assert_status(200, response)
        self.assertEqual(updated_pet_name, check_response.json()['name'])
        self.assertEqual(updated_pet_id, check_response.json()['id'])


if __name__ == '__main__':
    unittest.main()
