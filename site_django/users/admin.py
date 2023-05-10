from django.contrib import admin
from .models import Profile # чтобы таблица профилей подтянулась в бд

admin.site.register(Profile) # регистируем таблицу

# Register your models here.
