from tkinter.font import names

from django.contrib import admin
from .models import *



# Register your models here.


@admin.register(Post)
class AuthorAdmin(admin.ModelAdmin):

        list_display = ['title' , 'description' , 'status' , 'author']
        list_filter = ['title']
        ordering = ('title',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
       list_display  = ['name']

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['name' , 'email' , 'type']

@admin.register(Comment)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['title' , 'content' , 'active']
    list_filter = ['active']
    list_editable = ['active']