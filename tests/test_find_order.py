# -*- coding: utf-8 -*-
import unittest
from tests.base_tc_class import BaseApi
import req


class TestFindOrder(BaseApi):
    def test_find_existing_order(self):
        existing_order_id = 2

        response = req.get_store_order(existing_order_id)
        self.assert_status(200, response)
        self.assertEqual(existing_order_id, response.json()['id'])

    def test_find_not_existing_order(self):
        not_existing_order_id = 993767826382

        response = req.get_store_order(not_existing_order_id)
        self.assert_status(404, response)
        self.assertEqual(1, response.json()['code'])


if __name__ == '__main__':
    unittest.main()
