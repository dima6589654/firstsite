from django.urls import path, include
from django.views.decorators.cache import cache_page
from bblist import views
from task_do import settings

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', cache_page(60)(views.create_task), name='create_task'),
    path('<int:task_id>/', cache_page(60)(views.task_detail), name='task_detail'),
    path('<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('tasks/due-today/', views.tasks_due_today, name='tasks_due_today'),
    path('tasks/ordered-by-due-date/', views.tasks_ordered_by_due_date, name='tasks_ordered_by_due_date'),
    path('icecream-list/', views.icecream_list, name='icecream_list'),
    path('create-icecream/', views.create_icecream, name='create_icecream'),
    path('task_titles/', views.task_titles, name='task_titles'),
    path('search/', views.search, name='search'),
]

if settings.DEBUG:
    # import debug_toolbar

    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
