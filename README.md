# Filtros de Imagens Digitais

Projeto desenvolvido para a disciplina de Processamento Digital de Imagens.

O objetivo deste trabalho foi carregar uma imagem e aplicar diferentes filtros para observar seus efeitos na suavização da imagem e na detecção de bordas.

## Tecnologias utilizadas

* Python 3.11
* OpenCV
* NumPy
* Matplotlib

## Estrutura do projeto

```text
atividade-filtros/
│
├── imagens/
│   └── imagem.jpg
│
├── resultados/
│   ├── original.jpg
│   ├── media_3x3.jpg
│   ├── media_5x5.jpg
│   ├── mediana_3x3.jpg
│   ├── mediana_5x5.jpg
│   ├── sobel.jpg
│   └── comparacao_filtros.png
│
├── main.py
├── README.md
└── requirements.txt
```

## Filtros utilizados

### Filtro de Média

O filtro de média substitui cada pixel pela média dos pixels vizinhos, produzindo um efeito de suavização.

Testes realizados:

* Kernel 3x3
* Kernel 5x5

### Filtro de Mediana

O filtro de mediana substitui cada pixel pelo valor mediano da sua vizinhança, ajudando a reduzir ruídos e preservar melhor as bordas.

Testes realizados:

* Kernel 3x3
* Kernel 5x5

### Filtro de Sobel

O filtro de Sobel é utilizado para destacar bordas e contornos presentes na imagem.

## Resultados observados

Após a aplicação dos filtros foi possível observar que:

* O filtro de média deixou a imagem progressivamente mais borrada conforme o tamanho do kernel aumentou.
* O filtro de mediana também suavizou a imagem, mas preservou melhor alguns detalhes e contornos.
* O filtro de Sobel destacou claramente as bordas dos objetos presentes na imagem.

Além das imagens individuais, foi gerada uma imagem comparativa contendo todos os resultados lado a lado para facilitar a análise.

## Respostas da atividade

### a) Como a imagem original mudou após a aplicação de cada filtro?

O filtro de média reduziu detalhes e suavizou a imagem. O filtro de mediana também suavizou a imagem, porém preservando melhor algumas bordas. O filtro de Sobel destacou os contornos e as regiões de transição da imagem.

### b) Qual filtro foi mais eficaz para suavizar a imagem?

O filtro de média com kernel 5x5 apresentou a suavização mais intensa.

### c) Qual filtro foi mais eficaz para destacar as bordas?

O filtro de Sobel foi o mais eficaz para destacar as bordas da imagem.

### d) Quais situações podem exigir o uso de cada tipo de filtro em um projeto real?

**Filtro de Média**

* Suavização geral da imagem.
* Redução de pequenas variações e ruídos.

**Filtro de Mediana**

* Remoção de ruídos preservando melhor as bordas.
* Limpeza de imagens antes de outras etapas de processamento.

**Filtro de Sobel**

* Detecção de contornos.
* Visão computacional.
* Reconhecimento e segmentação de objetos.

## Como executar

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o programa:

```bash
py main.py
```

As imagens processadas serão geradas automaticamente na pasta `resultados`.
