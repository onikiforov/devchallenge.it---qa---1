# -*- coding: utf-8 -*-
import unittest
from tests.base_tc_class import BaseApi
import utils
import req
import config


class TestUploadImage(BaseApi):
    def test_upload_pet_image(self):
        pet_name = 'DoGz'
        pet = utils.create_pet_object(pet_name)

        response = req.add_new_pet(pet)
        self.assert_status(200, response)
        self.assertEqual(pet_name, response.json()['name'])
        self.assertIsNotNone(response.json()['id'])

        pet_id = response.json()['id']

        upload_image_response = req.upload_image(pet_id,
                                                 image_file_path=config.image_file_path,
                                                 image_file_name=config.image_file_name,
                                                 additional_metadata='Some test data'
                                                 )

        self.assert_status(200, response)
        self.assertEquals(200, upload_image_response.json()['code'])


if __name__ == '__main__':
    unittest.main()
