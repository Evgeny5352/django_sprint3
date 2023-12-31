from django.contrib.auth import get_user_model

from django.db import models
from core.models import PublishedModel
from .const import TITLE_MAX_LENGTH, TITLE_MAX_STRING


User = get_user_model()


class Category(PublishedModel):
    title = models.CharField('Заголовок',
                             max_length=TITLE_MAX_LENGTH)
    description = models.TextField('Описание')
    slug = models.SlugField('Идентификатор',
                            unique=True,
                            help_text='Идентификатор страницы для URL;'
                                      ' разрешены символы латиницы,'
                                      ' цифры, дефис и подчёркивание.')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title[:TITLE_MAX_STRING]


class Location(PublishedModel):
    name = models.CharField('Название места',
                            max_length=TITLE_MAX_LENGTH)

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name[:TITLE_MAX_STRING]


class Post(PublishedModel):
    title = models.CharField('Заголовок',
                             max_length=TITLE_MAX_LENGTH)
    text = models.TextField('Текст')
    pub_date = models.DateTimeField('Дата и время публикации',
                                    help_text='Если установить'
                                              ' дату и время в будущем — можно'
                                              ' делать отложенные публикации.')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='Автор публикации')
    location = models.ForeignKey(Location,
                                 on_delete=models.SET_NULL,
                                 blank=True,
                                 null=True,
                                 verbose_name='Местоположение')
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 verbose_name='Категория')

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('-pub_date',)
        default_related_name = 'posts'

    def __str__(self):
        return self.title[:TITLE_MAX_STRING]
