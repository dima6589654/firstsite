from django.contrib import admin
from .models import TodoList, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created', 'due_date', 'category', 'user')
    search_fields = ('title', 'content', 'user__username')

    list_filter = ('category', 'user')
    date_hierarchy = 'created'
    ordering = ('-created',)
