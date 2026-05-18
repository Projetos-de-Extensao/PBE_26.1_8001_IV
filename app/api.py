# app/api.py
from rest_framework import viewsets
from app.models import Aluno, Empresa, Instituicao, Orientador, TermoDeCompromisso
from app.serializers import (
    AlunoSerializer,
    EmpresaSerializer,
    InstituicaoSerializer,
    OrientadorSerializer,
    TermoDeCompromissoSerializer,
)

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class InstituicaoViewSet(viewsets.ModelViewSet):
    queryset = Instituicao.objects.all()
    serializer_class = InstituicaoSerializer

class OrientadorViewSet(viewsets.ModelViewSet):
    queryset = Orientador.objects.all()
    serializer_class = OrientadorSerializer

class TermoDeCompromissoViewSet(viewsets.ModelViewSet):
    queryset = TermoDeCompromisso.objects.all()
    serializer_class = TermoDeCompromissoSerializer