from django.contrib.auth import get_user_model
from rest_framework import authentication
from rest_framework import exceptions

UserModel = get_user_model()


class UserAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        username = request.META.get('X_USERNAME')
        if not username:
            return None

        try:
            user = UserModel.objects.get(username=username)
        except UserModel.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return user, None
