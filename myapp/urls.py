from django.urls import path
from . import views

urlpatterns = [
    # URL Pattern For Home Page
    path(
        '',
        views.index,
        name='index'),
    # URL Pattern For About Page
    path(
        'about/',
        views.about,
        name='about'),
    # URL Pattern For Contact Page
    path(
        'contact/',
        views.contact,
        name='contact'),
    # URL Pattern For Creating A New Booking
    path(
        'book_table/',
        views.create,
        name='create'),
    # URL Pattern For Handling Submission Of Table Booking Form
    path(
        'add_table/',
        views.add_table,
        name='add_table'),
    # URL Pattern For Deleting A Booking
    path(
        'delete_booking/<int:id>/',
        views.delete_booking,
        name='delete_booking'),
    # URL Pattern For Updating A Booking
    path(
        'update_booking/<int:id>/',
        views.update_booking,
        name='update_booking'),
]
