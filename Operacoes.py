# NESSE ARQUIVO ESTÃO OPERAÇÕES QUE SÃO USADAS PARA GERAR UMA MATRIZ COM OS PIXELS DUMA IMAGEM OU MASCARA, 
# COLETAR ALGUMA INFORMAÇÃO DELAS OU PASSAR A IMAGEM NO FORMATO DE MATRIZ PARA O FORMATO DE LISTA.

#Legenda:
# listaImagem => lista com todas as informações da imagem
# matrizPixels => matriz com todos os pixels da imagem
# listaMascara => lista com todas as informações da mascara
# mascaraPixels => matriz com todos os pixels da mascara

def dimensaoImagem(listaImagem):          # Recebe uma listaImagem e retorna suas dimensões
    formato = listaImagem[0]  
    tamanho = listaImagem[2].split() 
    largura = int(tamanho[0])
    altura = int(tamanho[1])
    return (formato, largura, altura)

def geraMatriz(largura, altura):    # Recebe uma largura e altura e retorna uma matriz com essas dimensões preenchida com 0s
    matriz = []
    for _ in range(0, altura):
        matriz.append([0] * largura)
    return matriz

def pegaMatrizPixels(listaPixels, largura, altura): # Recebe uma listaPixels, altura e largura e retorna a matrizPixels da listaPixels
    matrizPixels = geraMatriz(largura, altura)
    for i in range (0, altura):
        for j in range (0, largura):
            matrizPixels[i][j] = int(listaPixels[j + (i * largura)])
    return matrizPixels

def pegaPixels(listaImagem, largura, altura): # Recebe uma listaImagem, altura e largura e separa os pixels das demais informações da listaImagem
    lista = listaImagem[3:len(listaImagem)]   # Retira da lista o que não for pixel
    listaPixels = []
    for linha in lista: # Pega as cadeias de pixel
        for c in linha: # Percorre as cadeias pegando cada pixel
            if c != '\n':
                listaPixels.append(c) # Monta uma lista todos os pixels
    matrizPixels = pegaMatrizPixels(listaPixels, largura, altura) # Com a lista no formato certo pode chamar a pegaMatrizPixels
    return matrizPixels

def conteudoMascara(listaMascara):      # Recebe uma listaMascara e retorna a mascaraPixels dela
    mascaraPixels = [l.split() for l in listaMascara[1:len(listaMascara)]] # Exclui a informação de tamanho e separa pelos espaços em branco
    for li in mascaraPixels:
        for i in range(0, len(li)):
            li[i] = int(li[i])      # Transforma os pixels da matriz em inteiros
    return mascaraPixels

def reflexao(mascaraPixels, largura, altura): # Faz a reflexão da máscara, gira em 180º, para usar na dilatação
    mascaraRefletida = geraMatriz(largura, altura)
    for i in range(0, altura):
        for j in range(0, largura):
            mascaraRefletida[i][j] = mascaraPixels[(altura - 1) - i][(largura - 1) - j]
    return mascaraRefletida

def formatoPBM(matrizPixels, formato, largura, altura): # Recebe a matrizPixels da imagem e todas as outras infomações para retornar uma listaImagem com essas informações
    novaListaImagem = [formato.strip('\n'), "# Imagem Processada", str(largura) + " " + str(altura)] # Bota as informações iniciais da imagem na lista
    linha = ""   # String usada para juntar os pixels novamente numa cadeia, ex: "000000..." => 70 zeros
    for i in range(0, altura):
        for j in range(0, largura):
            linha += str(matrizPixels[i][j])   # Bota o pixel na string
            if len(linha) == 70:               # Tamanho da cadeia de pixels na linha (PBM => 70)
                novaListaImagem.append(linha)  # Bota a cadeia de pixels na lista
                linha = ""                     # Reseta a string
            if i == altura-1 and j == largura-1 and linha != "": # Se esta lendo o ultimo elemento e a linha tem pelo menos um pixel na string
                novaListaImagem.append(linha)                    # Bota a cadeia de pixels na lista
    return novaListaImagem