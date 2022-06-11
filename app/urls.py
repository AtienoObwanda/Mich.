from django.urls import path
from . import views

urlpatterns = [
    path('api/projects/', views.ProjectList.as_view()),
    # path('project/<int:pk>/', views.ProjectDetail.as_view()),
]
