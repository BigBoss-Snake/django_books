from django.contrib import admin

from .models import Authors, Books

class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')
    

class BooksAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'author_book')
    list_filter = ('author', 'title', 'author_book')

# admin.site.register(Authors)
# admin.site.register(Books)
admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Books, BooksAdmin)

