from django.db import models
from django.utils import timezone #для работы с датой и временем
from django.contrib.auth.models import User
from django.urls import reverse #для возврата текущей страницы

class News(models.Model):  
    title = models.CharField('Название статьи', max_length=100, unique=True) #для уникальности названий
    text = models.TextField('Основной текст статьи') #как TEXT и VARCHAR в SQL
    date = models.DateTimeField('Дата и время публикации', default=timezone.now) #чтобы проставлялось текущее время
    author = models.ForeignKey(User, verbose_name='Автор' ,on_delete=models.CASCADE) 

    views = models.IntegerField('Просмотры', default=0)

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'pk': self.pk})  
    
    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

class Messages(models.Model):
    topic = models.CharField('Тема письма', max_length=100)
    email = models.EmailField('Почта получателя')
    text = models.TextField('Текст сообщения')
    date = models.DateTimeField('Дата и время отправки сообщения', default=timezone.now)

    def __str__(self):
        return self.topic 
    
    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'База сообщений'
# Create your models here.
