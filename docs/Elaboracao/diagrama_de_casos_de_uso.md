---
id: diagrama_de_casos de uso
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
  **Pré-condição**: Aluno logado.
  **Pós-condição**: Candidatura registrada.
end note

note right of UC11
  **Pré-condição**: Vaga cadastrada pela empresa.
  **Pós-condição**: Vaga publicada ou recusada.
end note

@enduml
```