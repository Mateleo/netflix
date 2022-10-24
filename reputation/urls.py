from django.urls import path

from . import views

urlpatterns = [
    path('cw1', views.cw1, name='cw1'),
    path('cw2', views.cw2, name='cw2'),
    path('cw3', views.cw3, name='cw3'),
    path('tw1', views.tw1, name='tw1'),
    path('tw2', views.tw2, name='tw2'),
    path('tw3', views.tw3, name='tw3'),
]