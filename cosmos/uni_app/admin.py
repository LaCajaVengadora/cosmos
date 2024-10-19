from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Cat); admin.site.register(Carrera); admin.site.register(Uni)
admin.site.register(UniImg); admin.site.register(CursoImg)
# ALLOWS ADMIN TO SEE models ON ADMIN PANEL