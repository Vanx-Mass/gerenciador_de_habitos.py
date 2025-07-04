# 🧠 Gerenciador de Hábitos no Terminal
#Este projeto permite cadastrar hábitos, visualizar e acompanhar sua prática diária.


# Inicializa com exemplo ou lista vazia
TESTE = True  # Possbilita alterar para False para usar lista vazia

def inicializar_habitos():
    if TESTE:
        return [
            {"nome": "Beber água", "categoria": "Saúde", "historico": []},
            {"nome": "Estudar Python", "categoria": "Estudo", "historico": []},
            {"nome": "Ler 10 páginas de um livro", "categoria": "Crescimento pessoal", "historico": []},
            {"nome": "Meditar 5 minutos", "categoria": "Saúde", "historico": []},
            {"nome": "Dormir antes das 23h", "categoria": "Saúde", "historico": []},
            {"nome": "Fazer uma caminhada", "categoria": "Bem-estar", "historico": []},
            {"nome": "Organizar a mesa de trabalho", "categoria": "Produtividade", "historico": []},
            {"nome": "Evitar redes sociais pela manhã", "categoria": "Foco", "historico": []}
        ]
    return []

habitos = inicializar_habitos()

# Adiciona hábitos
def adicionar_habito():
    nome = input("Digite o nome do hábito: ")
    categoria = input("Categoria (ex: Saúde, Estudo): ")
    habito = {"nome": nome, "categoria": categoria, "historico": []}
    habitos.append(habito)
    print(f"\n✅ Hábito '{nome}' adicionado com sucesso!\n")

# Lista hábitos
def listar_habitos():
    if not habitos:
        print("Nenhum hábito cadastrado.")
        return
    print("\n📋 Seus hábitos:")
    for i, h in enumerate(habitos, start=1):
        print(f"{i}. {h['nome']} ({h['categoria']})")

# Menu principal
def menu():
    while True:
        print("\n--- 📊 Gerenciador de Hábitos ---")
        print("1. Adicionar hábito")
        print("2. Listar hábitos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_habito()
        elif opcao == "2":
            listar_habitos()
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida.")

menu()
