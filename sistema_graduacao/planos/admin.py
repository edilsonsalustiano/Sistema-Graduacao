from django.contrib import admin


class PlanoAdmin(admin.ModelAdmin):
    list_display = ['nome_plano', 'valor_plano']
