from django.urls import path, include
from . import views

urlpatterns = [
    path('api/register/', views.RegisterUser.as_view()),
    path('api/login/', views.LoginUser.as_view()),
    path('api/user/', views.ProfileView.as_view()),
    path('api/logout/', views.LogoutView.as_view()),


    path('register', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name = 'login'),
    path('user/', views.ProfileView.as_view(), name='account'),
    path('logout/', views.LogoutView.as_view()),

]
