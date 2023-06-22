from django.urls import path, re_path
from bblist.views import task_list, delete_task, edit_task, task_detail, create_task

urlpatterns = [
    # path('', task_list, name='task_list'),
    # path('create/', create_task, name='create_task'),
    # path('<int:task_id>/', task_detail, name='task_detail'),
    # path('<int:task_id>/edit/', edit_task, name='edit_task'),
    # path('<int:task_id>/delete/', delete_task, name='delete_task'),

    re_path(r'^$', task_list, name='task_list'),
    re_path(r'^create/$', create_task, name='create_task'),
    re_path(r'^(?P<task_id>\d+)/$', task_detail, name='task_detail'),
    re_path(r'^(?P<task_id>\d+)/edit/$', edit_task, name='edit_task'),
    re_path(r'^(?P<task_id>\d+)/delete/$', delete_task, name='delete_task'),
]

