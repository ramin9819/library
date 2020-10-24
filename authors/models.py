from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone


# Create your models here.


def upload_location(instance,filename):
    return "images/%s/%s" %(instance.id, filename)


class Author(models.Model):
    fullName = models.CharField(max_length=200)
    bio = models.TextField(null=True, blank=True,)
    slug = models.SlugField(unique=True, allow_unicode=True, max_length=200)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    image = models.ImageField(upload_to='images/authors',  #use upload location
                                    null=True,
                                    blank=True,
                                    )
    

    def __str__(self):
        return self.fullName

    def get_absolute_url(self):
        return reverse("authors:detail", kwargs={"slug": self.slug})



    class Meta:
        ordering = ['-created', '-updated']



def create_slug(instance):
    slug = instance.fullName.replace(' ', '-').replace('.','-')
    qs = Author.objects.filter(slug = slug)
    exists = qs.exists()
    if exists:
        slug = "%s-%s" %(slug,instance.id)
    return slug


@receiver(post_save, sender=Author)
def post_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
        instance.save()
