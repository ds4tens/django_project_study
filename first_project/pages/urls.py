from django.urls import path 
from first_project.pages import views

urlpatterns = [
    path('',views.HomeView, name='home')
]