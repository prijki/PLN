def simular_chatbot():

    #Entrada de texto do usuário no chatbot
    entrada = "O produto é extremamente ótimo, é terrível que tenham parado de vender, fiquei chateado pois o produto era muito bom."

    # 1.Definição de sentimentos bons e ruins.
    bad_sentiments = ["odeio", "ruim", "péssimo", "terrível", "chateado"]
    good_sentiments = ["adoro", "amo", "excelente", "bom", "ótimo", "feliz"]

    # 2.Lógica condicional para verificar presença das palavras boas ou ruins na entrada do usuário.
    
    # 2.1 tokenização da entrada de palavras.
    texto = ["O","produto","é","extremamente","ótimo","é","terrível","que","tenham","parado","de","vender","fiquei","chateado","pois","o","produto","era","muito","bom"]

    # 3. Variáveis de contagem de sentimentos detectados
    positivos = 0
    negativos = 0

    # 4. Lógica condicional: verifica cada palavra da mensagem
    for palavra in texto:
        if palavra.lower() in good_sentiments:   # verifica se é positiva
            positivos += 1
        elif palavra.lower() in bad_sentiments: # verifica se é negativa
            negativos += 1

    # 5. Classificação final do sentimento da mensagem
    if positivos > negativos:
        sentimento_detectado = "positivo"
    elif negativos > positivos:
        sentimento_detectado = "negativo"
    else:
        sentimento_detectado = "neutro"

    # 6. Retorno com entrada analisada e sentimento detectado
    return {
        "entrada": entrada,
        "tokens": texto,
        "sentimento_detectado": sentimento_detectado
    }


#hdeyiwo

import nltk
from textblob import TextBlob
import random

nltk.download('punkt')
nltk.download('movie_reviews')
nltk.download('averaged_perceptron_tagger')

# Piadas e charadas fora do loop
piadas = [
    "— Por que o livro foi ao médico? — Porque ele tinha muitas páginas em branco! 😄",
    "— Qual é o cúmulo do absurdo? — Pintar o chão de água! 😂",
    "— O que o zero disse para o oito? — Belo cinto! 😆",
    "— Por que o tomate foi ao banco? — Porque ele queria virar extrato! 🍅",
    "— O que o chão disse para a mesa? — Pare de me apoiar! 😄"
]

charadas = [
    ("Quanto mais você tira, maior fica?", "buraco"),
    ("O que tem cabeça, mas não pensa?", "alfinete"),
    ("O que é que cai em pé e corre deitado?", "chuva"),
    ("O que é que quanto mais se seca, mais molhado fica?", "toalha"),
    ("O que tem dentes mas não morde?", "pente")
]

def analisar_sentimento(mensagem):
    analise = TextBlob(mensagem)
    if analise.sentiment.polarity > 0:
        return 'positivo'
    elif analise.sentiment.polarity == 0:
        return 'neutro'
    else:
        return 'negativo'

def retorno(sentimento):
    if sentimento == "positivo":
        return "Que bom que se divertiuu!!! Fico feliz que tenha gostado, volte mais vezes."
    elif sentimento == "neutro":
        return "Poxa espero que possa te alegrar na próxima tentativa."
    else:
        return "Sinto muito que não tenha gostado, vou tentar melhorar para uma próxima vez."

def iniciar_chat():
    while True:
        boas_vindas = """\nOlá! Bem-vindo ao RisoChat!! 
__________________________ 
1. Para ouvir uma piada. 
2. Para uma charada. 
3. Para sair"""
        print(boas_vindas)
        option = input("Digite sua opção: ")

        if option == '1':
            piada = random.choice(piadas)
            print("\n" + piada)
        elif option == '2':
            charada, resposta_certa = random.choice(charadas)
            print("\nO que é, o que é:", charada)
            resposta = input("Digite sua resposta: ")
            if resposta.lower().strip() == resposta_certa:
                print("Acertou! 🎉")
            else:
                print(f"Sinto muito, a resposta era '{resposta_certa}'.")
        elif option == '3':
            print("Sinto muito que não queira se divertir. Até a próxima!")
            break
        else:
            print("Opção inválida, tente novamente.")
            continue

        mensagem = input("\nConseguiu dar uma boa risada? O que achou da minha performance? ")
        print(f"(Debug: polaridade={TextBlob(mensagem).sentiment.polarity})")  # para ver polaridade
        print(retorno(sentimento=analisar_sentimento(mensagem)))

        continuar = input("\nDeseja tentar novamente? s/n: ")
        if continuar.lower() != 's':
            print("Obrigado por brincar com o RisoChat! Até mais!")
            break

iniciar_chat()
