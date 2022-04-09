from django.urls import path, include

from car_api.account.views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('', include('rest_framework.urls'), name='login'),

]
