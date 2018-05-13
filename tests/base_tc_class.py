import unittest


class BaseApi(unittest.TestCase):
    def assert_status(self, code, response):
        self.assertEqual(
            code,
            response.status_code,
            msg='Request is: {} {}\nResponse code is {} {}\nResponse body is: {}'.format(
                response.request.method,
                response.request.url,
                response.status_code,
                response.reason,
                response.content
            )
        )

    def assert_status_list(self, code_list, response):
        self.assertIn(
            response.status_code,
            code_list,
            msg='Request is: {} {}\nResponse code is {} {}\nResponse body is: {}'.format(
                response.request.method,
                response.request.url,
                response.status_code,
                response.reason,
                response.content
            )
        )
