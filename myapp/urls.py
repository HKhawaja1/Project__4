from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('book_table/', views.create, name='create'),
    path('add_table/', views.add_table, name='add_table'),
    path('delete_booking/<int:id>/', views.delete_booking, name='delete_booking'),
    path('update_booking/<int:id>/', views.update_booking, name='update_booking'),
]