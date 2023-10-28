import os

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


class CustomUser(AbstractUser):
    bio = models.TextField(verbose_name="О себе")
    profile_picture = models.ImageField(verbose_name="Аватар", upload_to='avatars/', default='default_avatar.jpg')
    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Task(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Описание")
    priority = models.IntegerField(verbose_name="Приоритет")
    due_date = models.DateTimeField(verbose_name="Срок выполнения")
    attachment = models.FileField(verbose_name="Вложение", upload_to='attachments/', default='default_attachment.jpg')
    is_login_required = models.BooleanField(default=False, verbose_name="Требуется вход")

    def __str__(self):
        return self.title

    @classmethod
    def get_task_by_due_date(cls, due_date):
        return cls.objects.filter(due_date=due_date)

    @classmethod
    def get_tasks_ordered_by_due_date(cls):
        return cls.objects.order_by('due_date')

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


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

    def __str(self):
        return f"{self.flavor} - {self.topping}"

    class Meta:
        verbose_name = 'Мороженое'
        verbose_name_plural = 'Мороженое'
