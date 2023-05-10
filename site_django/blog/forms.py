from django import forms
from .models import Messages #для работы с таблицей профилей

class CreateMessageForm(forms.ModelForm):
    topic = forms.CharField(label='Тема письма',
                            required=True,
                            widget=forms.TextInput(attrs={'class': 'w-75 form-control', 'placeholder': 'Тема письма'}))
    email = forms.EmailField(label='Почта получателя',
                             required=True,
                             widget=forms.TextInput(attrs={'class': 'w-75 form-control', 'placeholder': 'Введите адрес эл. почты'}))
    text = forms.CharField(label='Текст письма',
                            required=True,
                            widget=forms.Textarea(attrs={'class': 'w-75 form-control', 'placeholder': 'Тема письма'}))
    
    class Meta:
        model = Messages
        fields = ['topic', 'email', 'text']