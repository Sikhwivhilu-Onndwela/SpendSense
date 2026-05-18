from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tracker/', views.tracker, name='tracker'),
    path('tips/', views.tips, name='tips'),
    path('about/', views.about, name='about'),
]