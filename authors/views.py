from .models import Author
from .forms import AuthorForm
from books.models import Book
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect,redirect
from django.utils import timezone
from django.core.paginator import Paginator
from django.core import serializers


# Create your views here.

def base(request):
    return render(
        request=request,
        template_name= "base.html",
        context={}
    )

def retrive(request): #retrive
    authors =  Author.objects.all()
    paginator = Paginator(authors, 6) # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }
    return render(
        request= request,
        template_name="authors/retrive.html",
        context= context)


def detail(request, slug=None): # retrive
    author = Author.objects.get(slug=slug)
    context = {
        'author': author,
        'books': author.book_set.all()
    }
    return render(
        request=request,
        template_name='authors/detail.html',
        context=context
    )


def edit(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    else:
        instance = Author.objects.get(slug=slug)
        form = AuthorForm(request.POST or None, request.FILES or None, instance=instance)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request,"Changes Saved")
            return HttpResponseRedirect(instance.get_absolute_url())
        context={
            'form':form,
            "submit_value": "Edit Post",
        }
        return render(
            request=request,
            template_name= 'authors/form.html',
            context=context
        )

def delete(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    else:
        instance = Author.objects.get(slug=slug)
        instance.delete()
        messages.success(request,"Successfully Deleted")
        return redirect("authors:retrive")


def create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    else:
        form = AuthorForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request,"Successfully Created")
            #return HttpResponseRedirect(instance.get_absolute_url())
        context={
            "form": form,
            "submit_value": str("Create New Post"),
        }
        return render(request=request, template_name="authors/form.html", context=context)

#
#def ser(request):
#    if not request.user.is_staff or not request.user.is_superuser:
#        raise Http404
#    data = serializers.serialize("json", Book.objects.all())
#    with open("Books.json", mode='a', encoding='utf-8') as f:
#        f.write(data)
#    print(data)
#    return redirect("authors:retrive")


def deser_book(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    with open("serialized/Books.json", mode='r', encoding='utf-8') as f:
        data = f.read()
        for obj in serializers.deserialize("json", data):
            obj.save()
    return redirect("books:retrive")


def deser_author(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    with open("serialized/Authors.json", mode='r', encoding='utf-8') as f:
        data = f.read()
        for obj in serializers.deserialize("json", data):
            obj.save()
    return redirect("authors:retrive")
