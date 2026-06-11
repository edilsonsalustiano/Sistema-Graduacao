from django.contrib import admin
from modalidades.models import Modalidade
from planos.models import Plano


@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ('nome_plano', 'valor_plano')
