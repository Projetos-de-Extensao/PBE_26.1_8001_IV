from django.contrib import admin
from .models import Aluno, Empresa, Instituicao, Orientador, TermoDeCompromisso

admin.site.register(Aluno)
admin.site.register(Empresa)
admin.site.register(Instituicao)
admin.site.register(Orientador)
admin.site.register(TermoDeCompromisso)