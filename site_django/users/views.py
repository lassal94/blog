from django.shortcuts import render, redirect
from .forms import UserRegisterForm, ProfileForm, UserUpdateForm 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':  # проверка метода передачи данных
        form = UserRegisterForm(request.POST)
        if form.is_valid(): #проверка корректности данных
            form.save()
            username = form.cleaned_data.get('username') #получаем данные из поля username в форме
            messages.success(request, f'Пользователь {username} был успешно зарегистрирован') #для вывода сообщения об успешной операции
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 
                  'users/registration.html', 
                  {
                    'title': 'Страница регистрации',
                    'form': form
                  })
@login_required #декоратор для проверки авторизации (чтобы на страницу профиля можно было зайти только при успешной авторизации)
def profile(request):
    if request.method == 'POST':
        profileForm = ProfileForm(request.POST, request.FILES, 
                                       instance=request.user.profile) 
        updateUserForm = UserUpdateForm(request.POST, request.FILES, 
                                        instance=request.user)   
        if profileForm.is_valid() and updateUserForm.is_valid(): #если обе формы валидные - обновляем
            updateUserForm.save()
            profileForm.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлен!') #выводим success уведомление
            return redirect('profile') #остаемся на той же странице
    else:
        profileForm = ProfileForm(instance=request.user.profile)
        updateUserForm = UserUpdateForm(instance=request.user)

    data = {
            'profileForm': profileForm,
            'updateUserForm': updateUserForm
        }

    return render(request, 'users/profile.html', data)

