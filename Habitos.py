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
