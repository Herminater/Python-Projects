from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("employees/", views.ToDoView.as_view(), name="Todos"),
    path("employees/create", views.ToDoCreate.as_view(), name="Todocreate"),
    path("employees/<int:pk>/update", views.ToDoUpdate.as_view(), name="Todoupdate"),
    path("employees/<int:pk>/delete", views.ToDoDelete.as_view(), name="Tododelete")]