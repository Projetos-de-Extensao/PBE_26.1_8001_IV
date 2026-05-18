---
id: diagrama_de_classes
title: Diagrama de Classes
---

# Projeto de Arquitetura: Diagrama de Classes

Este documento detalha a estrutura de dados e as relações entre as entidades do Sistema de Gestão de Estágios, integrando as regras da Lei 11.788/08 e a lógica de validação automática.

## Detalhamento das Entidades e Atributos

A tabela abaixo descreve os atributos planejados, tratando o Orientador como uma entidade de dados vinculada à Instituição de Ensino, conforme as diretrizes de automação do sistema.


| Classe | Atributo | Tipo | Descrição |
| :--- | :--- | :--- | :--- |
| **Usuário** | `nome` | String | Dados de acesso para perfis que interagem com o sistema (Aluno/Empresa). |
| | `email` | String | Dados de acesso para perfis que interagem com o sistema (Aluno/Empresa). |
| | `senha` | String | Dados de acesso para perfis que interagem com o sistema (Aluno/Empresa). |
| **Aluno** | `cpf` | String | Identificadores para fins de Termo de Compromisso e histórico acadêmico. |
| | `matricula` | String | Identificadores para fins de Termo de Compromisso e histórico acadêmico. |
| | `curso` | String | Critérios para validação automática da elegibilidade ao estágio. |
| | `periodo` | Int | Critérios para validação automática da elegibilidade ao estágio. |
| **Empresa** | `cnpj` | String | Identificação jurídica da parte concedente (empresa). |
| | `razaoSocial` | String | Identificação jurídica da parte concedente (empresa). |
| | `supervisor` | String | Nome do profissional responsável pelo acompanhamento na empresa. |
| **Instituição** | `nomeUnidade` | String | Identificação do campus universitário (ex: Ibmec RJ / Ibmec MG). |
| | `coordenador` | String | Responsável institucional pela validação final do convênio de estágio. |
| **Orientador** | `nome` | String | Identificação do docente responsável pela análise pedagógica. |
| | `siape` | String | Identificação do docente responsável pela análise pedagógica. |
| | `areaAtuacao` | String | Vincula o professor ao curso e área de conhecimento do aluno. |
| **Termo de Compromisso**| `dataInicio` | Date | Período de vigência para controle do limite legal de 2 anos. |
| | `dataFim` | Date | Período de vigência para controle do limite legal de 2 anos. |
| | `apoliceSeguro` | String | Número da apólice obrigatória contra acidentes (Art. 9º da Lei 11.788). |
| | `statusJuridico` | Enum | Estado do contrato: `Pendente`, `Ativo` ou `Concluído`. |
| **Documento** | `tipo` | String | Categoria do arquivo (TCE, Plano de Atividades ou Relatório). |
| | `hashSHA256` | String | Identificador de integridade gerado automaticamente no upload. |
| | `valido` | Boolean | Resultado da validação automática realizada pelo sistema. |
| **Relatório Semestral**| `resumoAtividades` | Text | Conteúdo enviado periodicamente pelo aluno a cada 6 meses. |
| | `dataReferencia` | Date | Data para controle do envio obrigatório (Art. 7º). |

## Diagrama de Classes Conceitual

O diagrama abaixo apresenta a arquitetura de relações do sistema. Note que o **Orientador** é representado como uma entidade vinculada à Instituição, sem herança de login, focando na automação da validação.

```kroki-plantuml
@startuml Sistema_Gestao_Estagios_DiagramaFinal

' Configurações Visuais
left to right direction
skinparam shadowing false
skinparam monochrome true
hide circle
hide methods
hide attributes

' Definição das Classes
abstract class Usuario <<Abstract>>
class Aluno
class Empresa
class InstituicaoEnsino
class Orientador #fff9c4 
class TermoCompromisso
class Documento
class RelatorioAtividades

' Herança (Somente perfis com interação direta/login)
Usuario <|-- Aluno
Usuario <|-- Empresa

' Relacionamentos e Multiplicidade
InstituicaoEnsino "1" *-- "0..*" Orientador : possui >
Orientador "1" -- "0..*" Aluno : supervisiona >
Aluno "1" -- "0..*" TermoCompromisso : realiza >
Empresa "1" -- "0..*" TermoCompromisso : cadastra >

' Composição de Documentos e Relatórios
TermoCompromisso "1" *-- "1..*" Documento : contém >
Aluno "1" -- "0..*" RelatorioAtividades : envia >
RelatorioAtividades "1" -- "1" Documento : materializa-se em >

@enduml
```