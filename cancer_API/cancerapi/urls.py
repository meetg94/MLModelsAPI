from django.urls import path
from . import views

urlpatterns = [
    path('', views.predict, name='home'),
    path('predict/', views.predict, name='predict'),
]