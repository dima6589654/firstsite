from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet)
router.register(r'icecream', views.IceCreamViewSet)
router.register(r'users', views.CustomUserViewSet)
urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('create/', views.CreateTaskView.as_view(), name='create_task'),
    path('<int:task_id>/', views.task_detail, name='task_detail'),
    path('<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('tasks/due-today/', views.tasks_due_today, name='tasks_due_today'),
    path('tasks/ordered-by-due-date/', views.tasks_ordered_by_due_date, name='tasks_ordered_by_due_date'),
    path('icecream-list/', views.icecream_list, name='icecream_list'),
    path('create-icecream/', views.create_icecream, name='create_icecream'),
    path('task_titles/', views.task_titles, name='task_titles'),
    path('search/', views.search, name='search'),
    path('api/', include(router.urls)),
    path('api/report/<int:task_id>/', views.ReportController.as_view(), name='report'),
    path('api/tasks-list/', views.TaskList.as_view(), name='tasks_list_api'),
    path('api/icecream-list/', views.IceCreamList.as_view(), name='icecream_list_api'),
]
if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]
