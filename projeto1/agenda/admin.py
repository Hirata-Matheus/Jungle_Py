from django.contrib import admin

from .models import Pessoa, Compromisso

class PessoaAdmin(admin.ModelAdmin):
    list_display = ("Nome","Email", "Telefone", "Dtanas")
    
class CompromissoAdmin(admin.ModelAdmin):
    list_display = ("Data", "Hora", "Titulo", "Detalhes")

admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Compromisso, CompromissoAdmin)
