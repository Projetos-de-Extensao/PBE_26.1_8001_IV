from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
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



class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class InstituicaoViewSet(viewsets.ModelViewSet):
    queryset = Instituicao.objects.all()
    serializer_class = InstituicaoSerializer



class OrientadorViewSet(viewsets.ModelViewSet):
    queryset = Orientador.objects.all()
    serializer_class = OrientadorSerializer

class TermoDeCompromissoViewSet(viewsets.ModelViewSet):
    queryset = TermoDeCompromisso.objects.select_related(
        'aluno',
        'empresa'
    ).all()
    serializer_class = TermoDeCompromissoSerializer


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer



class RelatorioSemestralViewSet(viewsets.ModelViewSet):
    queryset = RelatorioSemestral.objects.all()
    serializer_class = RelatorioSemestralSerializer