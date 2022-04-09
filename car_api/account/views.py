from django.contrib.auth import get_user_model
from rest_framework import generics as rest_views

from car_api.account.authentication import UserAuthentication
from car_api.account.serializers import RegisterUserSerializer, LoginUserSerializer

UserModel = get_user_model()


class RegisterView(rest_views.CreateAPIView):
    serializer_class = RegisterUserSerializer


class LoginView(rest_views.GenericAPIView):
    authentication_classes = (UserAuthentication, )
    serializer_class = LoginUserSerializer
    http_method_names = ['get', 'post']

    def post(self, request):
        pass
