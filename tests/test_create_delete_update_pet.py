# -*- coding: utf-8 -*-
import unittest
from tests.base_tc_class import BaseApi
import utils
import req


class TestCreateDeleteUpdatePet(BaseApi):
    def test_create_delete_and_update_pet(self):
        initial_pet_name = 'DoGz'

        pet = utils.create_pet_object(initial_pet_name)

        response = req.add_new_pet(pet)
        self.assert_status(200, response)
        self.assertEqual(initial_pet_name, response.json()['name'])
        self.assertIsNotNone(response.json()['id'])

        pet_id = response.json()['id']

        delete_response = req.delete_pet(pet_id)
        self.assert_status(200, delete_response)

        update_response = req.update_pet_form_data(pet_id, pet_name='updated_name', pet_status='available')
        self.assert_status(404, update_response)


if __name__ == '__main__':
    unittest.main()
