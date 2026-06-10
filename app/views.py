from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
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
    queryset = Aluno.objects.select_related('usuario', 'orientador').all()
    serializer_class = AlunoSerializer
    permission_classes = [AllowAny]


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class InstituicaoViewSet(viewsets.ModelViewSet):
    queryset = Instituicao.objects.all()
    serializer_class = InstituicaoSerializer



class OrientadorViewSet(viewsets.ModelViewSet):
    queryset = Orientador.objects.select_related('usuario', 'instituicao').all()
    serializer_class = OrientadorSerializer

class TermoDeCompromissoViewSet(viewsets.ModelViewSet):
    queryset = TermoDeCompromisso.objects.select_related(
        'aluno',
        'empresa'
    ).all()
    serializer_class = TermoDeCompromissoSerializer
    permission_classes = [IsAuthenticated]
    @action(detail=False, methods=['post'], url_path='avaliar-termo')
    def avaliar_termo(self, request):
        """
        Endpoint do Link Mágico: POST /api/termos/avaliar-termo/
        Espera receber: {"token": "UUID", "decisao": "aprovar" ou "reprovar"}
        """
        token = request.data.get('token')
        decisao = request.data.get('decisao')

        # Trava de segurança: Verifica se quem está logado é do tipo Orientador
        if getattr(request.user, 'tipo', '') != 'orientador':
            return Response(
                {"erro": "Acesso negado. Apenas professores orientadores podem avaliar termos."}, 
                status=status.HTTP_403_FORBIDDEN
            )

        # Busca o termo específico usando o token do Deep Link
        termo = get_object_or_404(TermoDeCompromisso, token_validacao=token)

        # Processa a decisão
        if decisao == 'aprovar':
            termo.statusJuridico = TermoDeCompromisso.StatusJuridico.ATIVO
            termo.save()
            
            # Avisa a empresa e o aluno
            send_mail(
                subject='Estágio Aprovado!',
                message=f'O termo de compromisso do aluno {termo.aluno.usuario.username} foi validado.',
                from_email='sistema.estagios@instituicao.edu.br',
                recipient_list=[termo.empresa.email, termo.aluno.usuario.email],
                fail_silently=True
            )
            return Response({"mensagem": "Termo aprovado com sucesso!"}, status=status.HTTP_200_OK)

        elif decisao == 'reprovar':
            termo.statusJuridico = TermoDeCompromisso.StatusJuridico.REPROVADO
            termo.save()
            
            # Avisa apenas o aluno para correção
            send_mail(
                subject='Estágio Reprovado',
                message='Seu termo de compromisso foi negado pelo orientador. Acesse o sistema.',
                from_email='sistema.estagios@instituicao.edu.br',
                recipient_list=[termo.aluno.usuario.email],
                fail_silently=True
            )
            return Response({"mensagem": "Termo reprovado e aluno notificado."}, status=status.HTTP_200_OK)

        return Response({"erro": "Decisão inválida. Use 'aprovar' ou 'reprovar'."}, status=status.HTTP_400_BAD_REQUEST)


class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer



class RelatorioSemestralViewSet(viewsets.ModelViewSet):
    queryset = RelatorioSemestral.objects.select_related('aluno', 'documento').all()
    serializer_class = RelatorioSemestralSerializer