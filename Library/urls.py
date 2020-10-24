"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from authors import views as author_view
from books import views as book_view
from member import views as member_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.static import serve


urlpatterns = [
    path('', author_view.base),
    path('accounts/profile/',member_view.profile, name = 'profile'),
    path('accounts/profile/edit',member_view.profile_edit, name = 'edit'),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('deser-book', author_view.deser_book),
    path('deser-author', author_view.deser_author),
    #path('ser', author_view.ser),
    re_path(r'^authors/', include("authors.urls", namespace='authors')),
    re_path(r'^books/', include("books.urls", namespace='books')),
    #re_path(r'^member/', include("member.urls", namespace='member')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]


