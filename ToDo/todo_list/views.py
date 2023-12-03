from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from .forms import TodoForm
# Create your views here.


class ToDoView(ListView):
    model = Task
    template_name = "todo_view.html"
    context_object_name = 'todos'


class ToDoCreate(CreateView):
    model = Task
    template_name = "todo_create.html"
    form_class = TodoForm
    success_url = reverse_lazy("Todos")
    

class ToDoUpdate(UpdateView):
    model = Task
    template_name = "todo_update.html"
    form_class = TodoForm
    success_url = reverse_lazy("Todos")
    context_object_name = 'todo'

class ToDoDelete(DeleteView):
    model = Task
    template_name = "todo_delete.html"
    success_url = reverse_lazy("Todos")
    context_object_name = 'todo'
