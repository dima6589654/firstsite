from django.urls import path, re_path
from bblist import views
from bblist.views import task_list, delete_task, edit_task, task_detail, create_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', create_task, name='create_task'),
    path('<int:task_id>/', task_detail, name='task_detail'),
    path('<int:task_id>/edit/', edit_task, name='edit_task'),
    path('<int:task_id>/delete/', delete_task, name='delete_task'),
    path('tasks/due-today/', views.tasks_due_today, name='tasks_due_today'),
    path('tasks/ordered-by-due-date/', views.tasks_ordered_by_due_date, name='tasks_ordered_by_due_date'),
]


