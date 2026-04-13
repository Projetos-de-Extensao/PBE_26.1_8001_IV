Levantamento de Requisitos
Sistema: Sistema de Gestão de Estágios

---

## 1. Identificação dos Stakeholders

**Alunos:** Pessoas que buscam oportunidades de estágio e desejam se candidatar às vagas disponíveis.

**Empresas:** Estabelecimentos que oferecem vagas de estágio e avaliam candidatos.

**Administrador:** Responsável por gerenciar o sistema, usuários e validar vagas cadastradas.

---

## 2. Requisitos Funcionais

| ID   | Descrição                                                                 | Prioridade |
|------|-------------------------------------------------------------------------|------------|
| RF01 | O aluno deve poder se cadastrar no sistema                              | Alta       |
| RF02 | O aluno deve poder realizar login                                       | Alta       |
| RF03 | O aluno deve visualizar vagas de estágio disponíveis                    | Alta       |
| RF04 | O aluno deve se candidatar a vagas                                      | Alta       |
| RF05 | O aluno deve acompanhar o status da candidatura                         | Média      |
| RF06 | A empresa deve poder se cadastrar no sistema                            | Alta       |
| RF07 | A empresa deve cadastrar vagas de estágio                               | Alta       |
| RF08 | A empresa deve visualizar candidatos                                    | Alta       |
| RF09 | A empresa deve aprovar ou rejeitar candidatos                           | Alta       |
| RF10 | O administrador deve gerenciar usuários                                 | Média      |
| RF11 | O administrador deve aprovar vagas antes da publicação                  | Alta       |
| RF12 | O sistema deve gerar relatórios                                         | Baixa      |

---

## 3. Requisitos Não Funcionais

**Performance:** O sistema deve apresentar tempo de resposta rápido mesmo com múltiplos usuários.

**Segurança:** Os dados dos usuários devem ser protegidos, com autenticação segura.

**Usabilidade:** A interface deve ser simples, intuitiva e de fácil navegação.

---

## 4. Exemplo de Caso de Uso

### UC01 - Candidatar-se a Vaga

**Atores:** Aluno, Sistema.

**Pré-condição:** O aluno deve estar cadastrado e logado no sistema.

**Fluxo Principal:**
1. O aluno acessa a lista de vagas disponíveis.
2. O aluno seleciona uma vaga de interesse.
3. O aluno visualiza os detalhes da vaga.
4. O aluno clica em "Candidatar-se".
5. O sistema registra a candidatura e confirma a ação.

**Fluxos Alternativos:**
- FA1: Aluno não está logado → Sistema solicita login.
- FA2: Vaga indisponível → Sistema informa que a vaga foi encerrada.

**Pós-condição:** A candidatura é registrada no sistema e fica disponível para análise da empresa.

---

## 5. Protótipo (Exemplo Simplificado)

**Tela de Vagas:** Lista de vagas com filtros (área, localização, empresa).

**Tela de Detalhes:** Informações da vaga + botão "Candidatar-se".

**Tela de Perfil:** Dados do aluno + histórico de candidaturas.

---

## 6. Validação

**Validação com Usuários:** Confirmar se o processo de candidatura é simples e intuitivo.

**Teste com Empresas:** Verificar se o fluxo de aprovação de candidatos atende às necessidades.