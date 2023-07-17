from authapp.views import login, logout, AllUsersView, UserDetailView
from django.urls import path
app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/',logout, name='logout'),
    path('users/', AllUsersView.as_view(), name='user_list'),
    path('users/detail/', UserDetailView.as_view(), name='user_detail'),
]
