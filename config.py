import os

base_url = 'http://petstore.swagger.io'
api_version = 'v2'
use_proxy = False
image_file_name = 'doge.jpg'
image_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), image_file_name)
