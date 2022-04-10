import json

from rest_framework import status

from car_api.car.models import CarBrand
from car_api.common_tools.TestDataMixin import TestDataMixin


class CarBrandTest(TestDataMixin):

    def test_create_success(self):
        self.login(self.VALID_LOGIN_DATA)
        response = self.create_car_brand(self.VALID_CAR_BRAND)

        car_brand = CarBrand.objects.first()

        expected_response = status.HTTP_201_CREATED
        expected_car_brand_name = self.VALID_CAR_BRAND['car_brand_name']

        actual_response = response.status_code
        actual_car_brand_name = car_brand.car_brand_name

        self.assertIsNotNone(car_brand)
        self.assertEqual(expected_response, actual_response)
        self.assertEqual(expected_car_brand_name, actual_car_brand_name)

    def test_create_failure(self):
        self.login(self.VALID_LOGIN_DATA)
        response = self.create_car_brand(self.INVALID_CAR_BRAND)

        car_brand = CarBrand.objects.first()

        expected_response = status.HTTP_400_BAD_REQUEST

        actual_response = response.status_code

        self.assertIsNone(car_brand)
        self.assertEqual(expected_response, actual_response)

    def test_get_request_returns_correct_data(self):
        self.login(self.VALID_LOGIN_DATA)
        self.create_car_brand(self.VALID_CAR_BRAND)

        response = self.client.get(self.CAR_BRAND_URL)
        data = json.loads(response.content)[0]

        expected_car_brand_name = self.VALID_CAR_BRAND['car_brand_name']
        actual_car_brand_name = data['car_brand_name']

        self.assertEqual(expected_car_brand_name, actual_car_brand_name)
