from django.contrib import admin
from .models import Task, IceCream


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'due_date')
    list_display_links = ('title', 'priority')
    search_fields = ('title', 'priority')


class IceCreamAdmin(admin.ModelAdmin):
    list_display = ('flavor', 'topping', 'price')
    list_display_links = ('flavor', 'topping')
    search_fields = ('flavor', 'topping')


admin.site.register(Task, TaskAdmin)
admin.site.register(IceCream, IceCreamAdmin)
