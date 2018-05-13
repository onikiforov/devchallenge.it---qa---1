def create_pet_object(name, photo_urls=None, tags=None, status='available'):
    pet_object = {
        'name': name,
        'photo_urls': photo_urls if photo_urls else [],
        'tags': tags if tags else [],
        'status': status
    }

    return pet_object
