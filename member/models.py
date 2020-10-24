from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete, pre_delete, pre_save
from books.models import Book
from django.utils import timezone
from datetime import datetime, timedelta
from django.dispatch import receiver

# Create your models here.

class Borrow(models.Model):
    member = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    def __str__(self):
        return self.member.username +' - '+ self.book.slug



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    num_borrowed = models.IntegerField(default=0)
    prof = models.ImageField(upload_to='images/profile', default='images/profile/defaul-profile.png')

    def __str__(self):
        return self.user.username




#####Signals

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(pre_delete, sender=Book)
def remove_borrow_record(sender, instance, **kwargs):
    borrow_record = Borrow.objects.filter(book__slug = instance.slug)
    if borrow_record:
        borrow_record[0].delete()


@receiver(pre_delete, sender=Borrow)
def decrease_borrowed_num(sender, instance, **kwargs):
    user_prof = Profile.objects.get(user__username = instance.member.username)
    user_prof.num_borrowed -= 1
    user_prof.save()
    instance.book.available = True
    instance.book.save()
    

@receiver(post_save, sender=Borrow)
def increase_borrowed_num(sender, instance, **kwargs):
    user_prof = Profile.objects.get(user__username = instance.member.username)
    user_prof.num_borrowed += 1
    user_prof.save()