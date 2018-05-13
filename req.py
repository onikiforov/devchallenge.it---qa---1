import requests
import config

"""
Remove proxy dict
Move non request methods to another file
"""

proxy_ip = '127.0.0.1'
proxy_port = '8200'

http_proxy = 'http://{}:{}'.format(proxy_ip, proxy_port)
https_proxy = 'https://{}:{}'.format(proxy_ip, proxy_port)

proxyDict = {
    'http': http_proxy,
    'https': https_proxy
}

default_base_url = 'http://petstore.swagger.io'
default_api_version = 'v2'

try:
    use_proxy = config.use_proxy
except KeyError:
    use_proxy = False

try:
    base_url = config.base_url
except KeyError:
    base_url = default_base_url

try:
    api_version = config.api_version
except KeyError:
    api_version = default_api_version


def form_url(path):
    url = '{}/{}/{}'.format(base_url, api_version, path)

    return url


def find_pet_by_id(pet_id):
    url = form_url('pet/{}'.format(pet_id))

    r = requests.get(url,
                     proxies=proxyDict if use_proxy else None,
                     verify=False if use_proxy else None)

    return r


def add_new_pet(pet_object):
    url = form_url('pet')

    r = requests.post(url,
                      json=pet_object,
                      proxies=proxyDict if use_proxy else None,
                      verify=False if use_proxy else None)

    return r


def update_pet(pet_object):
    url = form_url('pet')

    r = requests.put(url,
                     json=pet_object,
                     proxies=proxyDict if use_proxy else None,
                     verify=False if use_proxy else None)

    return r


def delete_pet(pet_id):
    url = form_url('pet/{}'.format(pet_id))

    r = requests.delete(url,
                        proxies=proxyDict if use_proxy else None,
                        verify=False if use_proxy else None)

    return r


def update_pet_form_data(pet_id, pet_name=None, pet_status=None):
    url = form_url('pet/{}?name={}&status={}'.format(pet_id, pet_name, pet_status))

    r = requests.post(url,
                      proxies=proxyDict if use_proxy else None,
                      verify=False if use_proxy else None)

    return r


def upload_image(pet_id, image_file_path, image_file_name, additional_metadata=None):
    url = form_url('pet/{}/uploadImage'.format(pet_id))

    files = {'file': (image_file_name, open(image_file_path, 'rb'), 'image/jpeg')}

    values = {'additionalMetadata': additional_metadata}

    r = requests.post(url,
                      files=files,
                      data=values,
                      proxies=proxyDict if use_proxy else None,
                      verify=False if use_proxy else None)

    return r


def get_store_order(order_id):
    url = form_url('store/order/{}'.format(order_id))

    r = requests.get(url,
                     proxies=proxyDict if use_proxy else None,
                     verify=False if use_proxy else None)

    return r
