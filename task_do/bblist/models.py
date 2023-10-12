import os

from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    priority = models.IntegerField(verbose_name="Приоритет")
    due_date = models.DateTimeField(verbose_name="Срок выполнения")
    attachment = models.FileField(verbose_name="Вложение", upload_to='attachments/', default='default_attachment.jpg')

    def __str__(self):
        return self.title

    @classmethod
    def get_task_by_due_date(cls, due_date):
        return cls.objects.filter(due_date=due_date)

    @classmethod
    def get_tasks_ordered_by_due_date(cls):
        return cls.objects.order_by('due_date')


# #######################################
@receiver(post_delete, sender=Task)
def delete_attachment(sender, instance, **kwargs):
    if instance.attachment:
        if os.path.isfile(instance.attachment.path):
            os.remove(instance.attachment.path)
            print(f"Вложение удалено: {instance.attachment.name} для задачи: {instance.title}")


class IceCream(models.Model):
    flavor = models.CharField(max_length=100, verbose_name="Вкус")
    topping = models.CharField(max_length=100, verbose_name="Топпинг")
    price = models.DecimalField(max_digits=10, decimal_places=1, verbose_name="Цена")

    def __str__(self):
        return f"{self.flavor} - {self.topping}"
