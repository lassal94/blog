from django.db import models
from django.contrib.auth.models import User #импортируем таблицу User
from PIL import Image #для работы с изображениями


class Profile(models.Model): #создаем новый класс для таблицы пользователя
    CHOISES = (('m', 'Мужской пол'), ('f', 'Женский пол'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)  
    sex = models.CharField(max_length=1, choices=CHOISES, default='m')
    agrees = models.BooleanField(default=False)
    img = models.ImageField('Фото пользователя', default='user_images/man.png', upload_to='user_images')


    def __str__(self):
        return f'Профиль пользователя {self.user.username}'
    
    def save(self, *args, **kwargs):  #будет применяться при сохранении данных. Прописываем для обрезки слишком больших изображений
        super().save() #наследуем стандартную save() из Model, которая применяется для сохранения данных
        image = Image.open(self.img.path) #получаем фото, которое пользователь пытается загрузить. path - для получения полного пути
        if image.height > 256 or image.width > 256:
            resize = (256, 256) # задаем новые размеры
            image.thumbnail(resize) # присваиваем новые размеры
            image.save(self.img.path) # перезапись предыдущей фотографии обрезанной фотографией

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


    

# Create your models here.
