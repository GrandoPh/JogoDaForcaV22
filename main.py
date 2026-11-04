
import os

jogar_novamente = "s"

while jogar_novamente == "s":

    # Cadastro do desafiante
    nome_desafiante = input("Nome do desafiante: ")
    palavra = input("Digite a palavra secreta: ").upper()

    dica1 = input("Digite a primeira dica: ")
    dica2 = input("Digite a segunda dica: ")
    dica3 = input("Digite a terceira dica: ")

    # Limpa a tela
    os.system("cls")

    # Cadastro do desafiado
    nome_desafiado = input("Nome do desafiado: ")

    erros = 0
    dicas_usadas = 0
    letras_digitadas = ""
    palavra_oculta = ""

    # Cria os asteriscos da palavra
    for letra in palavra:
        if letra == " ":
            palavra_oculta += " "
        else:
            palavra_oculta += "*"

    # Início do jogo
    while erros < 6 and palavra_oculta != palavra:

        os.system("cls")

        print("========== JOGO DA FORCA ==========")
        print("Desafiante:", nome_desafiante)
        print("Desafiado:", nome_desafiado)
        print("Erros:", erros, "de 6")
        print("Letras tentadas:", letras_digitadas)
        print()

        # Desenha o boneco conforme os erros
        if erros == 0:
            boneco = [
                "  _____",
                "  |   |",
                "  |   O",
                "  |  /|\\",
                "  |  / \\",
                "__|__"
            ]

        elif erros == 1:
            boneco = [
                "  _____",
                "  |   |",
                "  |   O",
                "  |  /|\\",
                "  |  /",
                "__|__"
            ]

        elif erros == 2:
            boneco = [
                "  _____",
                "  |   |",
                "  |   O",
                "  |  /|\\",
                "  |",
                "__|__"
            ]

        elif erros == 3:
            boneco = [
                "  _____",
                "  |   |",
                "  |   O",
                "  |  /|",
                "  |",
                "__|__"
            ]

        elif erros == 4:
            boneco = [
                "  _____",
                "  |   |",
                "  |   O",
                "  |   |",
                "  |",
                "__|__"
            ]

        elif erros == 5:
            boneco = [
                "  _____",
                "  |   |",
                "  |   O",
                "  |",
                "  |",
                "__|__"
            ]

        # Mostra o boneco à esquerda e a palavra à direita
        print("FORCA                         PALAVRA")
        print()

        print(boneco[0])
        print(boneco[1])

        print(boneco[2] + "                  ", end="")

        for letra in palavra_oculta:
            print(letra, end=" ")

        print()

        print(boneco[3])
        print(boneco[4])
        print(boneco[5])

        print()
        print("1 - Tentar uma letra")
        print("2 - Pedir uma dica")

        opcao = input("Escolha uma opção: ")

        # Escolha da opção
        if opcao == "2":

            if dicas_usadas == 3:
                print("Você já utilizou as três dicas!")
                input("Pressione ENTER para continuar...")
                continue

            dicas_usadas += 1

            if dicas_usadas == 1:
                print("Dica 1:", dica1)

            elif dicas_usadas == 2:
                print("Dica 2:", dica2)

            elif dicas_usadas == 3:
                print("Dica 3:", dica3)

            letra = input("Agora tente uma letra: ").upper()

        elif opcao == "1":
            letra = input("Digite uma letra: ").upper()

        else:
            print("Opção inválida!")
            input("Pressione ENTER para continuar...")
            continue

        # Verifica se foi digitado apenas um caractere
        if len(letra) != 1:
            print("Digite apenas uma letra!")
            input("Pressione ENTER para continuar...")
            continue

        # Verifica se a letra já foi utilizada
        if letra in letras_digitadas:
            print("Você já tentou essa letra!")
            input("Pressione ENTER para continuar...")
            continue

        letras_digitadas += letra + " "

        # Verifica se a letra existe na palavra
        if letra in palavra:

            nova_palavra = ""
            posicao = 0

            for caractere in palavra:

                if caractere == letra:
                    nova_palavra += letra
                else:
                    nova_palavra += palavra_oculta[posicao]

                posicao += 1

            palavra_oculta = nova_palavra

            print("Parabéns! Você acertou uma letra!")

        else:
            erros += 1
            print("Você errou! O boneco perdeu uma parte.")

        input("Pressione ENTER para continuar...")

    # Resultado final
    os.system("cls")

    print("========== FIM DE JOGO ==========")
    print("Palavra:", palavra)
    print()

    if palavra_oculta == palavra:
        print("Parabéns,", nome_desafiado + "!")
        print("Você descobriu a palavra!")
        print(nome_desafiante, "perdeu o desafio!")

    else:
        print("Que pena,", nome_desafiado + "!")
        print("Você perdeu o jogo!")
        print("O vencedor foi:", nome_desafiante)
        print()
        print("O boneco desapareceu!")

        # Desenho da forca vazia
        print("  _____")
        print("  |   |")
        print("  |")
        print("  |")
        print("__|__")

    print()

    jogar_novamente = input(
        "Desejam jogar novamente? (s/n): "
    ).lower()

    os.system("cls")

print("Obrigado por jogar!")
