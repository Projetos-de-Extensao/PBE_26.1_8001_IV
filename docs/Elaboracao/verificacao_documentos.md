# 📄 Verificação de Documentos

## • Objetivo
O módulo de verificação de documentos tem como finalidade garantir que todos os documentos exigidos para o estágio sejam enviados, armazenados e validados de forma segura, íntegra e auditável, assegurando conformidade com as diretrizes acadêmicas.

---

## • Envio de Documentos
O sistema deve permitir que o aluno realize o upload dos documentos obrigatórios em formato digital (preferencialmente PDF), vinculando-os ao seu cadastro.

- O envio deve ser autenticado (usuário logado)
- Cada documento deve possuir identificação de tipo
- O sistema deve registrar data e hora do envio

---

## • Classificação de Documentos
Os documentos devem ser categorizados conforme sua finalidade, incluindo, mas não se limitando a:

- Termo de Compromisso de Estágio
- Relatórios de Atividades
- Declarações da Empresa
- Comprovantes Acadêmicos

Cada categoria deve possuir regras específicas de validação.

---

## • Integridade dos Dados
No momento do upload, o sistema deve gerar um **hash criptográfico (ex: SHA-256)** do arquivo, com o objetivo de garantir sua integridade.

- O hash deve ser armazenado no banco de dados
- Deve ser possível recalcular o hash para verificação futura
- Alterações no arquivo devem ser detectáveis por divergência de hash

---

## • Armazenamento
Os documentos devem ser armazenados de forma estruturada e segura, contendo os seguintes metadados:

- Nome do arquivo
- Tipo de documento
- Identificador do usuário
- Data de envio
- Hash criptográfico
- Status de validação

---

## • Validação de Documentos

A validação deve ocorrer em duas etapas complementares:

### Validação Automática
Realizada pelo sistema no momento do envio:

- Verificação do formato do arquivo (PDF válido)
- Validação de tamanho máximo permitido
- Verificação de integridade básica do arquivo

### Validação Manual
Realizada por um responsável institucional (orientador ou coordenador):

- Análise do conteúdo do documento
- Verificação de assinaturas e autenticidade
- Conferência de dados obrigatórios

---

## • Controle de Status
Cada documento deve possuir um status associado ao seu ciclo de vida:

- **Pendente**: aguardando validação
- **Aprovado**: validado com sucesso
- **Rejeitado**: não atende aos critérios

O sistema deve registrar:

- Responsável pela validação
- Data da validação
- Justificativa em caso de rejeição

---

## • Auditoria e Rastreamento
O sistema deve manter um histórico completo das ações realizadas:

- Upload de documentos
- Atualizações
- Aprovações e rejeições

Essas informações devem garantir rastreabilidade e transparência no processo.

---

## • Segurança
O sistema deve implementar mecanismos de segurança para proteção dos dados:

- Controle de acesso baseado em perfil de usuário
- Proteção contra alteração indevida de arquivos
- Garantia de integridade dos documentos via hash
- Armazenamento seguro dos documentos

---

## • Versionamento de Documentos
Em caso de rejeição, o sistema deve permitir o reenvio do documento:

- Versões anteriores devem ser mantidas
- Histórico de alterações deve ser preservado
- Cada versão deve possuir seu próprio hash

---

## • Conformidade Acadêmica
O sistema deve assegurar que:

- Apenas documentos obrigatórios sejam exigidos
- Os critérios de validação estejam alinhados com a instituição
- O fluxo siga as diretrizes do regulamento de estágio

---

## • Considerações Técnicas
O uso de hash criptográfico tem como objetivo garantir a integridade dos documentos armazenados, não sendo suficiente, isoladamente, para validar a autenticidade do conteúdo.

A validação final depende de análise humana e critérios institucionais definidos.