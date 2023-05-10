#файл для создания своих форм (неимпортированных) обязательно forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm #можем импортировать сюда класс стандартных форм
from .models import Profile #для работы с таблицей профилей

class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(label='Как вас зовут?', 
                               required=False, 
                               widget=forms.TextInput(attrs={'class': 'w-75 form-control', 'placeholder': 'Введите имя (необязательное поле)'}))
    last_name = forms.CharField(label='Ваша фамилия?', 
                               required=False, 
                               widget=forms.TextInput(attrs={'class': 'w-75 form-control', 'placeholder': 'Введите фамилию (необязательное поле)'}))
    email = forms.EmailField(label='Введите email', 
                             required=True,
                             widget=forms.TextInput(attrs={'class': 'w-75 form-control', 'placeholder': 'Введите адрес эл. почты'})) #тип поля - email required=False - чтобы регистрация проходила и без заполнения поля
    username = forms.CharField(label='Введите логин', 
                               required=True, 
                               help_text='Нельзя вводить символы: @, /, _',
                               widget=forms.TextInput(attrs={'class': 'w-75 form-control', 'placeholder': 'Введите логин'})) #help_text - для текста рядом с формой
    password1 = forms.CharField(label='Введите пароль', 
                                required=True, 
                                help_text='пароль не должен быть маленьким или простым',
                                widget=forms.PasswordInput(attrs={'class': 'w-25 form-control'})) #attrs - чтобы сразу добавлять стили
    password2 = forms.CharField(label='Повторите пароль', 
                                required=True,
                                widget=forms.PasswordInput(attrs={'class': 'w-25 form-control'}))

    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name' ,'password1', 'password2'] 

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='Как вас зовут?', 
                               required=False, 
                               widget=forms.TextInput(attrs={'class': 'w-75 form-control', 'placeholder': 'Введите имя (необязательное поле)'}))
    last_name = forms.CharField(label='Ваша фамилия?', 
                               required=False, 
                               widget=forms.TextInput(attrs={'class': 'w-75 form-control', 'placeholder': 'Введите фамилию (необязательное поле)'}))
    email = forms.EmailField(label='Введите email', 
                             required=True,
                             widget=forms.TextInput(attrs={'class': 'w-75 form-control', 'placeholder': 'Введите адрес эл. почты'})) #тип поля - email required=False - чтобы регистрация проходила и без заполнения поля
    username = forms.CharField(label='Введите логин', 
                               required=True, 
                               help_text='Нельзя вводить символы: @, /, _',
                               widget=forms.TextInput(attrs={'class': 'w-75 form-control', 'placeholder': 'Введите логин'}))
    
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name']

class ProfileForm(forms.ModelForm):
    img = forms.ImageField(label='Загрузить фото', 
                           required=False,
                           widget=forms.FileInput 
                          )
    sex = forms.ChoiceField(label='Выберите пол', 
                            choices=Profile.CHOISES,
                            required=False)
    agrees = forms.BooleanField(label='',
                                help_text='Согласен(а) на отправку уведомлений', 
                                required=False)
    
    
    class Meta:
        model = Profile 
        fields = ['img', 'sex', 'agrees']
    


