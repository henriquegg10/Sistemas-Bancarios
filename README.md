# BANCO INF101

### Sistema de Registro e Gestão de Contas Bancárias

Projeto desenvolvido para a disciplina INF101, correspondente à **Etapa 1**
do trabalho de desenvolvimento de um sistema bancário em C++.

---

## Sumário

- [Descrição](#descrição)
- [Objetivo](#objetivo)
- [Dados da conta](#dados-da-conta)
- [Operações disponíveis](#operações-disponíveis)
- [Regras do sistema](#regras-do-sistema)
- [Validações](#validações)
- [Estrutura do programa](#estrutura-do-programa)
- [Conceitos utilizados](#conceitos-utilizados)
- [Compilação](#compilação)
- [Execução](#execução)
- [Exemplo](#exemplo)
- [Limitações](#limitações)

---

## Descrição

O Banco INF101 é um programa desenvolvido em C++ para realizar o cadastro
e o gerenciamento básico de uma conta bancária.

A primeira etapa do projeto tem como objetivo trabalhar os fundamentos da
linguagem C++, utilizando variáveis individuais e um menu de operações.

O sistema permite cadastrar uma conta, consultar seus dados, verificar o
saldo, alterar o tipo da conta e modificar sua situação.

---

## Objetivo

O objetivo desta etapa é consolidar conceitos básicos de programação.

Entre os principais pontos trabalhados estão:

- Declaração de variáveis;
- Entrada e saída de informações;
- Condições;
- Repetições;
- Menu com `switch`;
- Funções;
- Validação de dados;
- Utilização de diferentes tipos de variáveis.

---

## Dados da conta

A conta possui os seguintes dados:

| Informação | Tipo | Descrição |
|---|---|---|
| Número da conta | `int` | Identificação da conta |
| Nome do cliente | `string` | Nome do titular |
| CPF | `string` | CPF do titular |
| Tipo da conta | `int` | Corrente ou poupança |
| Saldo | `double` | Valor disponível |
| Conta ativa | `bool` | Indica a situação da conta |

### Tipos de conta

O sistema utiliza dois tipos:

```text
1 - Corrente
2 - Poupanca
