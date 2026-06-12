---
id: diagrama_de_casos_de_uso
title: Diagrama de Casos de Uso
---


```kroki-plantuml
@startuml Sistema_Gestao_Estagios_CasosDeUso

left to right direction
skinparam actorStyle awesome

actor Aluno
actor Empresa
actor Administrador
actor Sistema as "Sistema"

usecase (UC01: Cadastro de Aluno) as UC01
usecase (Preencher Dados Pessoais) as UC01_1
usecase (Enviar Formulário de Cadastro) as UC01_2
usecase (Validar Dados do Aluno) as UC01_3
usecase (Dados Inválidos) as FA01

usecase (UC02: Login) as UC02
usecase (Informar E-mail e Senha) as UC02_1
usecase (Validar Credenciais) as UC02_2
usecase (Credenciais Inválidas) as FA02

usecase (UC03: Visualizar Vagas) as UC03
usecase (Listar Vagas Disponíveis) as UC03_1
usecase (Aplicar Filtros) as UC03_2
usecase (Nenhuma Vaga Disponível) as FA03

usecase (UC04: Candidatar-se a Vaga) as UC04
usecase (Selecionar Vaga) as UC04_1
usecase (Registrar Candidatura) as UC04_2
usecase (Vaga Encerrada) as FA04

usecase (UC05: Acompanhar Candidatura) as UC05
usecase (Consultar Status da Candidatura) as UC05_1
usecase (Nenhuma Candidatura Encontrada) as FA05

usecase (UC06: Cadastro de Empresa) as UC06
usecase (Preencher Dados Institucionais) as UC06_1
usecase (Enviar Cadastro da Empresa) as UC06_2
usecase (Validar Dados da Empresa) as UC06_3
usecase (Dados da Empresa Inválidos) as FA06

usecase (UC07: Cadastro de Vaga) as UC07
usecase (Preencher Informações da Vaga) as UC07_1
usecase (Enviar Cadastro da Vaga) as UC07_2
usecase (Dados Incompletos) as FA07

usecase (UC08: Visualizar Candidatos) as UC08
usecase (Listar Candidatos) as UC08_1
usecase (Nenhum Candidato) as FA08

usecase (UC09: Aprovar/Rejeitar Candidato) as UC09
usecase (Selecionar Candidato) as UC09_1
usecase (Atualizar Status do Candidato) as UC09_2
usecase (Erro no Sistema) as FA09

usecase (UC10: Gerenciar Usuários) as UC10
usecase (Visualizar Usuários Cadastrados) as UC10_1
usecase (Editar Usuário) as UC10_2
usecase (Remover Usuário) as UC10_3
usecase (Usuário Não Encontrado) as FA10

usecase (UC11: Aprovar Vaga) as UC11
usecase (Analisar Dados da Vaga) as UC11_1
usecase (Publicar Vaga) as UC11_2
usecase (Rejeitar Vaga) as UC11_3
usecase (Dados Inconsistentes) as FA11

usecase (UC12: Gerar Relatórios) as UC12
usecase (Selecionar Critérios) as UC12_1
usecase (Emitir Relatório) as UC12_2
usecase (Sem Dados Suficientes) as FA12

Aluno --> UC01
Aluno --> UC02
Aluno --> UC03
Aluno --> UC04
Aluno --> UC05

Empresa --> UC06
Empresa --> UC02
Empresa --> UC07
Empresa --> UC08
Empresa --> UC09

Administrador --> UC02
Administrador --> UC10
Administrador --> UC11
Administrador --> UC12

Sistema --> UC01_3
Sistema --> UC02_2
Sistema --> UC03_1
Sistema --> UC04_2
Sistema --> UC05_1
Sistema --> UC06_3
Sistema --> UC08_1
Sistema --> UC09_2
Sistema --> UC10_1
Sistema --> UC11_1
Sistema --> UC12_2

UC01 --> UC01_1 : <<include>>
UC01 --> UC01_2 : <<include>>
UC01 --> UC01_3 : <<include>>

UC02 --> UC02_1 : <<include>>
UC02 --> UC02_2 : <<include>>

UC03 --> UC03_1 : <<include>>
UC03 --> UC03_2 : <<extend>>

UC04 --> UC04_1 : <<include>>
UC04 --> UC04_2 : <<include>>

UC05 --> UC05_1 : <<include>>

UC06 --> UC06_1 : <<include>>
UC06 --> UC06_2 : <<include>>
UC06 --> UC06_3 : <<include>>

UC07 --> UC07_1 : <<include>>
UC07 --> UC07_2 : <<include>>
UC07 --> UC11 : <<include>>

UC08 --> UC08_1 : <<include>>

UC09 --> UC09_1 : <<include>>
UC09 --> UC09_2 : <<include>>

UC10 --> UC10_1 : <<include>>
UC10 --> UC10_2 : <<extend>>
UC10 --> UC10_3 : <<extend>>

UC11 --> UC11_1 : <<include>>
UC11 --> UC11_2 : <<extend>>
UC11 --> UC11_3 : <<extend>>

UC12 --> UC12_1 : <<include>>
UC12 --> UC12_2 : <<include>>

FA01 .> UC01_3 : <<extend>>
FA02 .> UC02_2 : <<extend>>
FA03 .> UC03_1 : <<extend>>
FA04 .> UC04_2 : <<extend>>
FA05 .> UC05_1 : <<extend>>
FA06 .> UC06_3 : <<extend>>
FA07 .> UC07_2 : <<extend>>
FA08 .> UC08_1 : <<extend>>
FA09 .> UC09_2 : <<extend>>
FA10 .> UC10_1 : <<extend>>
FA11 .> UC11_1 : <<extend>>
FA12 .> UC12_2 : <<extend>>

note right of UC04
  Pré-condição: Aluno logado.
  Pós-condição: Candidatura registrada.
end note

note right of UC11
  Pré-condição: Vaga cadastrada pela empresa.
  Pós-condição: Vaga publicada ou recusada.
end note

@enduml
```

---
id: diagrama_de_casos_de_uso
title: Diagrama de Casos de Uso
---

# Projeto de Arquitetura: Casos de Uso (V2.0)

Este documento detalha as interações entre os usuários (Aluno e Orientador) e o sistema. Na Versão 2.0, as interações foram simplificadas e a figura do **Sistema Temporal (Cron)** foi adicionada para lidar com as regras assíncronas estipuladas pela Lei 11.788/08.

---

## 1. Descrição dos Casos de Uso

### UC01 - Autenticar no Sistema (Login)
**Atores:** Aluno, Orientador.  
**Pré-condição:** Usuário previamente cadastrado na base de dados.  
**Fluxo Principal:**
1. O usuário acessa a tela de login.
2. O usuário insere e-mail e senha.
3. O sistema valida as credenciais.
4. O sistema concede o acesso baseado no perfil do usuário.
**Fluxos Alternativos:**
- FA01 (Credenciais Inválidas): O sistema não encontra o usuário ou a senha está incorreta. Exibe mensagem de erro e bloqueia o acesso.
**Pós-condição:** Usuário autenticado e sessão iniciada.

---

### UC02 - Enviar Termo e Dados da Empresa
**Atores:** Aluno.  
**Pré-condição:** Aluno autenticado no sistema.  
**Fluxo Principal:**
1. O aluno acessa a área de envio de documentos.
2. Preenche os dados passivos da Empresa (CNPJ, Razão Social, Supervisor).
3. Preenche as informações do contrato (Data de Início, Data de Fim, Apólice de Seguro).
4. Anexa o arquivo PDF do Termo de Compromisso.
5. O sistema engatilha automaticamente a validação de conformidade legal (UC03).
6. O sistema salva o registro e define o status.
**Fluxos Alternativos:**
- FA01 (Dados Incompletos): O aluno não preenche campos obrigatórios. O sistema alerta e impede o envio.
**Pós-condição:** Termo registrado no banco de dados.

---

### UC03 - Avaliar Termo via Link
**Atores:** Orientador.  
**Pré-condição:** Orientador autenticado na API e de posse do link recebido por e-mail.  
**Fluxo Principal:**
1. O orientador acessa seu e-mail e clica no Link contendo o Token UUID único.
2. O sistema valida se o usuário logado é realmente um Orientador.
3. O sistema atualiza o status jurídico do termo (Ativo ou Reprovado).
4. O sistema dispara um aviso para o aluno e para a empresa sobre o resultado.
**Fluxos Alternativos:**
- FA01 (Acesso Negado): Um Aluno tenta acessar o link ou o Orientador não está logado. O sistema retorna Erro 403 (Proibido).
- FA02 (Token Inválido): O UUID não existe na base. O sistema retorna Erro 404 (Não Encontrado).
**Pós-condição:** Contrato processado e auditado.

---

### UC04 - Emitir Consolidado Diário
**Atores:** Sistema Temporal (Cron).  
**Pré-condição:** Existência de Termos ativados automaticamente na data corrente.  
**Fluxo Principal:**
1. O script de segundo plano é executado às 23:59.
2. O sistema filtra todos os contratos ativos no dia agrupando por Orientador.
3. O sistema monta uma lista contendo os alunos de cada professor.
4. Dispara um único e-mail de resumo diário para a caixa de entrada de cada Orientador.
**Pós-condição:** Orientadores notificados sem excesso de *spam*.

---

### UC05 - Cobrar Relatório Semestral
**Atores:** Sistema Temporal (Cron).  
**Pré-condição:** Existência de Termos de Compromisso com status Ativo.  
**Fluxo Principal:**
1. O script é executado pelo servidor em rotina diária.
2. O sistema calcula a diferença entre a data atual e a `dataInicio` de cada contrato.
3. Ao bater a marca de múltiplos de 180 dias, o sistema gera uma pendência invisível no banco de dados.
4. O sistema dispara um e-mail de cobrança legal obrigatória para o aluno.
**Pós-condição:** Cumprimento automático da exigência periódica do Art. 7º da Lei 11.788/08.

---

## 2. Diagrama Visual

O diagrama abaixo ilustra as interações descritas, separando as ações ativas dos usuários humanos das ações autônomas executadas pelo servidor (Cron).

```kroki-plantuml
@startuml Sistema_Gestao_Estagios_CasosDeUso_V2

left to right direction
skinparam actorStyle awesome
skinparam monochrome true
skinparam shadowing false

' Definição dos Atores
actor "Aluno" as aluno
actor "Orientador" as orientador
actor "Sistema Temporal\n(Cron)" as cron

' Delimitação do Sistema
rectangle "Sistema de Gestão de Estágios V2.0" {
    
    usecase (UC01: Autenticar no Sistema) as UC01
    
    usecase (UC02: Enviar Termo e Dados da Empresa) as UC02
    usecase (Validar Conformidade Legal) as valida_lei
    
    usecase (UC03: Avaliar Termo via Link Mágico) as UC03
    
    usecase (UC04: Emitir Consolidado Diário) as UC04
    
    usecase (UC05: Cobrar Relatório Semestral) as UC05
    usecase (Criar Pendência no Banco) as cria_pendencia

}

' Relações dos Usuários Humanos
aluno --> UC01
orientador --> UC01

aluno --> UC02
UC02 ..> valida_lei : <<include>>

orientador --> UC03

' Relações da Automação (Robôs de Segundo Plano)
cron --> UC04
cron --> UC05
UC05 ..> cria_pendencia : <<include>>

' Notas explicativas
note right of valida_lei
  Inspeciona se falta seguro
  ou se a duração excede 2 anos
  (Art. 9º).
end note

note right of UC03
  Substitui a navegação em
  painéis. Ação feita via
  token UUID seguro.
end note

@enduml