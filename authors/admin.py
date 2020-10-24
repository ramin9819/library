from django.contrib import admin
from .models import Author
# Register your models here.


class PostModelField(admin.ModelAdmin):
    list_display = ['fullName', 'id']
    

    class Meta:
        model = Author

admin.site.register(Author, PostModelField)
