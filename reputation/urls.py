from django.urls import path

from . import views

urlpatterns = [
    path('cw1', views.cw1, name='cw1'),
]