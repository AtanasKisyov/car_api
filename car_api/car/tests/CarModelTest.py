import json

from rest_framework import status

from car_api.car.models import CarModel
from car_api.common_tools.TestDataMixin import TestDataMixin


class CarModelTest(TestDataMixin):

    def test_create_success(self):
        self.login(self.VALID_LOGIN_DATA)
        response = self.create_car_model(self.VALID_CAR_MODEL)

        car_model = CarModel.objects.first()

        expected_status_code = status.HTTP_201_CREATED
        expected_car_model_name = self.VALID_CAR_MODEL['car_model_name']

        actual_status_code = response.status_code
        actual_car_model_name = car_model.car_model_name

        self.assertIsNotNone(car_model)
        self.assertEqual(expected_status_code, actual_status_code)
        self.assertEqual(expected_car_model_name, actual_car_model_name)

    def test_create_failure(self):
        self.login(self.VALID_LOGIN_DATA)
        response = self.create_car_model(self.INVALID_CAR_MODEL)

        car_model = CarModel.objects.first()

        expected_status_code = status.HTTP_400_BAD_REQUEST
        actual_status_code = response.status_code

        self.assertIsNone(car_model)
        self.assertEqual(expected_status_code, actual_status_code)

    def test_get_request_returns_correct_data(self):
        self.login(self.VALID_LOGIN_DATA)
        self.create_car_model(self.VALID_CAR_MODEL)

        response = self.client.get(self.CAR_MODEL_URL)
        data = json.loads(response.content)[0]

        expected_car_brand_name = self.VALID_CAR_MODEL['car_model_name']
        actual_car_brand_name = data['car_model_name']

        self.assertEqual(expected_car_brand_name, actual_car_brand_name)
