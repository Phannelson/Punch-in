from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('punch-in/', views.punch_in, name='punch_in'),
]