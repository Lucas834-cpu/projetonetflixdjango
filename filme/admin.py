from django.contrib import admin

# Register your models here.
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

# somente existe, pois, queremos que admin apareça o campo personalizado filmes_vistos
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ('filmes_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)
