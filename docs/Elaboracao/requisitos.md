Levantamento de Requisitos
Sistema: Sistema de Gestão de Estágios

---

## 1. Identificação dos Stakeholders

**Alunos:** Estudantes que realizam estágio e acompanham sua documentação acadêmica.

**Empresas:** Organizações que recebem estagiários e participam do processo de acompanhamento do estágio.

**Orientadores:** Responsáveis pelo acompanhamento e validação das atividades de estágio dos alunos.

**Administrador:** Responsável pela manutenção e gerenciamento do sistema.

---

## 2. Requisitos Funcionais

| ID   | Descrição                                                                 | Prioridade |
|------|-------------------------------------------------------------------------|------------|
| RF01 | O aluno deve poder se cadastrar no sistema                              | Alta       |
| RF02 | O aluno deve poder realizar login                                       | Alta       |
| RF06 | A empresa deve poder se cadastrar no sistema                            | Alta       |
| RF10 | O administrador deve gerenciar usuários                                 | Média      |
| RF12 | O sistema deve gerar relatórios                                         | Baixa      |

---

## 3. Requisitos Não Funcionais

**Performance:** O sistema deve apresentar tempo de resposta rápido mesmo com múltiplos usuários.

**Segurança:** Os dados dos usuários devem ser protegidos, com autenticação segura. 

**Usabilidade:** A interface deve ser simples, intuitiva e de fácil navegação.

---

## 4. Casos de Uso

### UC01 - Login de Orientador

**Atores:** Orientador, Sistema.
**Pré-condição:** Orientador cadastrado no sistema.

**Fluxo Principal:**
1. O orientador acessa a tela de login.
2. O orientador informa e-mail e senha.
3. O sistema valida as credenciais.
4. O sistema concede acesso às funcionalidades disponíveis.

**Fluxos Alternativos:**
- FA1: Credenciais inválidas → Sistema exibe mensagem de erro.

**Pós-condição:** Orientador autenticado no sistema.

---

### UC02 - Login
**Atores:** Aluno/Empresa/Orientador/Administrador, Sistema.  
**Pré-condição:** Usuário cadastrado.  
**Fluxo Principal:**
1. O usuário acessa a tela de login.
2. O usuário insere e-mail e senha.
3. O sistema valida as credenciais.
4. O sistema permite acesso.
**Fluxos Alternativos:**
- FA1: Credenciais inválidas → Sistema exibe erro.
**Pós-condição:** Usuário autenticado no sistema.

---

### UC06 - Cadastro de Empresa
**Atores:** Empresa, Sistema.  
**Pré-condição:** Empresa não cadastrada.  
**Fluxo Principal:**
1. A empresa acessa a tela de cadastro.
2. Preenche os dados institucionais.
3. Envia o formulário.
4. O sistema valida e cria a conta.
**Fluxos Alternativos:**
- FA1: Dados inválidos → Sistema solicita correção.
**Pós-condição:** Conta de empresa criada.

---

### UC10 - Gerenciar Usuários
**Atores:** Administrador, Sistema.  
**Pré-condição:** Administrador logado.  
**Fluxo Principal:**
1. O administrador acessa o painel.
2. Visualiza os usuários cadastrados.
3. Edita ou remove usuários.
**Fluxos Alternativos:**
- FA1: Usuário não encontrado → Sistema informa.
**Pós-condição:** Usuários atualizados.

---

### UC12 - Gerar Relatórios
**Atores:** Administrador, Sistema.  
**Pré-condição:** Sistema com dados cadastrados.  
**Fluxo Principal:**
1. O administrador acessa a área de relatórios.
2. Seleciona os critérios.
3. O sistema gera o relatório.
**Fluxos Alternativos:**
- FA1: Sem dados suficientes → Sistema informa.
**Pós-condição:** Relatório gerado com sucesso.

---

## 5. Protótipo (Exemplo Simplificado)

**Tela de Login:** Acesso ao sistema por alunos, empresas, orientadores e administradores.

**Tela de Cadastro:** Cadastro de alunos e empresas.

**Tela de Documentos:** Envio e gerenciamento de documentos relacionados ao estágio.

**Tela de Termo de Compromisso:** Cadastro e acompanhamento dos termos de compromisso.

**Tela de Relatórios:** Consulta e geração de relatórios acadêmicos e administrativos.

---

## 6. Validação

**Validação com Usuários:** Confirmar se o cadastro e acompanhamento dos estágios são simples e intuitivos.

**Teste com Empresas e Orientadores:** Verificar se o gerenciamento de documentos, termos de compromisso e relatórios atende às necessidades do processo de estágio.