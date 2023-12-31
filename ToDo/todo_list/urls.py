from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("todos/", views.ToDoView.as_view(), name="Todos"),
    path("todos/create", views.ToDoCreate.as_view(), name="Todocreate"),
    path("todos/<int:pk>/update", views.ToDoUpdate.as_view(), name="Todoupdate"),
    path("todos/<int:pk>/delete", views.ToDoDelete.as_view(), name="Tododelete")]