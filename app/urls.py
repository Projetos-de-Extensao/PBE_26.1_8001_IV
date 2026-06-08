# app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (       
    AlunoViewSet,
    DocumentoViewSet,
    EmpresaViewSet,
    InstituicaoViewSet,
    OrientadorViewSet,
    RelatorioSemestralViewSet,
    TermoDeCompromissoViewSet,
)

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'empresas', EmpresaViewSet)
router.register(r'instituicoes', InstituicaoViewSet)
router.register(r'orientadores', OrientadorViewSet)
router.register(r'termos', TermoDeCompromissoViewSet)
router.register(r'documentos', DocumentoViewSet)
router.register(r'relatorios', RelatorioSemestralViewSet)

urlpatterns = [
    path('', include(router.urls)),
]