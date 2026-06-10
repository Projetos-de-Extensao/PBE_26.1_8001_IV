from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from app.models import TermoDeCompromisso, Orientador

class Command(BaseCommand):
    help = "Envia um resumo diário dos novos estágios iniciados hoje para cada orientador."

    def handle(self, *args, **options):
        hoje = timezone.now().date()
        
        orientadores = Orientador.objects.select_related('usuario').all()

        for professor in orientadores:
            termos_novos = TermoDeCompromisso.objects.filter(
                aluno__orientador=professor,
                statusJuridico=TermoDeCompromisso.StatusJuridico.ATIVO,
                dataInicio=hoje
            ).select_related('aluno__usuario', 'empresa')

            if termos_novos.exists():
                lista_alunos = "\n".join([
                    f"- {t.aluno.usuario.username} (Matrícula: {t.aluno.matricula} | Empresa: {t.empresa.razao_social})" 
                    for t in termos_novos
                ])

                send_mail(
                    subject=f"📊 Resumo Diário: Novos Estágios Ativos - {hoje:%d/%m/%Y}",
                    message=(
                        f"Olá, Professor(a) {professor.usuario.username}.\n\n"
                        f"O motor de automação do sistema validou e ativou os contratos dos seguintes alunos hoje:\n\n"
                        f"{lista_alunos}\n\n"
                        f"Nenhuma ação manual é necessária. Os documentos estão em conformidade com a Lei 11.788/08."
                    ),
                    from_email="sistema.estagios@instituicao.edu.br",
                    recipient_list=[professor.usuario.email],
                    fail_silently=True
                )
                
        self.stdout.write(self.style.SUCCESS('Comando consolidado_diario executado com sucesso!'))