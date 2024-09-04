carrinho = []
preco = []

while True:
    print("Escolha uma forma de login")
    print("1 - Cliente")
    print("2 - Funcionário")
    usuario = int(input("Digite a opcão: "))
    if usuario == 1:
        nc = input("Digite seu nome: ")
        cp = int(input("Digite seu CPF: "))
        print("Concluído")
    if usuario == 2:
        n = input("Digite seu nome: ")
        d = int(input("Digite sua data de nascimento: "))
        c = int(input("Digite seu CPF: "))
        m = int(input("Digite sua matricula: "))
        print("Concluído")    
    
    while True:
        print("1 - Alimentos")
        print("2 - Higiene")
        print("3 - Limpeza")
        print("4 - Finalizar as compras")
        print("5 - Retirar os produtos do carrinho")
        print("6 - Sair do Usuário")
        menu = int(input("Digite um número de acordo com a categoria desejada: "))
        
        while True:
            if menu == 1:
                print("1 - Arroz R$15")
                print("2 - Leite R$10")
                print("3 - Carne R$35")
                print("4 - Sair")
                alimentos = int(input("Digite o número de acordo com o produto desejado: "))
                if alimentos == 1:
                    carrinho.append("Arroz R$15")
                    preco.append(15)
                if alimentos == 2:
                    carrinho.append("Leite R$10")
                    preco.append(10)
                if alimentos == 3:
                    carrinho.append("Carne R$35")
                    preco.append(35)
                if alimentos == 4:
                    print("Escolha uma das opcões: ")
                    print("1 - Continuar as compras")
                    print("2 - Retirar do carrinho")
                    print("3 - Ir para o menu")
                    opc = int(input("Digite: "))
                    if opc == 1:
                        print
                    if opc == 2:
                        print(carrinho)
                        rt1 = int(input("digite um número de acordo com a ordem dos produtos colocados no carrinho: "))
                        del carrinho[rt1]
                        del preco[rt1]
                        print(carrinho)
                        print("Removido com sucesso")
                    if opc == 3:
                        break                    

            if menu == 2:
                print("1 - Pasta de dente R$5")
                print("2 - Fio dental R$4")
                print("3 - Sabonete de rosto R$3")
                print("4 - Sair")
                higiene = int(input("Digite o número de acordo com o produto desejado: "))
                if higiene == 1:
                    carrinho.append("Pasta de dente R$5")
                    preco.append(5)
                if higiene == 2:
                    carrinho.append("Fio dental R$4")
                    preco.append(4)
                if higiene == 3:
                    carrinho.append("Sabonete de rosto R$3")
                    preco.append(3)
                if higiene == 4:
                    print("Deseja: ")
                    print("1 - Continuar as compras")
                    print("2 - Retirar os produtos do carrinho")
                    print("3 - Ir para o menu principal")
                    opc2 = int(input("Digite: "))
                    if opc2 == 1:
                        print
                    if opc2 == 2:
                        print(carrinho)
                        rt2 = int(input("digite um número de acordo com a ordem dos produtos colocados no carrinho: "))
                        del carrinho[rt2]
                        del carrinho[rt2]
                        print(carrinho)
                        print("Removido com sucesso")
                    if opc2 == 3:
                        break
                        
            if menu == 3:
                print("1 - Multi Uso R$8")
                print("2 - Detergente R$2.5")
                print("3 - Sabão em pó R$7")
                print("4 - Sair")
                plimpeza = int(input("Digite o número de acordo com o produto desejado: "))
                if plimpeza == 1:
                    carrinho.append("Multi Uso R$8")
                    preco.append(8)
                if plimpeza == 2:
                    carrinho.append("Detergente R$2.5")
                    preco.append(2.5)
                if plimpeza == 3:
                    carrinho.append("Sabão em pó R$7")
                    preco.append(7)
                if plimpeza == 4:
                    print("Deseja: ")
                    print("1 - Continuar as compras")
                    print("2 - Retirar os produtos do carrinho")
                    print("3 - Ir para o menu principal")
                    opc3 = int(input("Digite: "))
                    if opc3 == 1:
                        print
                    if opc3 == 2:
                        print(carrinho)
                        rt3 = int(input("digite um número de acordo com a ordem dos produtos colocados no carrinho: "))
                        del carrinho[rt3]
                        del carrinho[rt3]
                        print(carrinho)
                        print("Removido com sucesso")
                    if opc3 == 3:
                        break

            if menu == 4:
                for ordem in carrinho:
                    print(ordem)
                
                soma = sum(preco)
                soma1 = soma + (soma * 0.25 )
                print(f'Preço total: R${soma1}')
                print("Selecione uma forma de pagamento:")
                print("1 - Dinheiro")
                print("2 - Pix")
                print("3 - Cartão")
                print("4 - Voucher")
                print("5 - Sair")
                pagamento = int(input("Digite a opção de pagamento: "))
                if pagamento == 1:
                    dinheiro = float(input("Digite a quantidade de dinheiro que deseja: "))
                    if dinheiro == soma1:
                        calculo = dinheiro - soma1
                        print("Pagamento concluído")
                        print(f'Troco: R${calculo}')
                        break
                    elif dinheiro > soma1:
                        calculo2 = dinheiro - soma1
                        print('Pagamento concluído')
                        print(f'Troco: R${calculo2}')
                        break
                    elif dinheiro < soma1:
                        print("Dinheiro insuficiente, solicite outra forma de pagamento")
                if pagamento == 2:
                    saldo = float(input("Qual o seu saldo?: "))
                    if saldo == soma1:
                        calculo = saldo - soma1
                        print("Pagamento com sucesso")
                        break
                    elif saldo > soma1:
                        calculo2 = saldo - soma1
                        print("Pagamneto com sucesso")
                        break
                    elif saldo < soma1:
                        print("Insuficiente, selecione outra forma de pagamento")
                if pagamento == 3:
                    print("1 - Crédito")
                    print("2 - Débito")
                    cartao = int(input("Qual tipo de cartão deseja usar: "))
                    if cartao == 1:
                        saldo1 = float(input("Qual saldo existente: "))
                        if saldo1 == soma1:
                            calculo1 = saldo1 - soma1
                            print("Pagamento com sucesso")
                            break
                        elif saldo1 > soma:
                            calculo2 = saldo1 - soma1
                            print("Pagamento com sucesso")
                            break
                        elif saldo1 < soma1:
                            print("Saldo Insuficiente, selecione outra forma de pagamento e tente novamente")
                    if cartao == 2:
                        saldo3 = float(input("Qual saldo existente: "))
                        if saldo3 == soma:
                            calculo3 = saldo3 - soma1
                            print("Pagamento com sucesso")
                            break
                        elif saldo3 > soma:
                            calculo2 = saldo3 - soma1
                            print("Pagamento com sucesso")
                            break
                        elif saldo3 < soma1:
                            print("Saldo Insuficiente, selecione outra forma de pagamento e tente novamente")
                if pagamento == 4:
                    print("Pagamento com sucesso")
                    break
                if pagamento == 5:
                    break
            
            if menu == 5:
                print(carrinho)
                rt4 = int(input("digite um número de acordo com a ordem dos produtos colocados no carrinho: "))
                del carrinho[rt4]
                del preco[rt4]
                print(carrinho)
                print("Removido com sucesso")
                break
        
            if menu == 6:
                print('Saindo do Usuário')
                break