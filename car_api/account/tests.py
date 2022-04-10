from django.contrib.auth import get_user_model
from rest_framework import status

from car_api.common_tools.TestDataMixin import TestDataMixin

UserModel = get_user_model()


class AccountTest(TestDataMixin):

    def test_register_success(self):

        response = self.register(self.VALID_REGISTER_DATA)

        user = UserModel.objects.first()
        expected_response = status.HTTP_201_CREATED
        expected_first_name = self.VALID_REGISTER_DATA['first_name']
        expected_last_name = self.VALID_REGISTER_DATA['last_name']

        actual_response = response.status_code
        actual_first_name = user.first_name
        actual_last_name = user.last_name

        self.assertEqual(expected_response, actual_response)
        self.assertEqual(expected_first_name, actual_first_name)
        self.assertEqual(expected_last_name, actual_last_name)

    def test_register_failure(self):

        response = self.register(self.INVALID_REGISTER_DATA)

        user = UserModel.objects.first()
        expected_response = 400
        actual_response = response.status_code

        self.assertIsNone(user)
        self.assertEqual(expected_response, actual_response)

    def test_login_success(self):

        is_logged_in = self.login(self.VALID_LOGIN_DATA)

        self.assertTrue(is_logged_in)

    def test_login_failure(self):

        is_logged_in = self.login(self.INVALID_LOGIN_DATA)

        self.assertFalse(is_logged_in)
