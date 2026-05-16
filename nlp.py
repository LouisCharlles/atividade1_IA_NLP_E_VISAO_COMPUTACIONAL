import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

texto = "O processamento de linguagem natural é muito interessante e facilita a análise de dados."

tokens = word_tokenize(texto, language='portuguese')

stop_words = set(stopwords.words('portuguese'))
tokens_limpos = [palavra for palavra in tokens if palavra.lower() not in stop_words]

print("Texto Original:\n", texto, "\n")
print("1. Resultado da Tokenização:\n", tokens, "\n")
print("2. Resultado após Remoção de Stop-Words:\n", tokens_limpos)