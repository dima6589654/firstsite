from django.db import models


class Car(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def __str__(self):
        return self.content

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'
