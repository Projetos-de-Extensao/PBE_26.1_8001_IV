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

# Levantamento de Requisitos 2.0
Sistema: Sistema de Gestão de Estágios (Versão 2.0)

---

## 1. Identificação dos Stakeholders

**Alunos:** Estudantes (usuários ativos) que realizam estágio, acessam o sistema e enviam sua documentação acadêmica.

**Orientadores (Professores):** Usuários ativos responsáveis pelo suporte em caso de pendência na documentação;

**Empresas:** Entidade estritamente **passiva** no sistema. Não possuem login ou acesso; seus dados institucionais são apenas registrados para vinculação formal aos contratos e envio de notificações automáticas.

**Sistema Temporal (Cron):** Agente autônomo do servidor responsável pela execução de rotinas em segundo plano e disparo de notificações baseadas na Lei 11.788/08.

---

## 2. Requisitos Funcionais

| ID   | Descrição                                                               | Prioridade |
|------|-------------------------------------------------------------------------|------------|
| RF01 | O aluno deve poder se cadastrar no sistema                              | Alta       |
| RF02 | O aluno e o orientador devem poder realizar login                       | Alta       |
| RF03 | O sistema deve permitir o registro de dados das Empresas parceiras (Entidade Passiva) | Alta |
| RF04 | O orientador deve poder avaliar o Termo via Link seguro          | Alta       |
| RF05 | O sistema deve inspecionar automaticamente a conformidade dos contratos no momento do envio | Alta       |
| RF06 | O sistema deve emitir um consolidado diário de estágios por e-mail      | Média      |
| RF07 | O sistema deve cobrar relatórios semestrais automaticamente a cada 6 meses | Alta       |

---

## 3. Requisitos Não Funcionais

**Performance e Otimização:** O sistema deve apresentar tempo de resposta rápido. As consultas à API foram otimizadas com Eager Loading (`select_related`) para erradicar a lentidão de múltiplas consultas aninhadas (Fim do problema N+1).

**Segurança e Privacidade (LGPD):** Dados sensíveis (como CPF) operam em modo `write_only` (apenas inserção, nunca expostos em listagens de leitura). 

**Integridade Anti-Fraude:** Status de auditoria jurídica são `read_only` e tokens de validação (UUID) não são editáveis pelo usuário final, protegendo os contratos contra manipulação de pacotes HTTP.

---

## 4. Protótipo Simplificado

**Tela de Login e Cadastro:** Acesso e registro exclusivo para Alunos e Orientadores.

**Painel de Envio:** Interface onde o aluno anexa documentos e fornece dados passivos da empresa (CNPJ, Razão Social, etc).

**Caixa de Entrada (E-mail):** Interface principal onde os Orientadores recebem os Links Mágicos para aprovação rápida de contratos e os consolidados diários.