# NESSE ARQUIVO ESTÃO OPERAÇÕES QUE SÃO USADAS PARA LER OU ESCREVER ARQUIVOS DE IMAGENS OU MASCARAS

#Legenda:
# listaImagem => lista com todas as informações da imagem
# matrizPixels => matriz com todos os pixels da imagem
# listaMascara => lista com todas as informações da mascara
# mascaraPixels => matriz com todos os pixels da mascara

def lerImagemPBM(endereco):               # Lê o arquivo com a imagem e transforma numa listaImagem
    arquivo = open(endereco,'r')
    if (arquivo == ''):
        print("Erro ao carregar arquivo")
        arquivo.close()
        return []
    else:
        listaImagem = arquivo.readlines()
        arquivo.close()
        return listaImagem

def criaImagemPBM(listaImagem):                  # Recebe uma listaImagem e escreve num arquivo.pbm
    nome = input("Escreva o nome do arquivo a ser criado: ")
    nome += ".pbm"
    arqCriado = open (nome,'w')
    for i in listaImagem:
        arqCriado.write(i + '\n')
    arqCriado.close()

def lerMascara(arquivo):            # Lê o arquivo com a mascara e transforma numa listaMascara
    arquivo = open(arquivo,'r')
    if (arquivo == ''):
        print("Erro ao carregar arquivo")
        arquivo.close()
        return []
    else:
        listaMascara = arquivo.readlines()
        arquivo.close()
        return listaMascara