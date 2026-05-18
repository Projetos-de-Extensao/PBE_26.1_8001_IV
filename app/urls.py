# app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import (       
    AlunoViewSet,
    EmpresaViewSet,
    InstituicaoViewSet,
    OrientadorViewSet,
    TermoDeCompromissoViewSet,
)

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'empresas', EmpresaViewSet)
router.register(r'instituicoes', InstituicaoViewSet)
router.register(r'orientadores', OrientadorViewSet)
router.register(r'termos', TermoDeCompromissoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]