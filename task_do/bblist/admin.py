from django.contrib import admin
from .models import Task, IceCream


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'due_date')
    list_filter = ('priority', 'due_date')
    search_fields = ('title', 'description')
    list_editable = ('priority',)  # Редактируемое поле
    list_per_page = 20  # Количество объектов на странице


class IceCreamAdmin(admin.ModelAdmin):
    list_display = ('flavor', 'topping', 'price')
    list_filter = ('flavor', 'topping')
    search_fields = ('flavor', 'topping')
    list_editable = ('price',)  # Редактируемое поле
    list_per_page = 20  # Количество объектов на странице


admin.site.register(Task, TaskAdmin)
admin.site.register(IceCream, IceCreamAdmin)
