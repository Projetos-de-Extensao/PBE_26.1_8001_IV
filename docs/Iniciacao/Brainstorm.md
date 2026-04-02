---
id: brainstorm
title: Brainstorm
---
 
## Introdução
<p align = "justify">
O brainstorm é uma técnica de elicitação de requisitos que consiste em reunir a equipe e discutir sobre diversos tópicos gerais do projeto apresentados no documento problema de negócio. No brainstorm o diálogo é incentivado e críticas são evitadas para permitir que todos colaborem com suas próprias ideias.
</p>
 
## Metodologia
<p align = "justify">
A equipe se reuniu para debater ideias gerais sobre o projeto no dia 02/04/2026, por meio de reunião online. A atividade teve início durante o período de aula e foi conduzida até a consolidação das ideias principais. Julia Valente D'Alessandro atuou como moderadora, direcionando a equipe com questões pré-elaboradas e registrando as respostas no documento.
</p>
 
## Brainstorm
 
## Versão 1.0
 
## Perguntas
 
### 1. Qual o objetivo principal da aplicação?
 
<p align = "justify">
<b>1</b> - Desenvolver uma API capaz de validar automaticamente propostas de estágio.
</p>
 
<b>2</b> - Fornecer validação em tempo real com base na Lei 11.788/08 e nas diretrizes institucionais.
 
<b>3</b> - Automatizar o processo de análise de conformidade dos contratos de estágio.
 
<b>4</b> - Reduzir o trabalho manual dos coordenadores acadêmicos.
 
<b>5</b> - Gerenciar regras acadêmicas e legais de forma centralizada e configurável.
</p>
 
---
 
### 2. Como será o processo para cadastrar um novo cliente?
 
<p align = "justify">
<b>1</b> - O administrador deverá realizar login no sistema para cadastrar novos clientes.
 
<b>2</b> - O cliente será registrado com credenciais de autenticação para acesso à API.
 
<b>3</b> - Com o usuário administrador logado, será possível associar o cliente aos cursos disponíveis.

<b>4</b> - O cliente utilizará um token para autenticação nas requisições.
 
<b>5</b> - O sistema validará as credenciais antes de permitir o envio de dados.
 
---
 
### 3. Como será a forma de adicionar produtos?
 
<p align = "justify">
<b>1</b> - O cliente enviará os dados da proposta de estágio via requisição HTTP.
</p>
 
<p align = "justify">
<b>2</b> - A proposta conterá informações como carga horária, empresa, duração e supervisor.
</p>
 
<b>3</b> - O sistema validará automaticamente os dados com base nas regras cadastradas.
 
<b>4</b> - As propostas serão armazenadas para controle e auditoria.

 
---
 
### 4. Outras perguntas pertinentes ao contexto

<p align = "justify">
<b>1</b> - Como garantir que todos os dados obrigatórios foram preenchidos corretamente?
 
<b>2</b> - Como tratar propostas que não atendem completamente aos requisitos?
 
<b>3</b> - Como permitir a correção e reenvio de propostas reprovadas?
 
<b>4</b> - Como manter as regras atualizadas conforme mudanças na legislação?

---
 
### 5. "Outras perguntas pertinentes ao contexto", Como seria a forma de adicionar do cliente adicionar os produtos ?
<p align = "justify">
<b>1</b> - O cliente deverá enviar requisições do tipo POST para a API em formato JSON estruturado.
</p>
 
### 6. Quais informações seriam interessante para o cliente?
<p align = "justify">
   <b>1</b> - Informações sobre o status da validação (aprovado ou reprovado).
   
   <b>2</b> - O cliente usuário poderá acessar informações detalhadas sobre pendências e inconsistências.

   <b>3</b> - O usuário poderá visualizar histórico de validações, regras aplicadas e justificativas do resultado.
   
</p>
 
### Requisitos elicitados
 
|ID|Descrição|
|----|-------------|
|BS01| O sistema deve permitir o cadastro de clientes consumidores da API.|
|BS02| O sistema deve autenticar clientes por meio de tokens seguros.|
|BS03| O sistema deve receber dados de propostas de estágio em formato JSON.|
|BS04| O sistema deve validar automaticamente os dados com base nas regras definidas.|
|BS05| O sistema deve retornar o status da validação (aprovado ou reprovado).|
|BS06| O sistema deve fornecer justificativas detalhadas em caso de reprovação.|
|BS07| O sistema deve armazenar o histórico de validações realizadas.|
|BS08| O sistema deve permitir a configuração de regras específicas por curso.|
|BS09| O sistema deve garantir conformidade com a Lei 11.788/08.|
|BS10| O sistema deve registrar todas as informações das propostas submetidas.|
|BS11| O sistema deve permitir o reenvio de propostas corrigidas.|
|BS12| O sistema deve manter logs para auditoria das validações.|
|BS13| O sistema deve garantir segurança e controle de acesso aos dados.|
|BS14| O sistema deve suportar múltiplas requisições simultâneas.|
|BS15| O sistema deve fornecer documentação para integração com clientes.|
 
## Conclusão
<p align = "justify">
Através da aplicação da técnica, foi possível elicitar alguns dos primeiros requisitos do projeto, permitindo uma melhor compreensão do problema e das funcionalidades esperadas para o sistema.
</p>

## Referências Bibliográficas
 
	⁠BARBOSA, S. D. J; DA SILVA, B. S. Interação humano-computador. Elsevier, 2010.
 
 
## Autor(es)
| Data | Versão | Descrição | Autor(es) |
| -- | -- | -- | -- |
| 02/04/2026 | 1.0 | Criação do documento | Julia Valente D'Alessandro, Luana Salles Sousa Miranda |