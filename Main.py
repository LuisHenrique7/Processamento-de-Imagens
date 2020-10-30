import Arquivos
import Operacoes
import OperacoesProcessamento

# Tira o ruido part 1

arquivo = input("Escreva o nome do arquivo com a imagem: ")
listImag = Arquivos.lerImagemPBM(arquivo)
formato, largura, altura = Operacoes.dimensaoImagem(listImag)
pixels = Operacoes.pegaPixels(listImag, largura, altura)
enderecoMask = 'mask3.txt'
mediana = OperacoesProcessamento.mediana(pixels, altura, largura, enderecoMask)
enderecoMask = 'mask1.txt'
dilatacao = OperacoesProcessamento.dilatacao(mediana, altura, largura, enderecoMask)

# Conta e circula palavras part 2

colunas, linhas, listaPontosLinhas, listaPontosColunas, listaQuantidadeLinhas, listaLinhasExtras = OperacoesProcessamento.contaColunasELinhas(dilatacao,  altura, largura)
palavras , listaDeX, listaDeY = OperacoesProcessamento.contaPalavras(dilatacao, altura, largura, listaPontosLinhas,listaPontosColunas, listaQuantidadeLinhas, listaLinhasExtras)
print("Número de colunas:", colunas)
print("Número de linhas:", linhas)
print("Número de palavras:", palavras)

circuladas = OperacoesProcessamento.circularPalavras(dilatacao, listaDeX, listaDeY)

novaImg = Operacoes.formatoPBM(circuladas, formato, largura, altura)
Arquivos.criaImagemPBM(novaImg)

