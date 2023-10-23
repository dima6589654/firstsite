from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .models import Task, IceCream


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'due_date')
    list_filter = ('priority', 'due_date')
    search_fields = ('title', 'description')
    list_editable = ('priority',)  # ������������� ����
    list_per_page = 20  # ���������� �������� �� ��������


class IceCreamAdmin(admin.ModelAdmin):
    list_display = ('flavor', 'topping', 'price')
    list_filter = ('flavor', 'topping')
    search_fields = ('flavor', 'topping')
    list_editable = ('price',)  # ������������� ����
    list_per_page = 20  # ���������� �������� �� ��������


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'date_joined', 'is_active')
    list_filter = ('date_joined', 'is_active')
    search_fields = ('username', 'email')
    list_editable = ('is_active',)
    list_per_page = 20



admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Task, TaskAdmin)
admin.site.register(IceCream, IceCreamAdmin)
