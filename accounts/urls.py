from django.urls import path
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('home/', views.expenses, name='expenses'),
    path('token/', views.get_jwt_token, name='get_token'),
]