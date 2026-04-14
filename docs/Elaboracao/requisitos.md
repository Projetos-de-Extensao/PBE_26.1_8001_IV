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

## 4. Casos de Uso

### UC01 - Cadastro de Aluno
Atores: Aluno, Sistema.  
Pré-condição: Usuário não possui cadastro.  
Fluxo Principal:
1. O aluno acessa a tela de cadastro.
2. O aluno preenche seus dados pessoais.
3. O aluno envia o formulário.
4. O sistema valida os dados e cria a conta.
Fluxos Alternativos:
- FA1: Dados inválidos → Sistema solicita correção.
Pós-condição: Conta de aluno criada com sucesso.

---

### UC02 - Login
Atores: Aluno/Empresa/Administrador, Sistema.  
Pré-condição: Usuário cadastrado.  
Fluxo Principal:
1. O usuário acessa a tela de login.
2. O usuário insere e-mail e senha.
3. O sistema valida as credenciais.
4. O sistema permite acesso.
Fluxos Alternativos:
- FA1: Credenciais inválidas → Sistema exibe erro.
Pós-condição: Usuário autenticado no sistema.

---

### UC03 - Visualizar Vagas
Atores: Aluno, Sistema.  
Pré-condição: Usuário logado.  
Fluxo Principal:
1. O aluno acessa a lista de vagas.
2. O sistema exibe vagas disponíveis.
3. O aluno pode aplicar filtros.
Fluxos Alternativos:
- FA1: Nenhuma vaga disponível → Sistema informa.
Pós-condição: Lista de vagas exibida.

---

### UC04 - Candidatar-se a Vaga
Atores: Aluno, Sistema.  
Pré-condição: Aluno logado.  
Fluxo Principal:
1. O aluno seleciona uma vaga.
2. O aluno clica em "Candidatar-se".
3. O sistema registra a candidatura.
Fluxos Alternativos:
- FA1: Vaga encerrada → Sistema informa indisponibilidade.
Pós-condição: Candidatura registrada.

---

### UC05 - Acompanhar Candidatura
Atores: Aluno, Sistema.  
Pré-condição: Candidatura realizada.  
Fluxo Principal:
1. O aluno acessa suas candidaturas.
2. O sistema exibe o status.
Fluxos Alternativos:
- FA1: Nenhuma candidatura → Sistema informa.
Pós-condição: Status visualizado.

---

### UC06 - Cadastro de Empresa
Atores: Empresa, Sistema.  
Pré-condição: Empresa não cadastrada.  
Fluxo Principal:
1. A empresa acessa cadastro.
2. Preenche dados institucionais.
3. Envia formulário.
4. Sistema valida e cria conta.
Fluxos Alternativos:
- FA1: Dados inválidos → Sistema solicita correção.
Pós-condição: Conta de empresa criada.

---

### UC07 - Cadastro de Vaga
Atores: Empresa, Sistema.  
Pré-condição: Empresa logada.  
Fluxo Principal:
1. Empresa acessa área de vagas.
2. Preenche informações da vaga.
3. Envia cadastro.
4. Sistema registra vaga.
Fluxos Alternativos:
- FA1: Dados incompletos → Sistema solicita correção.
Pós-condição: Vaga cadastrada.

---

### UC08 - Visualizar Candidatos
Atores: Empresa, Sistema.  
Pré-condição: Vaga cadastrada.  
Fluxo Principal:
1. Empresa acessa candidatos da vaga.
2. Sistema lista candidatos.
Fluxos Alternativos:
- FA1: Nenhum candidato → Sistema informa.
Pós-condição: Lista de candidatos exibida.

---

### UC09 - Aprovar/Rejeitar Candidato
Atores: Empresa, Sistema.  
Pré-condição: Existem candidatos.  
Fluxo Principal:
1. Empresa seleciona candidato.
2. Escolhe aprovar ou rejeitar.
3. Sistema atualiza status.
Fluxos Alternativos:
- FA1: Erro no sistema → Operação cancelada.
Pós-condição: Status atualizado.

---

### UC10 - Gerenciar Usuários
Atores: Administrador, Sistema.  
Pré-condição: Admin logado.  
Fluxo Principal:
1. Administrador acessa painel.
2. Visualiza usuários.
3. Edita ou remove usuários.
Fluxos Alternativos:
- FA1: Usuário não encontrado → Sistema informa.
Pós-condição: Usuários atualizados.

---

## 5. Protótipo (Exemplo Simplificado)

**Tela de Vagas:** Lista de vagas com filtros (área, localização, empresa).

**Tela de Detalhes:** Informações da vaga + botão "Candidatar-se".

**Tela de Perfil:** Dados do aluno + histórico de candidaturas.

---

## 6. Validação

**Validação com Usuários:** Confirmar se o processo de candidatura é simples e intuitivo.

**Teste com Empresas:** Verificar se o fluxo de aprovação de candidatos atende às necessidades.