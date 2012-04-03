from django.conf.urls.defaults import patterns, url
from route import route

urlpatterns = patterns('categoria.views',
    url(r'^$','index',name='index'),
    url(r'^(?P<pesquisar>\w+)/$','pesquisar',name='pesquisar'),
    #url(r'(\d+)/sucesso/$','success', name='success'),
)
