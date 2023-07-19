from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    priority = models.IntegerField(verbose_name="Приоритет")
    due_date = models.DateTimeField(verbose_name="Время выполнения")

    def __str__(self):
        return self.title

    @classmethod
    def get_task_by_due_date(cls, due_date):
        return cls.objects.filter(due_date=due_date)

    @classmethod
    def get_tasks_ordered_by_due_date(cls):
        return cls.objects.order_by('due_date')