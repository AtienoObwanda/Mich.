from django.urls import path
from . import views

urlpatterns = [
    path('api/projects/', views.ProjectList.as_view()),
    path('', views.AllProjectList.as_view(), name='projects' )
    # path('project/<int:pk>/', views.ProjectDetail.as_view()),
]
