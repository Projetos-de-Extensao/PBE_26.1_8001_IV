---
id: documento_de_arquitetura
title: Documento de Arquitetura
---
# Documento de Arquitetura de Software (DAS)

# Sistema de Gestão de Estágios

# Introdução

## Proposta

<p align = "justify">
Este documento apresenta uma visão geral da arquitetura do sistema, utilizando diferentes visões arquiteturais para destacar diferentes aspectos do sistema. É utilizado para capturar as decisões arquiteturais significativas que fizeram parte do sistema.
</p>

## Escopo

<p align = "justify">
A aplicação "Sistema de Gestão de Estágios" tem o objetivo de gerenciar alunos, empresas, orientadores, documentos, termos de compromisso e relatórios relacionados ao acompanhamento de estágios.
</p>

## Definições, Acrônimos e Abreviações

- MVC - Model View Controller.
- MVT - Model View Template.
- SGE - Sistema de Gestão de Estágios.

## Visão Geral

<p align = "justify">
O Documento de Arquitetura de Software (DAS) trata-se de uma visão geral de toda a arquitetura do sistema, observando diferentes aspectos do mesmo. Neste documento serão abordadas as seguintes visões da aplicação SGE:
</p>

- Caso de Uso;
- Lógica;
- Implantação;
- Implementação;
- Dados;

# Representação Arquitetural

## Cliente-Servidor

<p align = "justify">
Cliente-Servidor é um modelo de arquitetura...
</p>

Cliente (Frontend):

- View: Consiste.....

Servidor (Backend):

- Controller: faz a conexão entre as camadas...
- Service: Responsável pela lógica...
- Model: Responsável pela persistência...

# Objetivos de Arquitetura e Restrições

## Objetivos

<p align = "justify">
Segurança:
   -
Persistência:
   - 
Privacidade:
   - Middlewares: Foi usado middlewares...
Desempenho:
   Requisições...
Reusabilidade:
   Componentes no Frontend...
</p>

## Restrições

<p align = "justify">
Tamanho da tela:...

Portabilidade:...

| IE | Edge  | Firefox | Chrome | Safari | Googlebot |
| -- | ----- | ------- | ------ | ------ | --------- |
| 11 | >= 14 | >= 52   | >= 49  | >= 10  | Sim       |

Serviços: Os serviços oferecidos....

Acesso a internet: A aplicação está limitada apenas a conexão com internet

</p>

## Ferramentas Utilizadas

- Python: Linguagem de programação utilizada no backend.
- Django: Framework principal da aplicação.
- Django REST Framework: Desenvolvimento da API REST.
- SQLite: Banco de dados utilizado no projeto.
- Git: Controle de versão.
- GitHub: Hospedagem do código-fonte.
- MkDocs: Geração da documentação.
- VS Code: Ambiente de desenvolvimento.

# Visão de Caso de Uso

<p align = "justify">
Os casos de uso representam as principais funcionalidades do sistema relacionadas ao gerenciamento de estágios, usuários, documentos e relatórios.
</p>

![Caso de uso 1](../assets/Casos_de_Uso/Exemplocaso_de_uso_1.png)

![Caso de uso 2](../assets/Casos_de_Uso/Exemplocaso_de_uso_1.png)

# Visão Lógica

# Visão de Implantação

# Visão de Implementação

## Visão Geral

![Diagrama de Componentes](../assets/Casos_de_Uso/Exemplocaso_de_uso_1.png)

# Visão de Dados

## Modelo Entidade Relacionamento (MER)

#### Entidades e Relacionamentos:

## Diagrama Entidade Relacionamento (DER)

# Tamanho e Desempenho

# Qualidade

</p>

# Referências Bibliográficas

# Histórico de Versão

| Data       | Versão | Descrição                                                            | Autor(es)                                   |
| ---------- | ------- | ---------------------------------------------------------------------- | ------------------------------------------- |
| 08/11/2020 | 1.0 | Criada estrutura básica do documento | Equipe do Projeto |
| 15/11/2020 | 1.1     | Representação arquitetural e objetivos e restrições arquiteturais. | Autores                                     |
| 19/11/2020 | 1.2     | Adição dos diagramas, visões, tamanho e desempenho e qualidade      | Autores                                     |
| 20/11/2020 | 1.3     | Adição da descrição de MER e DER                                   | Autores                                     |
| 20/11/2020 | 1.4     | Adição do tópico de qualidade                                       | Autores                                     |
| 20/11/2020 | 1.5     | Revisão                                                               | Autores                                     |