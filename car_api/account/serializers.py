from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers


UserModel = get_user_model()


class RegisterUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        extra_kwargs = {
            'password': {
                'write_only': True
            },
        }
        fields = ('username', 'first_name', 'last_name', 'password')

    def create(self, validated_data):

        user = UserModel.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=make_password(validated_data['password']),
        )

        return user


class LoginUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ('username', 'password')
