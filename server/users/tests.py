from rest_framework.test import APITestCase
from core.tests import send_test_request


class UserTestCase(APITestCase):
    def test_creating_users(self):
        # trying to create user without data.
        user_creating_without_data_response = send_test_request(
            method='POST',
            path_name='auth.create_user'
        )
        user_creating_without_data_response_json = user_creating_without_data_response.json()
        self.assertEqual(user_creating_without_data_response.status_code, 400)
        for field in ('username', 'first_name', 'last_name', 'role', 'password', 'email'):
            self.assertIn(field, user_creating_without_data_response_json)

        del field
        # trying to create user with not valid password, role and email.
        user_creating_with_not_valid_data_response = send_test_request(
            'POST',
            path_name='auth.create_user',
            data={
                'username': 'user1',
                'first_name': 'Azamat',
                'last_name': 'Komaev',
                'role': 'cool_person',
                'password': 'pwd',
                'email': 'not_email'
            }
        )
        user_creating_with_not_valid_data_response_json = user_creating_with_not_valid_data_response.json()
        self.assertEqual(user_creating_without_data_response.status_code, 400)
        self.assertEqual(len(user_creating_with_not_valid_data_response_json), 3)

        for field in ('password', 'role', 'email'):
            self.assertIn(field, user_creating_with_not_valid_data_response_json)

        del field
        self.assertEqual(
            user_creating_with_not_valid_data_response_json['password'][0],
            'Ensure this field has at least 8 characters.'
        )
        self.assertEqual(
            user_creating_with_not_valid_data_response_json['role'][0],
            '"cool_person" is not a valid choice.'
        )
        self.assertEqual(
            user_creating_with_not_valid_data_response_json['email'][0],
            'Enter a valid email address.'
        )

        # creating user.
        user_creating_response = send_test_request(
            method='POST',
            path_name='auth.create_user',
            data={
                'username': 'user1',
                'first_name': 'Azamat',
                'last_name': 'Komaev',
                'role': 'employee',
                'password': 'user1_pwd',
                'email': 'mail@mail.ru'
            }
        )
        user_creating_response_json = user_creating_response.json()
        self.assertEqual(user_creating_response.status_code, 201)
        self.assertEqual(len(user_creating_response_json), 5)

        for field in ('id', 'username', 'first_name', 'last_name', 'role'):
            self.assertIn(field, user_creating_response_json)

        del field
        # trying to create user with existing username and email
        user_creating_with_existing_data_response = send_test_request(
            method='POST',
            path_name='auth.create_user',
            data={
                'username': 'user2',
                'first_name': 'David',
                'last_name': 'Johnson',
                'role': 'employer',
                'password': 'user1_password',
                'email': 'mail@mail.ru'
            }
        )
        user_creating_with_existing_data_response_json = user_creating_with_existing_data_response.json()
        self.assertEqual(len(user_creating_with_existing_data_response_json), 1)
        self.assertIn('email', user_creating_with_existing_data_response_json)
        self.assertEqual(
            user_creating_with_existing_data_response_json['email'][0],
            'A user with that email already exists.'
        )
