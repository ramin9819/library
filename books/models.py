from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, post_delete, pre_delete
from django.urls import reverse
from django.utils.text import slugify
from authors.models import Author
from django.utils import timezone
from datetime import timedelta
from django.dispatch import receiver

# Create your models here.

class Book(models.Model):
    genre_choices = [
        ('General','عمومی'),
        ('Novel','رمان'),
        ('Poetry','شعر'),
        ('Historic','تاریخی'),
        ('Philosophical','فلسفی'),
        ('Psychology','روانشناسی'),
    ]

    name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    summary = models.TextField(null=True)
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=200)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.ImageField(upload_to='images/books',  #use upload location
                                    null=True,
                                    blank=True,
                                    )
    genre = models.CharField(
        max_length=200,
        choices=genre_choices,
        default='General',
    )

    class Meta:
        ordering = ['-created', '-updated']



    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("books:detail", kwargs={"slug": self.slug})






###### Functions

def create_slug(instance):
    slug = instance.name.replace(' ', '-').replace('.','-')
    qs = Book.objects.filter(slug = slug)
    exists = qs.exists()
    if exists:
        slug = "%s-%s" %(slug,instance.id)
    return slug



###### Signals

@receiver(post_save, sender=Book)
def post_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
        instance.save()
