from rest_framework import serializers
from .models import Aluno, Empresa, Instituicao, Orientador, TermoDeCompromisso, Documento, RelatorioSemestral, Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password', 'tipo']

    def create(self, validated_data):
        password = validated_data.pop('password')
        usuario = Usuario(**validated_data)
        usuario.set_password(password)
        usuario.save()
        return usuario

class AlunoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer()

    class Meta:
        model = Aluno
        fields = [
            'id',
            'usuario',
            'cpf',
            'matricula',
            'curso',
            'periodo',
            'orientador',
        ]

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario_data['tipo'] = Usuario.TipoUsuario.ALUNO
        usuario = UsuarioSerializer().create(usuario_data)
        return Aluno.objects.create(usuario=usuario, **validated_data)


class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresa
        fields = [
            'id',
            'email',
            'cnpj',
            'razao_social',
            'ramo_atividade',
            'supervisor',
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
    usuario = UsuarioSerializer()

    class Meta:
        model = Orientador
        fields = [
            'id',
            'usuario',
            'siape',
            'areaAtuacao',
            'instituicao',
        ]

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario_data['tipo'] = Usuario.TipoUsuario.ORIENTADOR
        usuario = UsuarioSerializer().create(usuario_data)
        return Orientador.objects.create(usuario=usuario, **validated_data)


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
