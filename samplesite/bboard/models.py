from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models


def get_min_length():
    min_length = 3
    return min_length


def validate_even(val):
    if val % 2 != 0:
        raise ValidationError('Число %(value)s нечётное', code='odd',
                              params={'value': val})


class Rubric(models.Model):
    name = models.CharField(
        max_length=20,
        db_index=True,
        verbose_name="Название",
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/{self.pk}/"

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']


class Bb(models.Model):
    KINDS = (
        ("B", "куплю"),
        ("S", "продам"),
        ("C", "поменяю"),
    )

    rubric = models.ForeignKey(
        'Rubric',
        null=True,
        on_delete=models.PROTECT,
        verbose_name='Рубрика',
    )

    title = models.CharField(
        max_length=50,
        verbose_name="Товар",
        validators=[validators.MinLengthValidator(get_min_length)],
        error_messages={'min_length': 'Слишком мало символов'},
    )

    content = models.TextField(
        null=True,
        blank=True,
        verbose_name="Описание",
    )

    price = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Цена",
        validators=[validate_even]  # , MinMaxValueValidator(50, 60_000_000)]
    )

    published = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
        verbose_name="Опубликовано",
    )
    kind = models.CharField(
        max_length=1,
        choices=KINDS,
        default='S'
    )
    my_list = models.TextField(
        verbose_name="Список",
        null=True,
        blank=True
        )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Создание экземпляров модели Bb
        Bb.objects.create(title="Запись 1", my_list="Одиночная запись")
        for i in range(5):
            title = f"Запись {i + 1}"
            my_list = f"Запись {i + 1} в цикле"
            Bb.objects.create(title=title, my_list=my_list)


    def __str__(self):
        return f'Объявление: {self.title}'

    def title_and_price(self):
        if self.price:
            return f'{self.title} ({self.price:.2f})'
        return self.title

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        ordering = ['-published', 'title']
