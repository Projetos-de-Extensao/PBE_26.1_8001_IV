---
id: diagrama_de_classes
title: Diagrama de Classes
---

## Classes:

### Detalhamento das Entidades e Atributos

A tabela abaixo descreve os dados que cada classe será responsável por armazenar no sistema de gestão de estágios, servindo como base para o desenvolvimento do banco de dados.

## Dicionário de Classes (Entidades do Sistema)

| Classe | Atributo | Descrição | Regra de Negócio |
| :--- | :--- | :--- | :--- |
| **Aluno** | `matricula` | ID único do estudante | Identificação obrigatória Ibmec |
| **Empresa** | `cnpj` | Cadastro da empresa | Identificação do vínculo empregatício |
| **Empresa** | `acordo_cooperacao` | Número do convênio | Deve estar ativo para permitir o estágio |
| **Estágio** | `data_inicio` | Início das atividades | Validação de 30 dias de retroatividade |
| **Estágio** | `data_fim` | Término previsto | Soma de períodos não pode exceder 24 meses |
| **Estágio** | `apolice_seguro` | Número da apólice | Obrigatório para emissão do contrato |
| **Estágio** | `status_estagio` | Fase atual do contrato | Aberto / Ativo / Pendente Doc / Encerrado|
| **Documento** | `data_recebimento` | Entrega na secretaria | Inicia o SLA de 5 dias úteis |
| **Documento** | `status` | Situação da assinatura | Pendente / Validado / Rejeitado |
| **Supervisor**| `nome_supervisor` | Responsável técnico | Deve assinar a Avaliação de Desempenho |

## Arquitetura do Sistema (Visão Geral)

```kroki-plantuml
@startuml
' Configurações de estilo para clareza visual
skinparam monochrome true
skinparam shadowing false
hide circle
hide members

title Diagrama de Estrutura de Estágios - Ibmec (Foco em Classes)

' Definição das Classes Principais
class Aluno
class Empresa
class Supervisor
class Secretaria
class Estagio

' Agrupamento de Documentos para organização visual
package "Documentação e Fluxo" {
    abstract class Documento
    class TermoCompromisso
    class TermoAditivo
    class TermoRescisao
    class RelatorioAcompanhamento
    class AvaliacaoDesempenho
}

' Relacionamentos e Multiplicidade
Aluno "1" -- "0..*" Estagio : realiza >
Empresa "1" -- "0..*" Estagio : concede >
Empresa "1" *-- "1..*" Supervisor : possui >
Estagio "1" *-- "1..*" Documento : possui >

Secretaria "1" -- "0..*" Documento : valida >
Supervisor "1" -- "0..*" AvaliacaoDesempenho : preenche >

' Hierarquia de Tipos de Documentos
Documento <|-- TermoCompromisso
Documento <|-- TermoAditivo
Documento <|-- TermoRescisao
Documento <|-- RelatorioAcompanhamento
Documento <|-- AvaliacaoDesempenho

' Notas de Regras de Negócio
note "SLA: 5 dias úteis" as N1
Secretaria .. N1
N1 .. Documento

note "Limite: 24 meses" as N2
N2 .. TermoAditivo
@enduml
```
