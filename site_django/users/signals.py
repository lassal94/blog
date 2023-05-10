# для отслеживания различных действий (сигналов) внутри проекта. В нашем случае - регистрация пользователя
from django.contrib.auth.models import User # импортируем таблицу
from .models import Profile # импортируем таблицу
from django.db.models.signals import post_save # непосредственно для отслеживания сигнала
from django.dispatch import receiver #декоратор, с помощью которого к методу можно добавить обработчик действия (сохранение данных в User)

@receiver(post_save, sender=User)
# функция создания профиля instance - созданный объект, 
# created - информация по поводу того, как был создан объект
# **kwargs - возможны и доп аргументы
def create_profile(sender, instance, created, **kwargs): 
    if created:
        Profile.objects.create(user=instance) # create() - позволяет создать новый объект в определенной таблице
        # user - это атрибут класса Profile(в файле models.py)

# для обновления информации про пользователя
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs): 
    instance.profile.save() # обращаемся к пользователю, берем его профайл и сохраняем информацию