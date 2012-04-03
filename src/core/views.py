from django.shortcuts  import  render_to_response
from django.template import RequestContext
from datetime import datetime

def homepage(request,template=None):
    contagem = 18 - datetime.now().day
    context = RequestContext(request)
    return  render_to_response ('core/'+template, locals(), context)
