from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)

    class Meta:
        abstract = True 

    def __str__(self):
        return self.nome
    

class Aluno(Usuario):
    cpf = models.CharField(max_length=14, unique=True)  
    matricula = models.CharField(max_length=20, unique=True)
    curso = models.CharField(max_length=100)
    periodo = models.IntegerField()

    def __str__(self):
        return f"Aluno: {self.nome} ({self.matricula})"
    

class Empresa(Usuario):
    cnpj = models.CharField(max_length=18, unique=True)
    razao_social = models.CharField(max_length=255)
    ramo_atividade = models.CharField(max_length=100)

    def __str__(self):
        return f"Empresa: {self.razao_social}"
  
class Instituicao(models.Model):
    nomeUnidade = models.CharField(max_length=255)
    coordenador = models.CharField(max_length=255)

    def __str__(self):
        return self.nomeUnidade

    class Meta:
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"

class Orientador(models.Model):
    nome = models.CharField(max_length=255)
    siape = models.CharField(max_length=50)
    areaAtuacao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Orientador"
        verbose_name_plural = "Orientadores"

class TermoDeCompromisso(models.Model):

    class StatusJuridico(models.TextChoices):
        PENDENTE = 'Pendente', 'Pendente'
        ATIVO = 'Ativo', 'Ativo'
        CONCLUIDO = 'Concluído', 'Concluído'

    dataInicio = models.DateField()
    dataFim = models.DateField()
    apoliceSeguro = models.CharField(max_length=100)
    statusJuridico = models.CharField(
        max_length=10,
        choices=StatusJuridico.choices,
        default=StatusJuridico.PENDENTE,
    )

    def __str__(self):
        return f"Termo {self.pk} — {self.statusJuridico}"

    class Meta:
        verbose_name = "Termo de Compromisso"
        verbose_name_plural = "Termos de Compromisso"


class Documento(models.Model):

    class TipoDocumento(models.TextChoices):
        TCE = 'TCE', 'TCE'
        PLANO_ATIVIDADES = 'Plano de Atividades', 'Plano de Atividades'
        RELATORIO = 'Relatório', 'Relatório'

    tipo = models.CharField(
        max_length=40,
        choices=TipoDocumento.choices,
    )
    #uso pra garantir a integridade dos dados
    hashSHA256 = models.CharField(max_length=64)

    valido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.tipo}"

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"