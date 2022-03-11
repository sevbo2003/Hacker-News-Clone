from django.contrib import admin
from .models import News, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'points', 'number_of_likes')
    list_filter = ('created',)


admin.site.register(Comment)