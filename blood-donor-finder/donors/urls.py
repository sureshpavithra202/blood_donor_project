from django.urls import path
from . import views

urlpatterns = [
    path("", views.donor_list, name="donor_list"),
    path("add/", views.add_donor, name="add_donor"),
    path("edit/<int:id>/", views.edit_donor, name="edit_donor"),
    path("delete/<int:id>/", views.delete_donor, name="delete_donor"),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
]