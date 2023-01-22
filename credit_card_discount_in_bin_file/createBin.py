import struct
#cartoes = struct.Struct("20s 50s") #Estava armazenando o primeiro argumento de struct.pack em uma variável. Esse argumento diz o tipo da variável (string? float?) que será empacotada como byte. Também informa quantos bytes cada variável ocupará. No exercício, a primeira string ocupa 20 bytes e a segunda ocupa 50.


def main():
    try:
        with open("cartoes.txt", "r") as arquivoTxt:
            with open("cartoes.bin", "wb") as arquivoBin: #se o arquivo cartoes.bin não existir, a aplicação vai cria-lo.
                for linha in arquivoTxt:
                    entrada = linha.split('#') #split -> cada linha do arquivo texto será uma array. Os elementos dentro de cada array estão separados por # no ArquivoTexto.
                    print(entrada, len(entrada))
                    if len(entrada) > 1:
                        bandeira = entrada[0]
                        valor = entrada[1]
                        bloco = struct.pack("20s 50s", bandeira.encode("utf-8"), valor.encode("utf-8")) #encode() -> If no encoding is specified, UTF-8 will be used. struct.pack() -> pack variables as bytes
                        arquivoBin.write(bloco) #o método open() pode pedir o argumento de write in binary ("wb"), mas nada é escrito até utilizarmos o método write.
        print("Arquivo binário criado.")
    except IOError:
        print('Arquivo txt não encontrado.')


main()
