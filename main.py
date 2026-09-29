#include <iostream>
#include <string>
#include <limits>

using namespace std;

// ============================================================
// CONSTANTES DO SISTEMA
// ============================================================

const int CORRENTE = 1;
const int POUPANCA = 2;
const int SAIR = 6;


// ============================================================
// FUNÇÕES AUXILIARES
// ============================================================

void limparLinha()
{
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
}


void pausar()
{
    cout << "\nPressione ENTER para continuar...";
    cin.get();
}


// ============================================================
// CABEÇALHO
// ============================================================

void apresentarSistema()
{
    cout << "\n";
    cout << "**************************************************\n";
    cout << "*                                                *\n";
    cout << "*                BANCO INF101                    *\n";
    cout << "*       REGISTRO E GESTAO DE CONTAS              *\n";
    cout << "*                                                *\n";
    cout << "**************************************************\n";
}


// ============================================================
// MENU
// ============================================================

int selecionarOpcao()
{
    int opcao;

    cout << "\n---------------- MENU ----------------\n";
    cout << "1. Cadastrar conta\n";
    cout << "2. Consultar conta\n";
    cout << "3. Verificar saldo\n";
    cout << "4. Alterar tipo da conta\n";
    cout << "5. Ativar/Desativar conta\n";
    cout << "6. Sair\n";
    cout << "--------------------------------------\n";

    cout << "Opcao: ";
    cin >> opcao;

    if (cin.fail())
    {
        cin.clear();
        limparLinha();
        return -1;
    }

    limparLinha();

    return opcao;
}


// ============================================================
// CADASTRO
// ============================================================

void realizarCadastro(
    int &numeroConta,
    string &nomeCliente,
    string &cpf,
    int &tipoConta,
    double &saldo,
    bool &contaAtiva
)
{
    cout << "\n========== CADASTRO ==========\n";

    // Número da conta
    while (numeroConta <= 0)
    {
        cout << "Numero da conta: ";
        cin >> numeroConta;

        if (cin.fail())
        {
            cin.clear();
            limparLinha();
            numeroConta = 0;

            cout << "Valor invalido. Digite um numero inteiro.\n";
        }
        else if (numeroConta <= 0)
        {
            cout << "O numero da conta deve ser maior que zero.\n";
        }
    }

    limparLinha();

    // Nome
    while (nomeCliente.empty())
    {
        cout << "Nome do titular: ";
        getline(cin, nomeCliente);

        if (nomeCliente.empty())
        {
            cout << "O nome precisa ser informado.\n";
        }
    }

    // CPF
    while (cpf.empty())
    {
        cout << "CPF do titular: ";
        getline(cin, cpf);

        if (cpf.empty())
        {
            cout << "O CPF precisa ser informado.\n";
        }
    }

    // Tipo da conta
    tipoConta = 0;

    while (tipoConta != CORRENTE && tipoConta != POUPANCA)
    {
        cout << "\nTipo da conta:\n";
        cout << "1 - Corrente\n";
        cout << "2 - Poupanca\n";
        cout << "Escolha: ";

        cin >> tipoConta;

        if (cin.fail())
        {
            cin.clear();
            limparLinha();
            tipoConta = 0;

            cout << "Digite somente 1 ou 2.\n";
        }
        else if (tipoConta != CORRENTE && tipoConta != POUPANCA)
        {
            cout << "Opcao invalida.\n";
        }
    }

    // Saldo
    saldo = -1;

    while (saldo < 0)
    {
        cout << "Saldo inicial: R$ ";
        cin >> saldo;

        if (cin.fail())
        {
            cin.clear();
            limparLinha();
            saldo = -1;

            cout << "Digite um valor numerico valido.\n";
        }
        else if (saldo < 0)
        {
            cout << "O saldo nao pode ser negativo.\n";
        }
    }

    limparLinha();

    // Toda conta começa ativa
    contaAtiva = true;

    cout << "\n--------------------------------\n";
    cout << "Conta cadastrada com sucesso!\n";
    cout << "--------------------------------\n";
}


// ============================================================
// EXIBIÇÃO DO TIPO DA CONTA
// ============================================================

void mostrarTipo(int tipoConta)
{
    if (tipoConta == CORRENTE)
    {
        cout << "Corrente";
    }
    else if (tipoConta == POUPANCA)
    {
        cout << "Poupanca";
    }
    else
    {
        cout << "Nao informado";
    }
}


// ============================================================
// CONSULTA COMPLETA
// ============================================================

void mostrarDados(
    int numeroConta,
    const string &nomeCliente,
    const string &cpf,
    int tipoConta,
    double saldo,
    bool contaAtiva
)
{
    cout << "\n========== INFORMACOES ==========\n";

    cout << "Numero da conta : " << numeroConta << "\n";
    cout << "Titular         : " << nomeCliente << "\n";
    cout << "CPF             : " << cpf << "\n";

    cout << "Tipo da conta   : ";
    mostrarTipo(tipoConta);
    cout << "\n";

    cout << "Saldo           : R$ " << saldo << "\n";

    cout << "Situacao        : ";

    if (contaAtiva)
    {
        cout << "Ativa";
    }
    else
    {
        cout << "Inativa";
    }

    cout << "\n";
    cout << "=================================\n";
}


// ============================================================
// CONSULTA DE SALDO
// ============================================================

void consultarSaldo(int numeroConta, double saldo)
{
    cout << "\n========== SALDO ==========\n";
    cout << "Conta: " << numeroConta << "\n";
    cout << "Saldo atual: R$ " << saldo << "\n";
    cout << "===========================\n";
}


// ============================================================
// ALTERAÇÃO DO TIPO
// ============================================================

void modificarTipo(int &tipoConta)
{
    int novoTipo;

    cout << "\n====== ALTERAR TIPO ======\n";

    cout << "Tipo atual: ";
    mostrarTipo(tipoConta);
    cout << "\n";

    do
    {
        cout << "\n";
        cout << "1 - Corrente\n";
        cout << "2 - Poupanca\n";
        cout << "Novo tipo: ";

        cin >> novoTipo;

        if (cin.fail())
        {
            cin.clear();
            limparLinha();
            novoTipo = 0;

            cout << "Entrada invalida.\n";
        }
        else if (novoTipo != CORRENTE && novoTipo != POUPANCA)
        {
            cout << "Escolha 1 ou 2.\n";
        }

    } while (novoTipo != CORRENTE && novoTipo != POUPANCA);

    limparLinha();

    tipoConta = novoTipo;

    cout << "\nTipo da conta atualizado.\n";
}


// ============================================================
// ALTERAÇÃO DO STATUS
// ============================================================

void modificarStatus(bool &contaAtiva)
{
    contaAtiva = !contaAtiva;

    cout << "\nA conta foi ";

    if (contaAtiva)
    {
        cout << "ATIVADA";
    }
    else
    {
        cout << "DESATIVADA";
    }

    cout << ".\n";
}


// ============================================================
// PROGRAMA PRINCIPAL
// ============================================================

int main()
{
    // --------------------------------------------------------
    // Dados da conta
    // --------------------------------------------------------

    int numeroConta = 0;
    string nomeCliente = "";
    string cpf = "";
    int tipoConta = 0;
    double saldo = 0.0;
    bool contaAtiva = false;

    bool encerrado = false;

    apresentarSistema();

    // --------------------------------------------------------
    // Loop principal
    // --------------------------------------------------------

    while (!encerrado)
    {
        int opcao = selecionarOpcao();

        cout << "\n";

        switch (opcao)
        {
            // ------------------------------------------------
            // CADASTRAR
            // ------------------------------------------------

            case 1:

                if (numeroConta != 0)
                {
                    cout << "Ja existe uma conta cadastrada.\n";
                    cout << "O sistema trabalha com uma conta nesta etapa.\n";
                }
                else
                {
                    realizarCadastro(
                        numeroConta,
                        nomeCliente,
                        cpf,
                        tipoConta,
                        saldo,
                        contaAtiva
                    );
                }

                break;


            // ------------------------------------------------
            // CONSULTAR
            // ------------------------------------------------

            case 2:

                if (numeroConta == 0)
                {
                    cout << "Nenhuma conta foi cadastrada.\n";
                }
                else
                {
                    mostrarDados(
                        numeroConta,
                        nomeCliente,
                        cpf,
                        tipoConta,
                        saldo,
                        contaAtiva
                    );
                }

                break;


            // ------------------------------------------------
            // SALDO
            // ------------------------------------------------

            case 3:

                if (numeroConta == 0)
                {
                    cout << "Nenhuma conta foi cadastrada.\n";
                }
                else
                {
                    consultarSaldo(numeroConta, saldo);
                }

                break;


            // ------------------------------------------------
            // ALTERAR TIPO
            // ------------------------------------------------

            case 4:

                if (numeroConta == 0)
                {
                    cout << "Cadastre uma conta antes de alterar o tipo.\n";
                }
                else
                {
                    modificarTipo(tipoConta);
                }

                break;


            // ------------------------------------------------
            // ATIVAR / DESATIVAR
            // ------------------------------------------------

            case 5:

                if (numeroConta == 0)
                {
                    cout << "Cadastre uma conta antes de alterar o status.\n";
                }
                else
                {
                    modificarStatus(contaAtiva);
                }

                break;


            // ------------------------------------------------
            // SAIR
            // ------------------------------------------------

            case SAIR:

                cout << "Sistema encerrado.\n";
                cout << "Obrigado por utilizar o Banco INF101!\n";

                encerrado = true;

                break;


            // ------------------------------------------------
            // OPÇÃO INVÁLIDA
            // ------------------------------------------------

            case -1:

                cout << "Digite uma opcao numerica de 1 a 6.\n";

                break;


            default:

                cout << "Opcao inexistente.\n";
                cout << "Escolha uma opcao entre 1 e 6.\n";

                break;
        }
    }

    return 0;
}
