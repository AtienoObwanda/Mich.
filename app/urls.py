from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('api/projects/', views.TestProjectApi.as_view()),
    path('', views.AllProjectList.as_view(), name='projects' ),
    path('project/<int:pk>/', views.ProjectDetailList.as_view(),name='projectDetail'),
   ]
