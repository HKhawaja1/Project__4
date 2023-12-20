from django.urls import path
from . import views


urlpatterns = [
    # A URL Pattern For'login_user'
    path('login_user', views.login_user, name="login"),
    # A URL Pattern For'logout_user'
    path('logout_user', views.logout_user, name='logout'),
    # A URL Pattern For'register_user'
    path('register_user', views.register_user, name='register_user'),
]
