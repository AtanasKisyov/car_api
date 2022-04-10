from rest_framework import generics as rest_views
from rest_framework.response import Response

from car_api.car.models import CarBrand, UserCar, CarModel
from car_api.car.serializers import UserCarSerializer, CarBrandSerializer, CarModelSerializer


class UserCarView(rest_views.ListCreateAPIView):
    serializer_class = UserCarSerializer
    queryset = UserCar.objects.filter(is_deleted=False)


class CarBrandView(rest_views.ListCreateAPIView):
    serializer_class = CarBrandSerializer
    queryset = CarBrand.objects.filter(is_deleted=False)


class CarModelView(rest_views.ListCreateAPIView):
    serializer_class = CarModelSerializer
    queryset = CarModel.objects.filter(is_deleted=False)


class UserCarDetailView(rest_views.RetrieveUpdateDestroyAPIView):
    serializer_class = UserCarSerializer
    queryset = UserCar.objects.filter(is_deleted=False)

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        obj = UserCar.objects.get(pk=pk)
        obj.soft_delete()
        return Response(
            {
                'is_deleted': True
             }
        )


class CarModelDetailView(rest_views.RetrieveUpdateDestroyAPIView):
    serializer_class = CarModelSerializer
    queryset = CarModel.objects.filter(is_deleted=False)

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        obj = CarModel.objects.get(pk=pk)
        obj.soft_delete()
        return Response(
            {
                'is_deleted': True
             }
        )


class CarBrandDetailView(rest_views.RetrieveUpdateDestroyAPIView):
    serializer_class = CarBrandSerializer
    queryset = CarBrand.objects.filter(is_deleted=False)

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        obj = CarBrand.objects.get(pk=pk)
        obj.soft_delete()
        return Response(
            {
                'is_deleted': True
             }
        )
