from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Aluno, Documento, Empresa, Instituicao, Orientador, RelatorioSemestral, TermoDeCompromisso
from .serializers import (
    AlunoSerializer,
    EmpresaSerializer,
    InstituicaoSerializer,
    OrientadorSerializer,
    TermoDeCompromissoSerializer,
    DocumentoSerializer,
    RelatorioSemestralSerializer
)


class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nome', 'matricula']


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nome', 'cnpj']

class InstituicaoViewSet(viewsets.ModelViewSet):
    queryset = Instituicao.objects.all()
    serializer_class = InstituicaoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nome', 'cnpj']


class OrientadorViewSet(viewsets.ModelViewSet):
    queryset = Orientador.objects.all()
    serializer_class = OrientadorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nome', 'cpf']


class TermoDeCompromissoViewSet(viewsets.ModelViewSet):
    queryset = TermoDeCompromisso.objects.all()
    serializer_class = TermoDeCompromissoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['=id', 'status']

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['nome', 'tipo']


class RelatorioSemestralViewSet(viewsets.ModelViewSet):
    queryset = RelatorioSemestral.objects.all()
    serializer_class = RelatorioSemestralSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['=id', 'status']
