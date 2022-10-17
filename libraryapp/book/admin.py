from atexit import register
from django.contrib import admin
from django.contrib import admin
from .models import Book

# Register your models here.


class AdminBook(admin.ModelAdmin):
    list_display=['name','picture','author','email', 'describe']
admin.site.register(Book,AdminBook)
# @ admin register()