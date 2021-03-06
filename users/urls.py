from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from .views import  ProjectReviewView,ProjectCreateView, ProjectDeleteView, ProjectUpdateView

from . import views

urlpatterns = [
    # path('api/register/', views.RegisterUser.as_view()),
    path('api/login/', views.LoginUser.as_view()),
    # path('api/user/', views.ProfileView.as_view()),
    path('api/logout/', views.LogoutView.as_view()),

    # path('login/', views.LoginUser.as_view(), name = 'login'),


    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout_user.html'), name='logout'),
    path('logout/', views.LogoutView.as_view()),
    path('add/project/', views.AddProject.as_view(),name='addProject'),
    path('edit/project/<int:pk>/', views.UpdatePoject.as_view(),name='updateProject'),
    path('review/project/<int:pk>/', views.ProjectReviewView,name='review'),

    path('delete/project/<int:pk>/', views.DeleteProject.as_view(),name='deleteProject'),
    path('profile/<int:pk>/', views.UserProfile.as_view(),name='profile'),
    path('edit/profile/<int:pk>/', views.EditProfile.as_view(),name='editProfile'),

    path('project/new/', ProjectCreateView.as_view(), name='createProject' ),
    path('project/update/<int:pk>/', ProjectUpdateView.as_view(), name='updateProject' ),
    path('project/delete/<int:pk>/', ProjectDeleteView.as_view(), name='deleteProject' ),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)