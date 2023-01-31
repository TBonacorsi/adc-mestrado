import matplotlib.pyplot as plt
from collections import Counter
with open('Programas_de_curso_Total.txt') as file:
    texto = file.read().lower()

texto_sem_pontuacao = ' '
for c in texto:
    if c.isalpha() or c == ' ':
        texto_sem_pontuacao += c

palavras = texto_sem_pontuacao.split()

frequencia_palavras = {}
for palavra in palavras:
    if palavra not in frequencia_palavras:
        frequencia_palavras[palavra] = 0

    frequencia_palavras[palavra] += 1

frequencia_palavras = Counter(palavras)

plt.figure(figsize=(12, 18))
rotulos, valores = zip(*frequencia_palavras.most_common(15))
plt.title('Frequência de palavras nos programas de curso', fontsize=10)
plt.plot(rotulos, valores, "--", marker='d', color='g', linewidth=0.7)
plt.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=200,
                    hspace=0.4)
plt.legend(['frequência'], fontsize=10)
plt.savefig('FQWPrograma_Geral.png')
