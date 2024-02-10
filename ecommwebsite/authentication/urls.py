from django.urls import path
from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
    path("login/", views.handle_login, name="login"),
    path("logout/", views.handle_logout, name="logout"),
]
