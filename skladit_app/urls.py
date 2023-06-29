from django.contrib import admin
from django.urls import path, include

from skladit_app.views import *

urlpatterns = [
    path('', index, name='home'),
    path('second_page/', second_page, name='second_page'),
    path('page/', main_article, name='mail_article'),
    path('page/33/', uniq_article, name='uniq_article'),
    path('page/<int:page_id>/', article, name='article'),
    path('page/<int:page_id>/<slug:name>', article, name='article_name'),
    path('req/<slug:catid>/', reqget, name='reqget'),
]
