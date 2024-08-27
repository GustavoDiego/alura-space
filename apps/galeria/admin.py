from django.contrib import admin
from apps.galeria.models import Fotografia

class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id","nome","legenda","publicado")
    list_display_links = ("id", "nome")
    search_fields = ("nome",) #uso obrigatorio da virgula, pois tem que ser uma tupla
    list_filter = ("categoria","usuario", )
    list_editable = ("publicado",)
    list_per_page = 1

admin.site.register(Fotografia,ListandoFotografias)
