from django.urls import path
from ProyectoWebbApp import views



urlpatterns = [
    path('', views.home, name='Home'),
    path('servicio/', views.service, name='Service'),
    path('tienda/', views.store, name='Store'),
    path('blog/', views.blog, name='Blog'),
    path('contacto/', views.contact, name='Contact'),
]