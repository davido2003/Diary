from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.web1,name='home'),
    path('add/', views.web2, name='add')
]