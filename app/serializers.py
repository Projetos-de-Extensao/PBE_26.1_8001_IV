from rest_framework import serializers
from .models import Aluno, Empresa, Instituicao, Orientador, TermoDeCompromisso, Documento, RelatorioSemestral


class AlunoSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True)

    class Meta:
        model = Aluno
        fields = [
            'id',
            'nome',
            'email',
            'senha',
            'cpf',
            'matricula',
            'curso',
            'periodo',
            'orientador',
        ]


class EmpresaSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True)

    class Meta:
        model = Empresa
        fields = [
            'id',
            'nome',
            'email',
            'senha',
            'cnpj',
            'razao_social',
            'ramo_atividade',
        ]


class InstituicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituicao
        fields = [
            'id',
            'nomeUnidade',
            'coordenador',
        ]


class OrientadorSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True)

    class Meta:
        model = Orientador
        fields = [
            'id',
            'nome',
            'senha',
            'siape',
            'areaAtuacao',
            'instituicao',
        ]


class TermoDeCompromissoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermoDeCompromisso
        fields = [
            'id',
            'dataInicio',
            'dataFim',
            'apoliceSeguro',
            'statusJuridico',
            'aluno',
            'empresa',
        ]

class DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documento
        fields = [
            'id',
            'tipo',
            'hashSHA256',
            'valido',
            'termo',
        ]

class RelatorioSemestralSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelatorioSemestral
        fields = [
            'id',
            'resumoAtividades',
            'dataReferencia',
            'aluno',
            'documento',
        ]
