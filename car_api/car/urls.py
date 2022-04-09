from django.urls import path

from car_api.car.views import UserCarView, CarBrandView, CarModelView, UserCarDetailView, CarBrandDetailView, \
    CarModelDetailView

urlpatterns = [
    path('user-car/', UserCarView.as_view(), name='user_car'),
    path('user-car/<int:pk>', UserCarDetailView.as_view(), name='user_car_detail'),
    path('car-brand/', CarBrandView.as_view(), name='car_brand'),
    path('car-brand/<int:pk>', CarBrandDetailView.as_view(), name='car_brand_detail'),
    path('car-model/', CarModelView.as_view(), name='car_model'),
    path('car-model/<int:pk>', CarModelDetailView.as_view(), name='car_model_detail'),
]
