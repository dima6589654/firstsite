# -*- coding: utf-8 -*-
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from .forms import TaskForm, CategoryForm, CustomUserCreationForm
from .models import TodoList, Category


class RegisterView(View):
    template_name = 'registration/register.html'
    form_class = CustomUserCreationForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
        return render(request, self.template_name, {'form': form})


class GoodbyeView(TemplateView):
    template_name = 'registration/goodbye.html'


class TaskListView(ListView):
    model = TodoList
    template_name = 'todolist/task_list.html'
    context_object_name = 'tasks'
    ordering = ['-created']


class TaskDetailView(DetailView):
    model = TodoList
    template_name = 'todolist/task_detail.html'
    context_object_name = 'task'


@method_decorator(login_required, name='dispatch')
class TaskCreateView(CreateView):
    model = TodoList
    template_name = 'todolist/task_create.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class TaskUpdateView(UpdateView):
    model = TodoList
    template_name = 'todolist/task_update.html'
    form_class = TaskForm
    success_url = reverse_lazy('task_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.get_object()
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class TaskDeleteView(DeleteView):
    model = TodoList
    template_name = 'todolist/task_delete.html'
    success_url = reverse_lazy('task_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.get_object()
        return context


class CategoryListView(ListView):
    model = Category
    template_name = 'todolist/category_list.html'
    context_object_name = 'categories'


@method_decorator(login_required, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    template_name = 'todolist/category_create.html'
    form_class = CategoryForm
    success_url = reverse_lazy('category_list')


@method_decorator(login_required, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'todolist/category_delete.html'
    success_url = reverse_lazy('category_list')

    def get(self, request, *args, **kwargs):
        category = self.get_object()
        return render(request, self.template_name, {'category': category})

    def post(self, request, *args, **kwargs):
        category = self.get_object()
        try:
            related_tasks = category.todolist_set.all()
            if related_tasks.exists():
                return HttpResponse('<h1>Сначала удалите задачи с этой категорией!</h1>')
            return self.delete(request, *args, **kwargs)
        except BaseException:
            return HttpResponse(f'<h1>Произошла ошибка при удалении категории:</h1>')
