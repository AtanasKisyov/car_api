import json

from rest_framework import status

from car_api.car.models import UserCar
from car_api.common_tools.TestDataMixin import TestDataMixin


class UserCarTest(TestDataMixin):

    def test_create_success(self):
        self.login(self.VALID_LOGIN_DATA)
        response = self.create_user_car(self.VALID_USER_CAR)

        user_car = UserCar.objects.first()

        expected_status_code = status.HTTP_201_CREATED
        expected_user_car_odometer = self.VALID_USER_CAR['odometer']

        actual_status_code = response.status_code
        actual_user_car_odometer = user_car.odometer

        self.assertIsNotNone(user_car)
        self.assertEqual(expected_status_code, actual_status_code)
        self.assertEqual(expected_user_car_odometer, actual_user_car_odometer)

    def test_create_failure(self):

        self.login(self.VALID_LOGIN_DATA)
        response = self.create_user_car(self.INVALID_USER_CAR)

        user_car = UserCar.objects.first()

        expected_status_code = status.HTTP_400_BAD_REQUEST
        actual_status_code = response.status_code

        self.assertIsNone(user_car)
        self.assertEqual(expected_status_code, actual_status_code)

    def test_get_request_returns_correct_data(self):
        self.login(self.VALID_LOGIN_DATA)
        self.create_user_car(self.VALID_USER_CAR)

        response = self.client.get(self.USER_CAR_URL)
        data = json.loads(response.content)[0]

        expected_user_car_brand_name = self.VALID_USER_CAR['odometer']
        actual_user_car_brand_name = data['odometer']

        self.assertEqual(expected_user_car_brand_name, actual_user_car_brand_name)
