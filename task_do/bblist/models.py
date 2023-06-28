from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100,verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    priority = models.IntegerField(verbose_name="Приоритет")
    due_date = models.DateTimeField(verbose_name="Время выполнения")

    def __str__(self):
        return self.title
