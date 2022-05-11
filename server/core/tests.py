from typing import Optional
from django.urls import reverse
from rest_framework.test import APIClient


def send_test_request(method: str,
                      path_name: str,
                      params: Optional[list[str]] = None,
                      data: Optional[dict[str, str]] = None,
                      headers: Optional[dict[str, str]] = None):
    client = APIClient()
    full_path = reverse(path_name, args=params)

    if headers is None:
        headers = {}

    match method:
        case 'GET':
            response = client.get(full_path, **headers)
        case 'POST':
            response = client.post(full_path, data=data, **headers)
        case 'PATCH':
            response = client.patch(full_path, data=data, **headers)
        case _:
            response = client.get(full_path, **headers)

    return response
