import wikipedia
import nltk
import string
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

# Utilização da biblioteca da wikipedia para o download de datasets textuais
wikipedia.set_lang("pt")

# Utilizando o dataset de Neurociência para fazer o resumo de texto.
documento = wikipedia.page("Neurociência")
documento = documento.content

print(documento)

##### PRÉ PROCESSAMENTO DOS DADOS #######

documento = documento.replace("\n", " ")
documento = documento.replace("  ", " ")


# Utilizando as stopwords da biblioteca nltk para a lingua portuguesa e a biblioteca string para a limpeza dos dados
stopwords = nltk.corpus.stopwords.words('portuguese')
punctuation = string.punctuation
    
#Processo de tokenização
tokens = word_tokenize(documento)

# Processo de Stemming que retira a raiz das palavras
stemmer = SnowballStemmer("portuguese")
raizes = []
for token in tokens:
    if not token in punctuation and not token in stopwords:
        raizes.append(stemmer.stem(token))

#Frequencia das raizes 
frequencia_das_raizes = {
    raiz: raizes.count(raiz) for raiz in set(raizes)
    }

# print(sorted(frequencia_das_raizes.items(), key=lambda x: x[1], reverse=True))
     
del frequencia_das_raizes["=="]
del frequencia_das_raizes["''"]
del frequencia_das_raizes["``"]

# Dividindo o artigo em sentenças (Frases)
frases = sent_tokenize(documento)

ranking_frases = []

## Atribuindo pontuações as frases com base na frequencia das palavras tokenizadas.
for frase in frases:
    pontos = 0
    tokens = word_tokenize(frase)
    raizes = [stemmer.stem(token) for token in tokens]
    for raiz in raizes:
        pontos += frequencia_das_raizes.get(raiz, 0)
    ranking_frases.append(pontos / len(tokens))
     
# print(ranking_frases)

# Obtendo a média de pontos das frases
media_de_pontos = sum(ranking_frases) / len(ranking_frases)
media_de_pontos

resumo = []

# Criando um resumo do texto conforme a média da frequencia de palavras, e com 8 frases.
for i, frase in enumerate(frases):
    pontos = ranking_frases[i]
    if pontos > (media_de_pontos):
        resumo.append(frase)
    if len(resumo) == 8:
        resumo = " ".join(resumo)
        break

print("######### RESUMO CRIADO : ", resumo)
