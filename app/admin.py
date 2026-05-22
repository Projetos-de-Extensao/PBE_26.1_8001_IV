from django.contrib import admin
from .models import Aluno, Empresa, Instituicao, Orientador, TermoDeCompromisso, Documento, RelatorioSemestral

admin.site.register(Aluno)
admin.site.register(Empresa)
admin.site.register(Instituicao)
admin.site.register(Orientador)
admin.site.register(TermoDeCompromisso)
admin.site.register(Documento)
admin.site.register(RelatorioSemestral)