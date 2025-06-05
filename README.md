# 🐍 gerenciador_de_habitos.py

Gerenciador de Hábitos (em Python).  
Este projeto é um gerenciador simples de hábitos feito em Python, com foco em organização pessoal, produtividade e saúde.

## 💡 O que o projeto faz?

Este projeto permite:

✅ Adicionar novos hábitos com nome e categoria  
📋 Listar todos os hábitos cadastrados  
🔄 Trabalhar com uma lista de hábitos vazia ou já preenchida para testes  
🧪 Utilizar dados de exemplo para testes

## 🧪 Modo de teste

No início do dados_teste.py, você encontra a variável `TESTE`:

Se TESTE = True, o programa inicia com hábitos de exemplo já cadastrados.

Se TESTE = False, a lista de hábitos começa vazia.



## 🧱 Estrutura do Projeto
- `main.py`: interface principal do usuário (menu de interação)
- `habitos.py`: módulo com funções de manipulação de hábitos
- `test_habitos.py`: testes automatizados usando o framework `unittest`

▶️ Como rodar

✅ Opcionais:

Você pode testar o projeto mesmo sem terminal, via Google Colab:

Copie o conteúdo de habitos.py e main.py em células separadas.

No final, chame menu() para iniciar o programa.

Ou, localmente:

Salve os arquivos habitos.py e main.py na mesma pasta.

Execute com:  

✍️ Exemplo de uso  

--- 📊 Gerenciador de Hábitos ---  

Adicionar hábito  

Listar hábitos  

Sair  

Escolha uma opção: 2  

📋 Seus hábitos:  
  
Beber água (Saúde)  

Estudar Python (Estudo)  

...

🚀 Melhorias implementadas (branch melhorias)

✅ Modularização: separação de funções em habitos.py

✅ Testes automatizados com unittest (test_habitos.py)

✅ Organização de responsabilidades: main.py lida só com a execução

✅ Modo de teste com hábitos pré-preenchidos

✅ Código pronto para demonstração no Colab ou execução local


