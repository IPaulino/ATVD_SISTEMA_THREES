class SistemaStreaming:
    def __init__(self):
        # Criando um catálogo com filmes e séries
        self.catalogo = {
            "Filmes": ["Esqueceram de Mim 2", "Ghost do Outro lado da Vida", "Pokémon 4: Viajentes do Tempo", "Bem-vinda a Quixeramobim"],
            "Séries": ["The Good Doctor", "Grey's Anatomy", "Pokémon", "(Em Breve)"]
        }

    def exibir_catalogo(self):
        # Função para mostrar o catálogo
        for categoria, conteudo in self.catalogo.items():
            print(f"\nCatálogo de {categoria}:")
            for item in conteudo:
                print(f"- {item}")

def main():
    sistema = SistemaStreaming()
    div = "--"*20

    print("Bem-vindo ao ThreeS++\nSistema Simplificado de Streaming")

    while True:
        # Menu de opções
        print(div)
        print("Menu:")
        print("1. Visualizar Catálogo")
        print("2. Sair \n"+div)

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            print(div)
            # Se escolher 1, mostra o catálogo
            sistema.exibir_catalogo()
        elif escolha == "2":
            # Se escolher 2, sai do sistema
            print("\nSaindo do ThreeS++. Até mais!")
            break
        else:
            # Se escolher qualquer outra coisa, avisa que é inválido
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
