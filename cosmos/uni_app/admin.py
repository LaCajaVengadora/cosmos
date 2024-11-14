from django.contrib import admin
from .models import *

# Register your models here.

class UniAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'tipo', 'location']
    search_fields = ['name', 'id', 'location']
    list_filter = ['tipo']
    #readonly_fields = ['date']
class Template(admin.ModelAdmin):
    def display_uni(self, obj): return obj.uni.name
    display_uni.short_description = 'Uni'
    def display_cat(self, obj): return obj.cat.name
    display_cat.short_description = 'Cat'
class CarreraAdmin(Template):
    list_display = ['id', 'name', 'display_uni', 'display_cat', 'precio', 'modalidad', 'duration']
    search_fields = ['id', 'name' ,'uni__name', 'cat__name']
    list_filter = ['cat__name', 'modalidad', 'uni__name']
    #readonly_fields = ['date']
class CursoAdmin(Template):
    list_display = ['id', 'name', 'display_uni', 'display_cat', 'precio', 'modalidad', 'duration']
    search_fields = ['id', 'name' ,'uni__name', 'cat__name']
    list_filter = ['cat__name', 'modalidad', 'uni__name']
class BecaAdmin(Template):
    list_display = ['id', 'name', 'display_uni', 'precio']
    search_fields = ['id', 'name' ,'uni__name']
    list_filter = ['uni__name']


admin.site.register(Cat); admin.site.register(Uni, UniAdmin)
admin.site.register(Carrera, CarreraAdmin); admin.site.register(Curso, CursoAdmin); admin.site.register(Beca, BecaAdmin)
admin.site.register(UniImg); admin.site.register(CursoImg);
# ALLOWS ADMIN TO SEE models ON ADMIN PANEL