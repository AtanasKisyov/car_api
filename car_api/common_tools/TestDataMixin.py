import datetime

from django.urls import reverse
from rest_framework.test import APITestCase

from car_api.car.models import CarBrand, CarModel


class TestDataMixin(APITestCase):

    REGISTER_URL = reverse('register')
    CAR_BRAND_URL = reverse('car_brand')
    CAR_MODEL_URL = reverse('car_model')
    USER_CAR_URL = reverse('user_car')

    INVALID_REGISTER_DATA = {
        'username': '',
        'first_name': 'test',
        'last_name': 'testov',
        'password': 'unbreakable_password_1234',
    }

    VALID_REGISTER_DATA = {
            'username': 'test_testov',
            'first_name': 'test',
            'last_name': 'testov',
            'password': 'unbreakable_password_1234',
        }

    INVALID_LOGIN_DATA = {
        'username': '',
        'password': 'unbreakable_password_1234'
    }

    VALID_LOGIN_DATA = {
        'username': 'test_testov',
        'password': 'unbreakable_password_1234'
    }

    INVALID_CAR_BRAND = {
        'car_brand_name': '',
    }

    VALID_CAR_BRAND = {
        'car_brand_name': 'Ford',
    }

    INVALID_CAR_MODEL = {
        'car_model_name': '',
    }

    VALID_CAR_MODEL = {
        'car_model_name': 'Fiesta',
    }

    INVALID_USER_CAR = {
        'registered_at': 'invalid_date',
        'odometer': 127000,
    }

    VALID_USER_CAR = {
        'first_registration': '2010-01-01',
        'odometer': 127000,
    }

    def register(self, register_data):
        return self.client.post(
            path=self.REGISTER_URL,
            data=register_data,
            format='json',
        )

    def login(self, login_data):
        self.register(self.VALID_REGISTER_DATA)
        return self.client.login(**login_data)

    def create_car_brand(self, car_brand):
        return self.client.post(
            path=self.CAR_BRAND_URL,
            data=car_brand,
            format='json',
        )

    def create_car_model(self, car_model):
        self.create_car_brand(self.VALID_CAR_BRAND)
        car_brand = CarBrand.objects.first()
        car_model['car_brand'] = car_brand.id
        return self.client.post(
            path=self.CAR_MODEL_URL,
            data=car_model,
            format='json',
        )

    def create_user_car(self, user_car):
        self.create_car_model(self.VALID_CAR_MODEL)
        car_brand = CarBrand.objects.first()
        car_model = CarModel.objects.first()
        user_car['car_brand'] = car_brand.id
        user_car['car_model'] = car_model.id
        return self.client.post(
            path=self.USER_CAR_URL,
            data=user_car,
            format='json',
        )
