from .forms import BookForm
from .models import Book
from django.contrib import messages
from authors.models import Author
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator


def retrive(request):
    books = Book.objects.all()
    query = request.GET.get("q")
    if query:
        books = Book.objects.filter(
            Q(name__icontains=query)|
            Q(author__fullName__icontains=query)|
            Q(summary__icontains=query)|
            Q(genre__icontains=query)
        ).distinct()
    
    paginator = Paginator(books, 6) # Show 2 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj
    }
    
    return render(
        request = request,
        template_name='books/retrive.html',
        context = context,
    )

def create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = BookForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Successfully Created")
        #return HttpResponseRedirect(instance.get_absolute_url())
    context={
        "form": form,
        "submit_value": str("Create New Post"),
    }

    return render(
        request = request,
        template_name = 'books/form.html',
        context = context
    )

def detail(request, slug):
    context = {
        'book': Book.objects.get(slug=slug)
    }
    return render(
        request=request,
        template_name = 'books/detail.html',
        context=context,
    )

def edit(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = Book.objects.get(slug=slug)
    form = BookForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Changes Saved")
        return HttpResponseRedirect(instance.get_absolute_url())
        # PLEASE CHECK HERE
    context={
        'form':form,
        "submit_value": "Edit Post",
    }
    return render(
        request=request,
        template_name= 'books/form.html',
        context=context
    )

def delete(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance = Book.objects.get(slug=slug)
    instance.delete()
    messages.success(request,"Successfully Deleted")
    return redirect("books:retrive")
