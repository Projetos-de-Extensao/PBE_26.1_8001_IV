from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from app.models import TermoDeCompromisso, Documento, RelatorioSemestral

class Command(BaseCommand):
    help = "Monitora contratos ativos e cobra o Relatório Semestral a cada marco de 6 meses."

    def handle(self, *args, **options):
        hoje = timezone.now().date()
        
        termos_ativos = TermoDeCompromisso.objects.filter(
            statusJuridico=TermoDeCompromisso.StatusJuridico.ATIVO
        ).select_related('aluno__usuario', 'empresa')

        for termo in termos_ativos:
            dias_decorridos = (hoje - termo.dataInicio).days

            if dias_decorridos > 0 and (dias_decorridos % 180 == 0):
                
                documento_relatorio = Documento.objects.create(
                    tipo='Relatório',
                    hashSHA256='PENDENTE_PREENCHIMENTO_ALUNO',
                    valido=False,
                    termo=termo
                )

                RelatorioSemestral.objects.get_or_create(
                    aluno=termo.aluno,
                    documento=documento_relatorio,
                    dataReferencia=hoje,
                    defaults={'resumoAtividades': 'Aguardando o preenchimento das atividades pelo aluno.'}
                )

                send_mail(
                    subject="Urgente: Prazo de Relatório Semestral de Estágio Aberto",
                    message=(
                        f"Olá, {termo.aluno.usuario.username}.\n\n"
                        f"Seu contrato de estágio na empresa {termo.empresa.razao_social} atingiu o marco de 6 meses.\n"
                        f"Conforme as exigências do Art. 7º da Lei nº 11.788/08, é obrigatório o envio do relatório de atividades.\n\n"
                        f"O prazo para preenchimento já está aberto no sistema. Acesse o portal para enviar as informações."
                    ),
                    from_email="sistema.estagios@instituicao.edu.br",
                    recipient_list=[termo.aluno.usuario.email],
                    fail_silently=True
                )

        self.stdout.write(self.style.SUCCESS('Comando despertador_relatorio executado com sucesso!'))