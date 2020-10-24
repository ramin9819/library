from . import views as author_view
from django.urls import path, re_path

app_name = 'authors'

urlpatterns = [
    re_path(r'^(?P<slug>[\w-]+)/$', author_view.detail, name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', author_view.edit, name='edit'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', author_view.delete, name='delete'),
    path('', author_view.retrive, name='retrive'),
    path('create', author_view.create),

]
