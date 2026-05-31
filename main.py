import cv2
import os
import matplotlib.pyplot as plt

# Cria a pasta de saída caso ela não exista
os.makedirs("resultados", exist_ok=True)

# Carrega a imagem
imagem = cv2.imread("imagens/imagem.jpg")

# Verifica se a imagem foi encontrada
if imagem is None:
    print("Erro: imagem não encontrada!")
    exit()

# Salva a imagem original
cv2.imwrite("resultados/original.jpg", imagem)

# Aplica filtro de média
media_3 = cv2.blur(imagem, (3, 3))
media_5 = cv2.blur(imagem, (5, 5))

cv2.imwrite("resultados/media_3x3.jpg", media_3)
cv2.imwrite("resultados/media_5x5.jpg", media_5)

# Aplica filtro de mediana
mediana_3 = cv2.medianBlur(imagem, 3)
mediana_5 = cv2.medianBlur(imagem, 5)

cv2.imwrite("resultados/mediana_3x3.jpg", mediana_3)
cv2.imwrite("resultados/mediana_5x5.jpg", mediana_5)

# Converte para tons de cinza para aplicar Sobel
cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Calcula as bordas horizontais e verticais
sobel_x = cv2.Sobel(cinza, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(cinza, cv2.CV_64F, 0, 1, ksize=3)

# Converte os resultados para exibição
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Combina as bordas encontradas
sobel = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)

cv2.imwrite("resultados/sobel.jpg", sobel)

# Cria uma imagem comparando todos os filtros
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

imagens = [
    (cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB), "Original"),
    (cv2.cvtColor(media_3, cv2.COLOR_BGR2RGB), "Media 3x3"),
    (cv2.cvtColor(media_5, cv2.COLOR_BGR2RGB), "Media 5x5"),
    (cv2.cvtColor(mediana_3, cv2.COLOR_BGR2RGB), "Mediana 3x3"),
    (cv2.cvtColor(mediana_5, cv2.COLOR_BGR2RGB), "Mediana 5x5"),
    (sobel, "Sobel")
]

for ax, (img, titulo) in zip(axes.ravel(), imagens):

    # Exibe imagem colorida ou em escala de cinza
    if len(img.shape) == 2:
        ax.imshow(img, cmap="gray")
    else:
        ax.imshow(img)

    ax.set_title(titulo)
    ax.axis("off")

plt.tight_layout()

# Salva a comparação final
plt.savefig(
    "resultados/comparacao_filtros.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Filtros Aplicados com Sucesso")
