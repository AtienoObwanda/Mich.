from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
# from users.views import MyObtainTokenPairView,  TestRegisterView
# from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    # path('api/register/', views.RegisterUser.as_view()),
    path('api/login/', views.LoginUser.as_view()),
    path('api/user/', views.ProfileView.as_view()),
    path('api/logout/', views.LogoutView.as_view()),

    path('register', views.UserRegistrationView.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name = 'login'),

    path('user/', views.ProfileView.as_view(), name='account'),
    path('logout/', views.LogoutView.as_view()),
    path('add/project/', views.AddProject.as_view(),name='addProject'),
    path('edit/project/<int:pk>/', views.UpdatePoject.as_view(),name='updateProject'),
    path('review/project/<int:pk>/', views.AddReview.as_view(),name='review'),

    path('delete/project/<int:pk>/', views.DeleteProject.as_view(),name='deleteProject'),
    path('profile/<int:pk>/', views.UserProfile.as_view(),name='profile'),
    path('edit/profile/<int:pk>/', views.EditProfile.as_view(),name='editProfile'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)