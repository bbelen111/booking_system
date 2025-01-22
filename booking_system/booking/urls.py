from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('desc/', views.desc, name='desc'),
    path('contact/', views.contact, name='contact'),
    path('rooms/', views.rooms_list, name='rooms_list'),
    path('bookings/', views.bookings_list, name='bookings_list'),
    path('bookings/create/', views.create_booking, name='create_booking'),
]
