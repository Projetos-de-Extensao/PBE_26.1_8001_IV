---
id: prototipo_baixa_fidelidade
title: Protótipo de Baixa Fidelidade
---

## Introdução

<p align="justify">
A construção do protótipo de alta fidelidade auxilia a equipe de desenvolvimento a encontrar um nível de detalhes abrangentes, extrair funcionalidades, testar usabilidade, e também fornece uma base para o gerenciamento do projeto pois com o protótipo é possível realizar estimativas de quanto tempo será necessário desempenhar em cada funcionalidade.
</p>

## Metodologia

<p align="justify">
Iniciamos o projeto através dos levantamentos iniciais da equipe, após discussões a ferramenta Figma foi selecionada para produzir o protótipo de alta fidelidade com auxílio do Material Design Color Tool.
</p>

## Protótipo de alta fidelidade

### Versão 1.0

### Tela Login

```kroki-plantuml
@startsalt
{
  Sistema de Gestão de Estágios
  ==
  .
  Email:    | "email@exemplo.com    "
  Senha:    | "*********************"
  .
  [   Entrar   ]
  .
  Não tem conta? | "Cadastre-se"
}
@endsalt
```

## Tela Cadastro Aluno


```kroki-plantuml
@startsalt
{
  Cadastro de Aluno - Primeiro acesso
  ==
  .
  Nome:        | "                    "
  Email:       | "                    "
  Senha:       | "                    "
  CPF:         | "                    "
  Matrícula:   | "                    "
  Curso:       | "                    "
  Período:     | "                    "
  .
  [   Enviar Cadastro   ]
  .
  Já tem conta? | "Faça login"
}
@endsalt
```

## Tela Cadastro Empresa


```kroki-plantuml
@startsalt
{
  Cadastro de Empresa
  ==
  .
  Razão Social: | "                    "
  CNPJ:         | "                    "
  Email:        | "                    "
  Senha:        | "                    "
  Supervisor:   | "                    "
  .
  [   Enviar Cadastro   ]
  .
  Já tem conta? | "Faça login"
}
@endsalt
```

## Tela inicial - Aluno


```kroki-plantuml
@startsalt
{+
  Olá, [Nome do Aluno] | [ Sair ]
  ==
  {T
    + Menu
    ++ Vagas Disponíveis
    ++ Minhas Candidaturas
    ++ Meus Documentos
    ++ Meu Termo de Compromisso
  }
  ==
  Vagas Disponíveis
  --
  Filtrar por: | ^Área de Atuação^ | [ Buscar ]
  .
  {#
    Empresa        | Área          | Bolsa     | Ação
    Empresa ABC    | TI            | R$ 1.500  | [ Candidatar-se ]
    Empresa XYZ    | Engenharia    | R$ 1.200  | [ Candidatar-se ]
    Empresa 123    | Administração | R$ 1.000  | [ Candidatar-se ]
  }
}
@endsalt
```

## Tela de candidatura - Visualização, confirmação e acompanhamento

### Visualização


```kroki-plantuml
@startsalt
{+
  <b>Detalhes da Vaga
  ==
  .
  <b>Empresa:</b> | Empresa ABC
  <b>Cargo:</b>   | Dev Backend (Júnior/Estágio)
  <b>Local:</b>    | Rio de Janeiro, RJ (Híbrido)
  <b>Bolsa:</b>    | A combinar
  .
  -- Descrição da Vaga --
  {
    Atuar no desenvolvimento de APIs REST utilizando Python e Java. 
    Manutenção de bancos de dados e integração de sistemas legados.
    Participação em reuniões de planning e daily com o time de engenharia.
  }
  .
  -- Requisitos --
  * Cursando Engenharia da Computação, Museologia ou áreas afins.
  * Conhecimento básico em SQL e lógica de programação.
  * Proatividade e vontade de aprender novas tecnologias.
  .
  [  Confirmar Candidatura  ] | [ Voltar para Vagas ]
}
@endsalt
```

### Confirmação


```kroki-plantuml
@startsalt
{+
  Candidatura Registrada
  ==
  .
  Sua candidatura foi enviada com sucesso!
  .
  Empresa: | Empresa ABC
  Vaga:    | Dev Backend
  Status:  | Pendente
  .
  [ Ver Minhas Candidaturas ] | [ Voltar para Vagas ]
}
@endsalt
```

### Acompanhamento


```kroki-plantuml
@startsalt
{+
  Olá, [Nome do Aluno] | [ Sair ]
  ==
  Minhas Candidaturas
  --
  .
  {#
    Empresa        | Vaga         | Status
    Empresa ABC    | Dev Backend  | Pendente
    Empresa XYZ    | Estagiário   | Aprovado
  }
}
@endsalt
```

## Telas de documentação

### Termo de compromisso


```kroki-plantuml
@startsalt
{+
  Olá, [Nome do Aluno] | [ Sair ]
  ==
  Meu Termo de Compromisso
  --
  .
  Empresa:          | Empresa ABC
  Supervisor:       | Carlos Mendes
  Data de Início:   | 01/08/2025
  Data de Término:  | 01/08/2026
  Apólice de Seguro:| "123456-APL"
  Status Jurídico:  | Ativo
  .
  Documentos Vinculados:
  {#
    Tipo                 | Válido
    TCE                  | ✔ Sim
    Plano de Atividades  | ✔ Sim
    Relatório Semestral  | ⏳ Pendente
  }
  .
  [ Enviar Documento ] | [ Enviar Relatório Semestral ]
}
@endsalt
```

### Upload de documentos


```kroki-plantuml
@startsalt
{+
  Olá, [Nome do Aluno] | [ Sair ]
  ==
  Enviar Documentos
  --
  .
  Tipo de Documento:
  () TCE
  () Plano de Atividades
  () Relatório Semestral
  .
  Arquivo: | "nenhum arquivo selecionado" | [ Escolher Arquivo ]
  .
  Hash SHA-256: | "gerado automaticamente"
  .
  [   Enviar Documento   ]
}
@endsalt
``` 

### Envio de relatório

```kroki-plantuml
@startsalt
{+
  Olá, [Nome do Aluno] | [ Sair ]
  ==
  Enviar Relatório Semestral
  --
  .
  Data de Referência: | "dd/mm/aaaa"
  .
  Resumo de Atividades:
  "                                        "
  "                                        "
  "                                        "
  "                                        "
  .
  Anexar Documento: | "nenhum arquivo" | [ Escolher Arquivo ]
  .
  [   Enviar Relatório   ]
}
@endsalt`
```

### Resultado de validação

```kroki-plantuml
@startsalt
{+
  Resultado da Validação
  ==
  .
  Arquivo:          | plano_atividades.pdf
  Tipo:             | Plano de Atividades
  Hash SHA-256:     | "a3f5c...d91b"
  .
  --
  () ✔ Documento válido. Arquivo aceito pelo sistema.
  .
  --
  .
  [ Enviar Outro Documento ] | [ Voltar ]
}
@endsalt
```

## Tela Empresa

### Cadastro de vaga

```kroki-plantuml
@startsalt
{+
  Olá, [Nome da Empresa] | [ Sair ]
  ==
  Cadastrar Nova Vaga
  --
  .
  Título da Vaga:  | "                    "
  Área:            | "                    "
  Bolsa (R$):      | "                    "
  Carga Horária:   | "                    "
  Descrição:       | "                    "
  .
  Data de Início:  | "dd/mm/aaaa"
  Data de Término: | "dd/mm/aaaa"
  .
  [   Enviar para Aprovação   ]
}
@endsalt
```

### Visualização de candidatura

```kroki-plantuml
@startsalt
{+
  Olá, [Nome da Empresa] | [ Sair ]
  ==
  Candidatos para: Dev Backend
  --
  .
  {#
    Nome           | Curso      | Período | Ação
    João Silva     | Engenharia | 5°      | [ Aprovar ] | [ Rejeitar ]
    Maria Souza    | TI         | 4°      | [ Aprovar ] | [ Rejeitar ]
    Carlos Lima    | ADS        | 6°      | [ Aprovar ] | [ Rejeitar ]
  }
}
@endsalt
```

## Tela de relatórios - Coordenaçao


### Relatórios pendentes

```kroki-plantuml
@startsalt
{+
  Painel de Relatórios | [ Sair ]
  ==
  Relatórios Aguardando Confirmação de Validação
  --
  .
  {#
    Aluno        | Curso      | Data Ref. | Status                | 
    João Silva   | Engenharia | 06/2025   | Aguardando alteração  | 
    Maria Souza  | TI         | 06/2025   | Aprovado pelo sistema | 
  }
}
@endsalt
```


### Avaliação de relatorios - Validação aprovada

```kroki-plantuml
@startsalt
{+
  Relatório — João Silva | [ Voltar ]
  ==
  Aluno:           | João Silva
  Curso:           | Engenharia de Software
  Data Referência: | 06/2025
  --
  Resumo de Atividades:
  {^
    "Participei do desenvolvimento de APIs REST,    "
    "realizei reuniões de planejamento e apoiei     "
    "a equipe de QA nos testes de regressão.        "
  }
  --
  Parecer do Orientador:
  "                                        "
  "                                        "
  .
  Relatório aprovado pelo sistema
  .
  [   Confirmar Avaliação   ]
}
@endsalt
```
```kroki-plantuml
@startsalt
{+
  Relatório — João Silva | [ Voltar ]
  ==
  Aluno:           | João Silva
  Curso:           | Engenharia de Software
  Data Referência: | 06/2025
  --
  Resumo de Atividades:
  {^
    "Participei do desenvolvimento de APIs REST,    "
    "realizei reuniões de planejamento e apoiei     "
    "a equipe de QA nos testes de regressão.        "
  }
  --
  Parecer do Orientador:
  "                                        "
  "                                        "
  .
  Relatório reprovado pelo sistema - Necessita alterações
  .
  [   Confirmar Avaliação   ]
}
@endsalt
```

### Tela Inicial Administrador

```kroki-plantuml
@startsalt
{+
  Painel do Administrador | [ Sair ]
  ==
  {T
    + Menu
    ++ Gerenciar Usuários
    ++ Aprovar Vagas
    ++ Validar Relatórios
    ++ Gerar Relatórios
  }
  ==
  Gerenciar Usuários
  --
  Buscar usuário: | "                " | [ Buscar ]
  .
  {#
    Nome        | Tipo    | Status | Ações
    João Silva  | Aluno   | Ativo  | [ Editar ] | [ Remover ]
    Empresa ABC | Empresa | Ativo  | [ Editar ] | [ Remover ]
  }
}
@endsalt
```

### Tela Edição de Usuário - Administrador

```kroki-plantuml
@startsalt
{+
  Editar Usuário — João Silva | [ Voltar ]
  ==
  .
  Nome:       | "João Silva          "
  Email:      | "joao@email.com      "
  Tipo:       | ^Aluno^
  Status:     | ^Ativo^
  Matrícula:  | "2021001234          "
  Curso:      | "Engenharia de Software"
  Período:    | "5                   "
  .
  [   Salvar Alterações   ] | [ Cancelar ]
}
@endsalt
```
```kroki-plantuml
@startsalt
{+
  Editar Usuário — João Silva | [ Voltar ]
  ==
  .
  Nome:       | "João Silva          "
  Email:      | "joao@email.com      "
  Tipo:       | ^Aluno^
  Status:     | ^Ativo^
  Matrícula:  | "2021001234          "
  Curso:      | "Engenharia de Software"
  Período:    | "5                   "
  .
  [   Salvar Alterações   ] | [ Cancelar ]
}
@endsalt
```

```kroki-plantuml
@startsalt
{+
  Remover Usuário
  ==
  .
  ⚠ Tem certeza que deseja remover o usuário?
  .
  Nome:  | João Silva
  Tipo:  | Aluno
  Email: | joao@email.com
  .
  Esta ação não pode ser desfeita.
  .
  [   Confirmar Remoção   ] | [ Cancelar ]
}
@endsalt
```

### Tela Vagas - Administrador

```kroki-plantuml
@startsalt
{+
  Painel do Administrador | [ Sair ]
  ==
  Aprovar Vagas
  --
  .
  {#
    Empresa      | Vaga         | Status   | Ações
    Empresa XYZ  | Dev Frontend | Pendente | [ Aprovar ] | [ Rejeitar ]
    Empresa 123  | Designer     | Pendente | [ Aprovar ] | [ Rejeitar ]
  }
}
@endsalt
```

### Tela Relatórios - Administrador

```kroki-plantuml
@startsalt
{+
  Painel do Administrador | [ Sair ]
  ==
  Validação Final de Relatórios
  --
  .
  {#
    Aluno        | Orientador   | Parecer            | Ação
    João Silva   | Prof. Carlos | Aprovado           | [ Validar ] | [ Recusar ]
    Maria Souza  | Prof. Ana    | Solicitar Correção | [ Ver Detalhes ]
  }
}
@endsalt
```
```kroki-plantuml
@startsalt
{+
  Painel do Administrador | [ Sair ]
  ==
  Gerar Relatórios
  --
  .
  Critério: | ^Selecionar^
  Período:  | "dd/mm/aaaa" | até | "dd/mm/aaaa"
  .
  [   Emitir Relatório   ]
}
@endsalt
```


### Versão 2.0 (EM BREVE)



## Conclusão

<p align = "justify">
A partir da elaboração do protótipo foi possível ter uma noção inicial da interface do usuário, definindo fluxo, paleta de cores, botões, app bars e diversas outras funcionalidades
</p>



## Autor(es)

| Data     | Versão | Descrição                            | Autor(es)                                                                            |
| -------- | ------- | -------------------------------------- | ------------------------------------------------------------------------------------ |
| 15/04/26 | 1.0     | Criação do documento                   | Giovanna Perrone                                                 |
| 16/04/26 | 1.1     | Adicionado as imagens do protótipo     | Giovanna Perrone                                                 |                                              |

