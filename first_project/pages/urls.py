from django.urls import path 
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('hello/',views.HomePageView.as_view(), name='class_home'),
    path('about/', views.AboutPageView.as_view(), name='about'),
]