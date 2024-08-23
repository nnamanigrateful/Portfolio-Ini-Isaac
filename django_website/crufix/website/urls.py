
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('project_detail/<str:proj>', views.project_detail, name='project_detail')
]
