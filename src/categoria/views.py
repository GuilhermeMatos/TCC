# -*- encoding: utf-8 -*-
from django.shortcuts  import  render_to_response
from django.template import RequestContext
from models import Categoria

def index(request):
    sc = Categoria.objects.all()
    context = RequestContext(request)
    return  render_to_response ('categoria/index.html', locals(), context)

def pesquisar(request,pesquisar=None):
    sc = Categoria.objects.filter(nome__startswith=pesquisar)
    context = RequestContext(request)
    return  render_to_response ('categoria/index.html', locals(), context)