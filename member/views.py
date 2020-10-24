from .forms import ProfileEditForm
from .models import Borrow, Profile
from django.contrib import messages
from authors.models import Author
from books.models import Book
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.



def borrow(request, slug):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')
    member = request.user
    num_borrowed = member.profile.num_borrowed
    if (num_borrowed >= 3):
        messages.error(request, "You have BORROWED 3 books.\nAnd you can\'t Borrow more!")
        return redirect('profile')
    book = Book.objects.get(slug=slug)
    instance = Borrow()
    instance.member = member
    instance.book = book
    #instance.member.profile.num_borrowed += 1
    #member.save()
    book.available = False
    book.save()
    instance.save()
    messages.success(request,"Borrowed Successfully")
    return redirect('profile')

def returning(request,slug):
    member = request.user
    book = Book.objects.get(slug=slug)
    book.available = True
    instance = Borrow.objects.get(
        Q(member = member) &
        Q(book__slug = slug)
    )
    instance.delete()
    book.save()
    messages.success(request,"Returned Successfully")
    return redirect('profile')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login')

    member = request.user
    books = []
    # Could I use len(books) instead of all num_borrowed things ???
    for borrow_obj in Borrow.objects.filter(member = member):
        books.append(borrow_obj.book)

    context = {
        'name': member.username,
        'books':books,
    }
    return render(
        request=request,
        template_name="account/profile.html",
        context=context
    )

def profile_edit(request):
    profile = request.user.profile
    form = ProfileEditForm(request.POST or None, request.FILES or None, instance=profile)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request,"Changes Saved")
        return redirect('profile')
    context = {
        'form': form,
        "submit_value": "Edit",
    }
    return render(request=request, template_name="account/profile_edit.html", context=context)

