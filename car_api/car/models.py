import datetime

from django.db import models

from car_api.account.models import AuthUser


class SoftDeleteMixin(models.Model):

    def soft_delete(self):
        self.is_deleted = True
        self.deleted_at = datetime.datetime.now()
        self.save()

    def restore(self):
        self.is_deleted = False
        self.save()

    class Meta:
        abstract = True


class CarBrand(SoftDeleteMixin):

    CAR_BRAND_NAME_MAX_LENGTH = 15

    car_brand_name = models.CharField(
        max_length=CAR_BRAND_NAME_MAX_LENGTH,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
    )
    is_deleted = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.car_brand_name


class CarModel(SoftDeleteMixin):

    CAR_MODEL_NAME_MAX_LENGTH = 15

    car_model_name = models.CharField(
        max_length=CAR_MODEL_NAME_MAX_LENGTH,
    )

    car_brand = models.ForeignKey(
        CarBrand,
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    is_deleted = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.car_model_name


class UserCar(SoftDeleteMixin):

    user = models.ForeignKey(
        AuthUser,
        on_delete=models.CASCADE,
    )

    car_brand = models.ForeignKey(
        CarBrand,
        on_delete=models.CASCADE,
    )

    car_model = models.ForeignKey(
        CarModel,
        on_delete=models.CASCADE,
    )

    first_registration = models.DateField()

    odometer = models.IntegerField()

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    is_deleted = models.BooleanField(
        default=False,
    )
