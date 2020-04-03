from django.urls import path, re_path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.articles_index, name='index'),
    path('create/', views.articles_create, name='create'),
    re_path(r'^(?P<slug>[\w-]+)/$', views.articles_detail, name='detail')
]