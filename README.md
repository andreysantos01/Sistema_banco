Sistema Bancário


* **Depósito (1):** Permite depositar um valor em uma conta existente.
    
    * O sistema solicitará o CPF do cliente e o valor do depósito.
* **Saque (2):** Permite sacar um valor de uma conta corrente existente.
    
    * O sistema solicitará o CPF do cliente e o valor do saque.
    * Conta corrente com limite de saque de R$ 500,00 e limite de 3 saques por dia.
* **Extrato (3):** Exibe o extrato de uma conta corrente existente.
    
    * O sistema solicitará o CPF do cliente e exibirá o histórico de transações e o saldo atual.
* **Novo usuário (4):** Permite criar um novo cliente.
    
    * O sistema solicitará o CPF, nome completo, data de nascimento e endereço do cliente.
* **Nova conta (5):** Permite criar uma nova conta corrente para um cliente existente.
    
    * O sistema solicitará o CPF do cliente e criará uma nova conta corrente com agência "0001".
* **Listar contas (6):** Lista todas as contas correntes existentes.
    
    * Exibe o número da agência, número da conta e nome do titular de cada conta.
* **Sair (7):** Encerra o programa.

## Estrutura do código

O código é organizado em classes que representam as entidades do sistema bancário:

* **Cliente:** Classe base para clientes, com atributos como endereço e uma lista de contas.
* **PessoaFisica:** Subclasse de Cliente, representando clientes pessoa física, com atributos adicionais como nome, data de nascimento e CPF.
* **Conta:** Classe base para contas, com atributos como saldo, número, agência, cliente e histórico de transações.
* **ContaCorrente:** Subclasse de Conta, representando contas correntes, com atributos adicionais como limite de saque e limite de saques diários.
* **Historico:** Classe que armazena o histórico de transações de uma conta.
* **Transacao:** Classe abstrata para transações, com atributos como valor e métodos abstratos para registrar a transação.
* **Saque:** Subclasse de Transacao, representando saques.
* **Deposito:** Subclasse de Transacao, representando depósitos.

O código também inclui funções para:

* Exibir o menu principal.
* Filtrar clientes por CPF.
* Recuperar a conta de um cliente.
* Realizar depósitos, saques e exibir extratos.
* Criar clientes e contas.
* Listar contas.

## Observações

* O sistema não possui persistência de dados, ou seja, os dados são perdidos ao encerrar o programa.
* O sistema não possui tratamento de erros robusto, como validação de entradas e tratamento de exceções.

## Melhorias futuras

* Implementar persistência de dados usando um banco de dados ou arquivos.
* Adicionar mais tipos de contas, como conta poupança.
* Implementar mais tipos de transações, como transferências e pagamentos.
* Adicionar autenticação de usuários.
* Melhorar a interface do usuário.
* Adicionar testes unitários.
* Melhorar o tratamento de erros.
* Permitir que o cliente escolha a conta ao realizar transações.
* Adicionar limite de valor para depósito.
* Adicionar taxas para transações.
* Implementar uma interface gráfica.
