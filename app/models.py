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