# Documento de Levantamento de Requisitos
## Sistema de Gestão de Estágios

---

## Objetivo do Sistema
O sistema tem como objetivo facilitar o gerenciamento de estágios, permitindo que alunos, empresas e administradores interajam no processo de divulgação de vagas, candidatura e acompanhamento.

---

## Requisitos Funcionais (RF)

### Aluno
- RF01: O sistema deve permitir o cadastro de alunos  
- RF02: O sistema deve permitir autenticação (login)  
- RF03: O sistema deve permitir visualizar vagas de estágio disponíveis  
- RF04: O sistema deve permitir candidatura em vagas  
- RF05: O sistema deve permitir acompanhar o status da candidatura  
- RF06: O sistema deve permitir editar informações do perfil  

### Empresa
- RF07: O sistema deve permitir cadastro de empresas  
- RF08: O sistema deve permitir autenticação de empresas  
- RF09: O sistema deve permitir cadastrar vagas de estágio  
- RF10: O sistema deve permitir visualizar candidatos  
- RF11: O sistema deve permitir aprovar ou rejeitar candidatos  

### Administrador
- RF12: O sistema deve permitir gerenciar usuários  
- RF13: O sistema deve permitir aprovar vagas antes da publicação  
- RF14: O sistema deve permitir monitorar candidaturas  
- RF15: O sistema deve permitir gerar relatórios do sistema  

---

## Requisitos Não Funcionais (RNF)

- RNF01: O sistema deve ser acessível via navegador web  
- RNF02: O sistema deve possuir interface amigável e intuitiva  
- RNF03: O sistema deve garantir a segurança dos dados dos usuários  
- RNF04: O sistema deve apresentar bom desempenho (resposta rápida)  
- RNF05: O sistema deve estar disponível continuamente  
- RNF06: O sistema deve suportar múltiplos acessos simultâneos  

---

## Regras de Negócio (RN)

- RN01: O aluno deve estar cadastrado para se candidatar a uma vaga  
- RN02: A empresa só pode visualizar candidatos de suas vagas  
- RN03: As vagas devem ser aprovadas pelo administrador antes de serem publicadas  
- RN04: O aluno só pode acompanhar suas próprias candidaturas  
- RN05: Cada candidatura deve possuir um status (pendente, aprovado ou rejeitado)