from django.contrib import admin
from contact import models

# Decorator admin register
@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    #mostrar dados no admin com list display com tupla
    list_display = 'id','firstname', 'lastname', 'phone', 'email',
    ordering = 'id', # ordem crescente default (-id descrescente)
    #list_filter = 'created_date', # ativar filtro no admin
    search_fields = 'firstname', 'lastname', # campo de pesquisa
    list_per_page = 10 # pagina por quantidade de registro (nao tupla)
    list_max_show_all = 1 # listar x quantidade de valores enibe o mostrar tudo
    #list_editable = 'firstname', 'lastname', # editar valor direto no admin
    list_display_links = 'id', 'phone', # link do campo para edicao 