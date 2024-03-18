# from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import UserModel
from .forms import *


class UserCreate(CreateView):
    model=UserModel
    template_name='index.html'
    fields="__all__"
    success_url=reverse_lazy('userlist')

class UserModelList(ListView):
    model = UserModel
    template_name = 'list.html'  # Specify your template path
    context_object_name = 'object_list'  # Customize the context object name
    success_url=reverse_lazy('userlist')

class UserModelUpdateView(UpdateView):
    model = UserModel
    template_name = 'update.html'  # Specify your template path
    fields = "__all__"  # Specify the fields you want to display in the form

    def get_success_url(self):
        return reverse_lazy('userlist')

class UserModelDeleteView(DeleteView):
    model = UserModel
    template_name = 'delete.html'  # Specify your template path
    success_url = reverse_lazy('userlist')
