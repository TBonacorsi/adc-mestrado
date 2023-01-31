import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import sys
import os
os.chdir(sys.path[0])

# read text
text = open('Programas_de_curso_Total.txt', mode='r', encoding='utf-8').read()
stopwords = STOPWORDS

wc = WordCloud(
    background_color=None,
    stopwords=stopwords,
    height=600,
    width=400,
    max_words=80
)

wc.generate(text)

# store to file
wc.to_file('wordcloud_Geral.png')
