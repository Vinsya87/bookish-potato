from django.contrib import admin

from .models import Author, Genres, Titles, Categories


class TitlesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'author', 'year', 'title_urls', 'category')
    search_fields = ('title', 'author')
    list_filter = ('year', 'category',)
    empty_value_display = '-пусто-'


admin.site.register(Titles, TitlesAdmin)
admin.site.register(Author)
admin.site.register(Genres)
admin.site.register(Categories)
