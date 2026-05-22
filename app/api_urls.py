# app/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.api import (
    AlunoViewSet,
    EmpresaViewSet,
    InstituicaoViewSet,
    OrientadorViewSet,
    TermoDeCompromissoViewSet,
    DocumentoViewSet,
    RelatorioSemestralViewSet,
)

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'empresas', EmpresaViewSet)
router.register(r'instituicoes', InstituicaoViewSet)
router.register(r'orientadores', OrientadorViewSet)
router.register(r'termos', TermoDeCompromissoViewSet)
router.register(r'documentos', DocumentoViewSet)
router.register(r'relatoriosemestral', RelatorioSemestralViewSet)

urlpatterns = [
    path('', include(router.urls)),
]