# PLN-Text-Summarization

Este repositório reúne projetos de **Processamento de Linguagem Natural (PLN)** desenvolvidos em Python, com foco em técnicas de pré-processamento, análise e sumarização automática de textos.

## Sobre o projeto

O projeto principal deste repositório realiza a **sumarização automática de textos** usando artigos da Wikipédia. O código utiliza as bibliotecas `wikipedia`, `nltk` e `string` para:

- Buscar e baixar textos da Wikipédia em português
- Realizar pré-processamento: limpeza, remoção de stopwords e pontuação
- Tokenizar e aplicar stemming (radicalização das palavras)
- Calcular a frequência dos radicais das palavras
- Pontuar frases com base na frequência dos radicais
- Selecionar as frases mais relevantes para compor um resumo automático

## Como funciona

1. O usuário escolhe um artigo da Wikipédia (exemplo: "Neurociência").
2. O texto é baixado e pré-processado.
3. O algoritmo pontua cada frase do texto conforme a frequência dos radicais das palavras.
4. As frases com maior pontuação são selecionadas para formar o resumo final.

## Como executar

1. Instale as dependências:
   ```
   pip install wikipedia nltk
   ```
2. Execute o script principal:
   ```
   python Sumarizacao_textos.py
   ```
3. O resumo gerado será exibido no terminal.

## Estrutura do repositório

- `Sumarizacao_textos.py`: Script principal para sumarização de textos da Wikipédia.
- Outros scripts e notebooks relacionados a PLN podem ser adicionados aqui.

## Exemplos de uso

Você pode adaptar o código para resumir textos de diferentes temas, como:
- Inteligência Artificial
- História do Brasil
- Ciência de Dados
- Saúde Pública

## Contribuição

Sinta-se à vontade para abrir issues, enviar sugestões ou contribuir com novos projetos de PLN!

---

**Autor:**  
Priscila Jaroczinski  
[prijki](https://github.com/prijki/)
