# -*- coding: utf-8 -*-

import os

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View
from django.views.decorators.cache import cache_page
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import IceCreamForm, SearchForm
from .forms import TaskForm
from .models import CustomUser
from .models import IceCream
from .models import Task
from .serializers import CustomUserSerializer
from .serializers import TaskSerializer, IceCreamSerializer


class CreateTaskView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        form = TaskForm()
        if request.method == 'POST':
            form = TaskForm(request.POST, request.FILES)
            if form.is_valid():
                task = form.save(commit=False)
                attachment_file = request.FILES['attachment']
                with open(os.path.join('media', 'attachments', attachment_file.name), 'wb') as destination:
                    for chunk in attachment_file.chunks():
                        destination.write(chunk)
                task.attachment = 'attachments/' + attachment_file.name
                task.save()
                messages.add_message(request, settings.MY_CUSTOM_LEVEL, 'Задача успешно создана!')
                return redirect('task_list')

        return render(request, 'create_task.html', {'form': form})


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', task_id=task_id)
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form, 'task': task})


@cache_page(60)
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'delete_task.html', {'task': task})


def task_list(request):
    tasks = Task.objects.all()
    paginator = Paginator(tasks, 5)
    page = request.GET.get('page')
    tasks = paginator.get_page(page)
    return render(request, 'task_list.html', {'tasks': tasks})


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task_detail.html', {'task': task})


def create_icecream(request):
    if request.method == 'POST':
        form = IceCreamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('icecream_list')
    else:
        form = IceCreamForm()
    return render(request, 'create_icecream.html', {'form': form})


def icecream_list(request):
    icecream = IceCream.objects.all()
    paginator = Paginator(icecream, 5)
    page = request.GET.get('page')
    icecream = paginator.get_page(page)
    return render(request, 'icecream_list.html', {'icecream': icecream})


def tasks_due_today(request):
    current_datetime = timezone.now()
    tasks_due_today1 = Task.get_task_by_due_date(current_datetime.date())
    return render(request, 'tasks_due_today.html', {'tasks_due_today': tasks_due_today1})


def tasks_ordered_by_due_date(request):
    tasks_ordered = Task.get_tasks_ordered_by_due_date()
    return render(request, 'tasks_ordered_by_due_date.html', {'tasks_ordered': tasks_ordered})


def task_titles(request):
    tasks = Task.objects.values('title', 'priority')
    return render(request, 'task_titles.html', {'tasks': tasks})


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            tasks = Task.objects.filter(title__icontains=keyword)
            return render(request, 'search_results.html', {'tasks': tasks, 'keyword': keyword})
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # Ограничение доступа
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class IceCreamViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # Ограничение доступа
    queryset = IceCream.objects.all()
    serializer_class = IceCreamSerializer


class CustomUserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # Ограничение доступа
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def create_user(self):
        if self.method == 'POST':
            serializer = CustomUserSerializer(data=self.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReportController(APIView):
    permission_classes = [IsAuthenticated]  # Ограничение доступа

    def get(self, request, task_id):
        try:
            task = Task.objects.get(pk=task_id)
            icecream = IceCream.objects.first()
            task_serializer = TaskSerializer(task)
            icecream_serializer = IceCreamSerializer(icecream)
            report = {
                'task_details': task_serializer.data,
                'icecream_details': icecream_serializer.data
            }
            return Response(report)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=404)
