print("Bem-vindo ao nosso e-commerce!")
nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
print(f"Olá, {nome}! Você está cadastrado com o e-mail {email}.\n")
produtos = [
    {"nome": "Camiseta", "preco": 50.00},
    {"nome": "Calça", "preco": 120.00},
    {"nome": "Tênis", "preco": 250.00},
    {"nome": "Boné", "preco": 30.00},
]
print("Produtos disponíveis:")
for i, produto in enumerate(produtos):
    print(f"{i + 1}. {produto['nome']} - R$ {produto['preco']:.2f}")
carrinho = []
while True:
    escolha = input("\nDigite o número do produto que deseja comprar (ou 'sair' para finalizar): ")
    if escolha.lower() == 'sair':
        break
    try:
        escolha = int(escolha) - 1
        if 0 <= escolha < len(produtos):
            quantidade = int(input(f"Quantas unidades de {produtos[escolha]['nome']} você deseja? "))
            if quantidade > 0:
                carrinho.append({
                    "produto": produtos[escolha]["nome"],
                    "preco": produtos[escolha]["preco"],
                    "quantidade": quantidade
                })
                print(f"{quantidade} x {produtos[escolha]['nome']} adicionado(s) ao carrinho.")
            else:
                print("Quantidade inválida. Tente novamente.")
        else:
            print("Produto não encontrado. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número ou 'sair'.")
total = sum(item["preco"] * item["quantidade"] for item in carrinho)
print(f"\nTotal da compra: R$ {total:.2f}")
while True:
    try:
        valor_pago = float(input("Digite o valor que você deseja pagar: R$ "))
        if valor_pago >= total:
            troco = valor_pago - total
            print(f"Pagamento realizado com sucesso! Troco: R$ {troco:.2f}")
            break
        else:
            print("Valor insuficiente. Por favor, insira um valor maior ou igual ao total.")
    except ValueError:
        print("Entrada inválida. Digite um valor numérico.")

print("\nObrigado por comprar conosco! Volte sempre.")