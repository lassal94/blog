from django.shortcuts import render, redirect, get_object_or_404 # render позволяет отобразить определенный html-файл по определенному адресу
from .models import News  #чтобы выводить данные из БД на страницу сайта
from .forms import CreateMessageForm
from django.views.generic import (
    ListView,
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView
    ) #лучше использовать ListView - встроенный класс для вывода информации
      #DetailView - для постраничного вывода
      #CreateView - для создания на странице формы для добавления записи в определенную таблицу
      #UpdateView - для изменения информации в существующей записи
      #DeleteView - для удаления статьи
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
#LoginRequiredMixin используем, чтобы сделать страницу только доступным пользователям
#UserPassesTestMixin - чтобы статью мог редактировать только автор
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from django.core.mail import send_mail

class ShowNewsView(ListView):
    model = News #прописываем модель взаимодействия
    template_name = 'blog/home.html' #прописываем шаблон для вывода
    context_object_name = 'news' #встроенный атрибут, в него записываем то, что хотим отобразить (к чему потом обращаемся в шаблоне html)
    ordering = ['-date'] #можно добавить сортировку и указать по какому полю будем сортировать '-' - для обратной сортировки
    paginate_by = 2 #не более 2-х статей на странице

    def get_context_data(self, **kwargs):  #функция для передачи доп параметров в шаблон
        ctx = super(ShowNewsView, self).get_context_data(**kwargs) #передаем сам класс и получаем список параметров

        ctx['title'] = 'Главная страница сайта' #указываем значение
        return ctx
    
class UserAllNewsView(ListView):
    model = News #прописываем модель взаимодействия
    template_name = 'blog/user_news.html' #прописываем шаблон для вывода
    context_object_name = 'news' #встроенный атрибут, в него записываем то, что хотим отобразить (к чему потом обращаемся в шаблоне html)    paginate_by = 2 #не более 2-х статей на странице
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username')) #вытягиваем логин пользователя из url адреса
        return News.objects.filter(author=user).order_by('-date') #получаем только посты по текущему и автору и сортируем по дате в обратном порядке

    def get_context_data(self, **kwards):  #функция для передачи доп параметров в шаблон
        ctx = super(UserAllNewsView, self).get_context_data(**kwards) #передаем сам класс и получаем список параметров

        ctx['title'] = f"Статьи от пользователя {self.kwargs.get('username')}"
        return ctx
    
class NewsDetailView(DetailView):
    model = News
    template_name = 'blog/news_detail.html' #прописываем шаблон для обработки, вообще имя news_detail формируется автоматически, 
                                            #так что если хотим задать именно такое - можно не прописывать это поле
    context_object_name = 'post' #встроенный атрибут, в него записываем то, что хотим отобразить (к чему потом обращаемся в шаблоне html)

    def get_context_data(self, **kwards):  #функция для передачи доп параметров в шаблон именно kwards
        ctx = super(NewsDetailView, self).get_context_data(**kwards) #передаем сам класс и получаем список параметров

        ctx['title'] = News.objects.get(pk=self.kwargs['pk']) #получаем название текущей страницы и выводим его в тайтл
        return ctx
    
class CreateNewsView(LoginRequiredMixin, CreateView): #для создания на странице формы для добавления записи в определенную таблицу
    model = News                                      # LoginRequiredMixin используем, чтобы сделать страницу только доступным пользователям
    template_name = 'blog/create_news.html' # по умолчанию тут будет news_form.html

    fields = ['title', 'text']

    def get_context_data(self, **kwards):
        ctx = super(CreateNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Добавление статьи'
        ctx['btn_text'] = 'Добавить статью'
        return ctx

    def form_valid(self, form):
        form.instance.author = self.request.user #записываем зарегистрированного пользователя и возвращаем,
        #чтобы корректно записывался автор статьи
        return super().form_valid(form)
    
class UpdateNewsView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = News                                      
    template_name = 'blog/create_news.html'  #можно использовать тот же шаблон, что и для создания записи

    fields = ['title', 'text']

    def get_context_data(self, **kwards):
        ctx = super(UpdateNewsView, self).get_context_data(**kwards)
        ctx['title'] = 'Обновление статьи'
        ctx['btn_text'] = 'Обновить статью'
        return ctx
    
    def test_func(self):
        news = self.get_object()
        return self.request.user == news.author

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
    
class DeleteNewsView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = News
    template_name = 'blog/delete_news.html'
    success_url = '/'

    def test_func(self): #чтобы только автор статьи мог ее удалить
        news = self.get_object()
        return self.request.user == news.author

def contacts(request):
    if request.method == 'POST':  # проверка метода передачи данных
        form = CreateMessageForm(request.POST)
        if form.is_valid(): #проверка корректности данных
            form.save()
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('topic')
            plain_message = form.cleaned_data.get('text')
            from_email = f"Logo example@mail.ru"
            send_mail(subject, plain_message, from_email, [email])
            messages.success(request, f'Сообщение успешно отправлено на указанную вами почту {email}')
            return redirect('contacts')
    else:
        form = CreateMessageForm()

    return render(request, 
                  'blog/contacts.html', 
                  {
                    'title': 'Страница с контактами',
                    'form': form,
                  })

