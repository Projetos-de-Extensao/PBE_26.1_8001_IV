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

---
id: diagrama_de_classes
title: Diagrama de Classes
---

# Projeto de Arquitetura: Diagrama de Classes (V2.0)

Este documento detalha a estrutura de dados e as relações entre as entidades do Sistema de Gestão de Estágios, integrando as regras da Lei 11.788/08, a lógica de validação automática e as rotinas temporais de segundo plano.

## Detalhamento das Entidades e Atributos

A tabela abaixo descreve os atributos reais mapeados no banco de dados. Note que **Aluno** e **Orientador** possuem vínculos com a entidade **Usuário** (pois possuem acesso ao sistema), enquanto a **Empresa** atua como uma entidade estritamente passiva.

| Classe | Atributo | Tipo | Descrição |
| :--- | :--- | :--- | :--- |
| **Usuário** | `username` | String | Nome de acesso para os perfis ativos (Aluno e Orientador). |
| | `email` | String | E-mail utilizado para login, envio do consolidado diário e Links Mágicos. |
| | `password` | String | Senha criptografada do usuário. |
| | `tipo` | Enum | Define as permissões (`ALUNO` ou `ORIENTADOR`). |
| **Aluno** | `cpf` | String | Campo *write_only* (LGPD) para fins de Termo de Compromisso. |
| | `matricula` | String | Identificador acadêmico único. |
| | `curso` | String | Curso de graduação atual. |
| | `periodo` | Int | Período vigente. |
| **Empresa** | `cnpj` | String | Identificação jurídica da concedente (Entidade Passiva). |
| | `razao_social` | String | Razão social registrada. |
| | `supervisor` | String | Nome do profissional responsável na empresa. |
| **Instituição** | `nomeUnidade` | String | Identificação do campus (ex: Ibmec RJ). |
| | `coordenador` | String | Responsável institucional pela validação final. |
| **Orientador** | `siape` | String | Identificação do docente responsável. |
| | `areaAtuacao` | String | Vincula o professor à área de conhecimento do estágio. |
| **Termo de Compromisso**| `dataInicio` | Date | Período de vigência para gatilho do robô de 6 meses. |
| | `dataFim` | Date | Período para controle do limite legal de 2 anos. |
| | `apoliceSeguro` | String | Apólice obrigatória contra acidentes (Art. 9º). |
| | `statusJuridico` | Enum | Estado: `Pendente`, `Ativo`, `Reprovado` ou `Concluído`. |
| | `token_validacao` | UUID | Chave criptográfica única *read_only* para uso no Link Mágico. |
| **Documento** | `tipo` | String | Categoria do arquivo (Termo ou Relatório). |
| | `hashSHA256` | String | Identificador de integridade gerado no upload. |
| | `valido` | Boolean | Define se o documento não foi adulterado. |
| **Relatório Semestral**| `resumoAtividades` | Text | Conteúdo enviado a cada 6 meses (Art. 7º). |
| | `dataReferencia` | Date | Preenchido automaticamente pelo Cron Job. |

## Diagrama de Classes Conceitual

O diagrama abaixo apresenta a arquitetura V2.0. Destaca-se a composição de herança de usuários, os métodos do motor de validação no `TermoDeCompromisso` e a presença do `Sistema_Automato` (Cron).

```kroki-plantuml
@startuml Sistema_Gestao_Estagios_DiagramaFinal

' Configurações Visuais
left to right direction
skinparam shadowing false
skinparam monochrome true
skinparam classAttributeIconSize 0

' Definição das Classes
class Usuario {
    + id: int
    + username: string
    + email: string
    + password: string
    + tipo: string
}

class Aluno {
    + id: int
    + matricula: string
    + cpf: string
    + curso: string
    + periodo: int
}

class Empresa {
    + id: int
    + cnpj: string
    + razao_social: string
    + supervisor: string
}

class Instituicao {
    + id: int
    + nomeUnidade: string
    + coordenador: string
}

class Orientador {
    + id: int
    + siape: string
    + areaAtuacao: string
}

class TermoDeCompromisso {
    + id: int
    + dataInicio: Date
    + dataFim: Date
    + apoliceSeguro: string
    + statusJuridico: string
    + token_validacao: UUID
    + executar_validacao_automatica(): string
    + save(): void
}

class Documento {
    + id: int
    + tipo: string
    + hashSHA256: string
    + valido: boolean
}

class RelatorioSemestral {
    + id: int
    + resumoAtividades: text
    + dataReferencia: Date
}

class Sistema_Automato <<Boundary>> {
    + consolidado_diario(): void
    + despertador_relatorio(): void
}

' Relacionamentos
Aluno "1" *-- "1" Usuario : possui login >
Orientador "1" *-- "1" Usuario : possui login >

Instituicao "1" *-- "0..*" Orientador : possui >
Aluno "0..*" --> "1" Orientador : supervisionado por >

TermoDeCompromisso "0..*" --> "1" Aluno : realiza <
TermoDeCompromisso "0..*" --> "1" Empresa : vincula-se a >

Documento "0..*" --> "1" TermoDeCompromisso : pertence a >
RelatorioSemestral "0..*" --> "1" Aluno : enviado por >
RelatorioSemestral "1" *-- "1" Documento : materializa-se em >

Sistema_Automato ..> TermoDeCompromisso : monitora tempo >
Sistema_Automato ..> RelatorioSemestral : gera pendência >

@enduml
```