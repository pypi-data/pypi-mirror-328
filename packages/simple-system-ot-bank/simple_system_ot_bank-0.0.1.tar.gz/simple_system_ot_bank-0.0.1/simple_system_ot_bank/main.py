import textwrap
from tzlocal import get_localzone
from datetime import datetime

# <--- VALIDAÇÕES & EXCEÇÕES ---> #
def name_validade():
    nome = input("Informe o nome completo: ")
    if not all(c.isalpha() or c.isspace() for c in nome):
        print("\n@@@ Nome Inválido, Utilize apenas Letras e Espaços em Brancos! @@@")
        return
    return nome

def date_validade():
    try:
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        data_convertida = datetime.strptime(data_nascimento, "%d-%m-%Y")
        ano = data_convertida.year
        if ano < 1900 or ano > 2025:
            print("\n@@@ Ano fora do intervalo permitido. O ano deve estar entre 1900 e 2007. @@@")
            return
        return data_convertida
    except ValueError:
        print("\n@@@ Data inválida, Utilize o Formato Correto: (dd-mm-aaaa) @@@")

def postal_validade():
    endereco_input = input("Informe o endereço (logradouro-numero-bairro-cidade-estado): ")
    split = endereco_input.split("-") 
    chaves = ["logradouro", "nro", "bairro", "cidade", "estado"]
    endereco = {chaves[i]: split[i] for i in range(len(split))}
    return endereco

def filter_users(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def exceptions(valor, saldo, limite, numero_saques, LIMITE_SAQUES):
    
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
        
    if excedeu_saldo:
        print(f"Operação falhou! Saldo Insuficiente\nSaldo Atual: R$ {saldo}")
        return False
    elif excedeu_limite:
        print("Operação falhou! Valor do saque excede o limite (limite de R$ 500)")
        return False
    elif excedeu_saques:
        print(f"Operação falhou! Número máximo (3) de saques excedido\nSaques realizados hoje: {numero_saques}")
        return False
    else:
        return True
    
# <--- CONFIG  ---> #   
def get_local_datetime():
    local_timezone = get_localzone()
    local_date = datetime.now(local_timezone).strftime("%d-%m-%Y %H:%M:%S")
    
    return local_date

def menu():
    menu = """\n
    ==================== MENU =========================
    Escolha um número de 1-5 para realizar um operação:
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Saldo
    [5] Novo Usuário
    [6] Nova Conta
    [7] Listar Contas
    [8] Sair
    => """
    return input(textwrap.dedent(menu))

# <--- OPERAÇÕES ---> #
def make_deposit(valor, saldo, extrato, /):
    saldo += valor
    current_date = get_local_datetime()
    extrato += f"Depósito: R$ {valor:.2f} Horário: {current_date}\n"
    print("\n=== Depósito Realizado com Sucesso!!! ===")
    
    return saldo, extrato

def make_withdrawal(*,valor, saldo, extrato, numero_saques):
    saldo -= valor
    current_date = get_local_datetime()
    extrato += f"Saque: R$ {valor:.2f} Horário: {current_date}\n"
    numero_saques += 1
    print("\n=== Saque Realizado com Sucesso ===")
    return saldo, extrato, numero_saques

def view_statement(saldo,/,*,extrato):
    print("==================EXTRATOS======================")
    print("Não foram realizadas movimentações." if not extrato else f"Movimentações realizadas: \n{textwrap.dedent(extrato)}")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("================================================")

def view_balance(saldo):
    print(f"Saldo Atual: R$ {saldo}")
    
def create_user(usuarios):
    try:
        cpf = input("Informe o CPF (Somente Números): ")
        if cpf != cpf.isdigit() and len(cpf) != 11:
            print("CPF Inválido. Deve conter 11 Dígitos. Utilize Apenas Números. Tente Novamente!")
            return 
        
        usuario = filter_users(cpf, usuarios)
        
        if usuario:
            print("\n@@@ Já existe um usuário com esse CPF! @@@")
            return

        nome = name_validade()
        data_nascimento = date_validade()
        endereco = postal_validade()
        
        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf,  "endereco": endereco})
        
        print("=== Usuário Criado com Sucesso!!! ===")
    except ValueError:
        print("\n@@@ Erro interno durante a criação de usuário. Tente Novamente! @@@")
        
def create_account(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (Somente Números): ")
    usuario = filter_users(cpf, usuarios)
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, operação encerrada! @@@")

def list_accounts(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
            Titular:\t{conta['usuario']['endereco']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

# <--- APP --> #
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()
        
        # DEPOSITAR
        if opcao == "1":
            try:
                valor = float(input("Informe o valor do depósito: "))
                if valor > 0:
                    saldo, extrato = make_deposit(
                        valor, saldo, extrato
                    )
                else:
                    print("\n@@@ O valor de depósito precisa ser maior que 0 (zero). @@@")
            except ValueError:
                print("\n@@@ Número Inválido, por favor utilize o formato: 000.00 @@@")  
                      
        # SACAR       
        elif opcao == "2":
            try:
                valor = float(input("Informe o valor do saque: "))
                if valor > 0:
                    if exceptions(valor, saldo, limite, numero_saques, LIMITE_SAQUES):
                        saldo, extrato, numero_saques = make_withdrawal(
                            valor=valor, 
                            saldo=saldo, 
                            extrato=extrato, 
                            numero_saques=numero_saques
                        )                           
                else:
                    print("O valor do saque precisa ser maior que 0 (zero)")
            except ValueError:
                print("\nNúmero Inválido, por favor utilize o formato: 000.00")  
        
        # EXTRATO
        elif opcao == "3":
            view_statement(
                saldo, extrato=extrato
            )
            
        # SALDO
        elif opcao == "4":
            view_balance(saldo)
        
        # CRIAR USUARIO
        elif opcao == "5":
            create_user(usuarios)
            
        # CRIAR CONTA
        elif opcao == "6":
            numero_conta = len(contas) + 1
            conta = create_account(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                
        # LISTAR CONTAS
        elif opcao == "7":
            list_accounts(contas)
            
        elif opcao == "8":
            print("Finalizando Operação")
            break  
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()