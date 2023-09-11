while True:

    letra = str(input("Digite uma letra ou digite Sair para encerrar:"))

    letra= letra.lower()

    if letra == 'sair':
        print("Encerrando o programa.")
        break

    if letra.isalpha():
        if letra == 'a':
            print("Vogal")
        elif letra == 'e':
            print("Vogal")
        elif letra == 'i':
            print("Vogal")
        elif letra == 'o':
            print("Vogal")
        elif letra == 'u':
            print("Vogal")
        
        else: print("Consoante")
    else: print ("Não é uma letra")          