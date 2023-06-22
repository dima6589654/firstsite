from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    priority = models.IntegerField()
    due_date = models.DateTimeField()

    def __str__(self):
        return self.title
