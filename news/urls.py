from django.urls import path
from .views import home, welcome, news_link_detail, news_detail, newcomments

urlpatterns = [
    path('', home, name='home'),
    path('welcome/', welcome, name='welcome'),
    path('newcomments/', newcomments, name='newcomments'),
    path('item/<int:pk>/', news_link_detail, name='detail'),
    path('item-news/<int:pk>/', news_detail, name='news_detail'),
]