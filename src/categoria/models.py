# -*- coding: utf-8 -*-

from django.db import models

class Categoria(models.Model):
    nome = models.CharField('Nome',max_length=50, unique=True)
    descricao = models.CharField('Descrição',max_length=100)

    def _unicode__(self):
        return self.name

    class Meta:
        ordering = ['nome']
        verbose_name = u"Categoria"
        verbose_name_plural = u"Categorias"
