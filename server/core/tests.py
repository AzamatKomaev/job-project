from typing import Optional
from django.urls import reverse
from rest_framework.test import APIClient


def send_test_request(method: str,
                      path_name: str,
                      params: Optional[list[str]] = None,
                      data: Optional[dict[str, str]] = None):
    client = APIClient()
    full_path = reverse(path_name, args=params)
    match method:
        case 'GET':
            response = client.get(full_path)
        case 'POST':
            response = client.post(full_path, data=data)
        case 'PATCH':
            response = client.patch(full_path, data=data)
        case _:
            response = client.get(full_path)

    return response
