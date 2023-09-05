# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.utils import timezone
from .forms import TaskForm, IceCreamForm
from .models import Task, IceCream


def task_list(request):
    tasks = Task.objects.all()
    paginator = Paginator(tasks, 5)
    page = request.GET.get('page')
    tasks = paginator.get_page(page)
    return render(request, 'task_list.html', {'tasks': tasks})


def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task_detail.html', {'task': task})


def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data['title']
            priority = form.cleaned_data['priority']
            due_date = form.cleaned_data['due_date']
            print(f"Заголовок: {title}, Приоритет: {priority}, Время выполнения: {due_date}")
            return render(request, 'success.html', {'success_message': 'Задача успешно создана!'})
        else:
            return render(request, 'create_task.html', {'form': form, 'error_message': 'Произошла ошибка валидации'})
    else:
        form = TaskForm()
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


def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'delete_task.html', {'task': task})


def tasks_due_today(request):
    current_datetime = timezone.now()
    tasks_due_today1 = Task.get_task_by_due_date(current_datetime.date())
    return render(request, 'tasks_due_today.html', {'tasks_due_today': tasks_due_today1})


def tasks_ordered_by_due_date(request):
    tasks_ordered = Task.get_tasks_ordered_by_due_date()
    return render(request, 'tasks_ordered_by_due_date.html', {'tasks_ordered': tasks_ordered})


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


def task_titles(request):
    tasks = Task.objects.values('title', 'priority')
    return render(request, 'task_titles.html', {'tasks': tasks})
