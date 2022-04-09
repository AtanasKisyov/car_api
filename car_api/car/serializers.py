from rest_framework import serializers

from car_api.car.models import CarBrand, CarModel, UserCar


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = ('car_brand_name',)

    def create(self, validated_data):
        car_brand = CarBrand.objects.create(
            car_brand_name=validated_data['car_brand_name'],
        )
        return car_brand


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('car_model_name', 'car_brand')

    def create(self, validated_data):
        car_model = CarModel.objects.create(
            car_model_name=validated_data['car_model_name'],
            car_brand_id=validated_data['car_brand'].id,
        )
        return car_model


class UserCarSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCar
        fields = ('car_brand', 'car_model', 'first_registration', 'odometer')

    def create(self, validated_data):
        user = self.context['request'].user
        car_brand = validated_data['car_brand']
        car_model = validated_data['car_model']
        user_car = UserCar.objects.create(
            user=user,
            car_brand=car_brand,
            car_model=car_model,
            first_registration=validated_data['first_registration'],
            odometer=validated_data['odometer']
        )
        return user_car
