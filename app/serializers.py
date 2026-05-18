from rest_framework import serializers
from .models import Aluno, Empresa, Instituicao, Orientador, TermoDeCompromisso


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'


class InstituicaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instituicao
        fields = '__all__'


class OrientadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orientador
        fields = '__all__'


class TermoDeCompromissoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermoDeCompromisso
        fields = '__all__'