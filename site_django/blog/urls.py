from django.urls import path
from . import views # импортируем views из той же директории blog

#ОТСЛЕЖИВАЕМЫЕ URL АДРЕСА
urlpatterns = [
    path('', views.ShowNewsView.as_view(), name='home'),  
    path('user/<str:username>', views.UserAllNewsView.as_view(), name='user-news'),
    path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'), 
    path('news/<int:pk>/update', views.UpdateNewsView.as_view(), name='news-update'),
    path('news/<int:pk>/delete', views.DeleteNewsView.as_view(), name='news-delete'),
    path('news/add', views.CreateNewsView.as_view(), name='news-add'), #для формы добавления данных в таблицу
    path('contacts', views.contacts, name='contacts'), #еще одна страница
]