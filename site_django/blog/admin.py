from django.contrib import admin
from .models import News #импортируем нашу модель
from .models import Messages

admin.site.register(News)
admin.site.register(Messages)

# Register your models here.
