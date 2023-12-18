from django.db import models


class Bookmark(models.Model):
    WEBSITE = 'website'
    BOOK = 'book'
    ARTICLE = 'article'
    MUSIC = 'music'
    VIDEO = 'video'

    TYPES_LINKS = (
        (WEBSITE, 'website'),
        (BOOK, 'book'),
        (ARTICLE, 'article'),
        (MUSIC, 'music'),
        (VIDEO, 'video')
    )

    title = models.CharField(max_length=255, verbose_name='заголовок')
    description = models.TextField(verbose_name='краткое описание')
    url = models.URLField(verbose_name='ссылка')
    type = models.CharField(choices=TYPES_LINKS, default='website', verbose_name='тип ссылки')
    image = models.ImageField(max_length=255, upload_to='bookmarks', verbose_name='картинка', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')
    complation = models.ManyToManyField('complation.Complation', verbose_name='коллекция')

    def __str__(self):
        return self.title or ''
