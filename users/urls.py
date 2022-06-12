from django.urls import path, include
from . import views

urlpatterns = [
    path('api/register/', views.RegisterUser.as_view(), name='register'),
    path('register', views.RegisterUser.as_view(), name='register'),
    #     path('register', views.RegisterUser.as_view(), name='register'),

]
