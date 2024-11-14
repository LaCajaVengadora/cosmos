from django.contrib import admin
from blog_app.models import *
# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'author']
    search_fields = ['author', 'id']
    #list_filter = ['aut']
    #readonly_fields = ['date']
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'display_topic', 'date', 'author']
    search_fields = ['id', 'author__username', 'title', ]
    list_filter = ['topic', 'date']
    def display_topic(self, obj): return " - ".join([t.name for t in obj.topic.all()])
    display_topic.short_description = 'Topics'
    #readonly_fields = ['date']


admin.site.register(Comment, CommentAdmin); admin.site.register(Topic); admin.site.register(Post, PostAdmin)