from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('car_api.account.urls')),
    path('car/', include('car_api.car.urls')),
]
