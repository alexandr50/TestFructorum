from django.db import models


class Complation(models.Model):
    title = models.CharField(max_length=30, verbose_name='название')
    short_description = models.CharField(max_length=255, verbose_name='краткое описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return f'{self.title}'

