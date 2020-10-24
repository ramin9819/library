from . import views as book_view
from member import views as member_view
from django.urls import path, re_path

app_name = 'books'

urlpatterns = [
    path('', book_view.retrive, name='retrive'),
    path('create', book_view.create),
    re_path(r'^(?P<slug>[\w-]+)/borrow/$', member_view.borrow, name='borrow'),
    re_path(r'^(?P<slug>[\w-]+)/return/$', member_view.returning, name='return'),
    re_path(r'^(?P<slug>[\w-]+)/$', book_view.detail, name='detail'),
    re_path(r'^(?P<slug>[\w-]+)/edit/$', book_view.edit, name='edit'),
    re_path(r'^(?P<slug>[\w-]+)/delete/$', book_view.delete, name='delete'),
]
