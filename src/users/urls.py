from django.urls import path
from users import views 

urlpatterns = [
    path("users/", views.users, name="users"),
    path("users/<int:id>/delete", views.delete_user, name="delete_user"),
    path("users/<int:pk>", views.UserUpdate.as_view(), name="update_user"),
    path("users/new", views.UserCreate.as_view(), name="create_user"),
]