# -*- coding: utf-8 -*-

from django.contrib import admin
from models import Categoria

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome','descricao')
    search_fields = ('nome','descricao')
    list_filter = ['nome']

admin.site.register(Categoria, CategoriaAdmin)
