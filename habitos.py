def adicionar_habito(habitos):
    nome = input("Digite o nome do hábito: ")
    categoria = input("Categoria (ex: Saúde, Estudo): ")
    habito = {"nome": nome, "categoria": categoria, "historico": []}
    habitos.append(habito)
    print(f"\n✅ Hábito '{nome}' adicionado com sucesso!\n")

def listar_habitos(habitos):
    if not habitos:
        print("Nenhum hábito cadastrado.")
        return
    print("\n📋 Seus hábitos:")
    for i, h in enumerate(habitos, start=1):
        print(f"{i}. {h['nome']} ({h['categoria']})")

def menu():
    TESTE = True
    if TESTE:
        habitos = [
            {"nome": "Beber água", "categoria": "Saúde", "historico": []},
            {"nome": "Estudar Python", "categoria": "Estudo", "historico": []},
        ]
    else:
        habitos = []

    while True:
        print("\n--- 📊 Gerenciador de Hábitos ---")
        print("1. Adicionar hábito")
        print("2. Listar hábitos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_habito(habitos)
        elif opcao == "2":
            listar_habitos(habitos)
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")
