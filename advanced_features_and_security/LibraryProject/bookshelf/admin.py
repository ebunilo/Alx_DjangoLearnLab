from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser


# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('author', 'publication_year')
    

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username')
    


admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
