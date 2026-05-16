# Atividade Prática: Inteligência Artificial (PLN e Visão Computacional)

Este repositório contém a implementação prática de técnicas essenciais de **Processamento de Linguagem Natural (PLN / NLP)** e **Visão Computacional (VC)** desenvolvidas como parte dos requisitos de avaliação da disciplina de Inteligência Artificial.

O objetivo do projeto é demonstrar a aplicação prática de conceitos teóricos abordados em aula através de scripts estruturados em Python, utilizando bibliotecas de referência na comunidade científica e de desenvolvimento.

---

## 🚀 Estrutura do Repositório

O projeto é composto pelos seguintes arquivos principais:

* **`nlp.py`**: Script focado no processamento inicial de fluxos de texto (Pipeline de pré-processamento).
* **`visao_computacional.py`**: Script de Visão Computacional focado na segmentação por limiarização e classificação baseada em proporções geométricas.
* **`requirements.txt`**: Arquivo de definição de dependências que lista todas as bibliotecas necessárias para a execução fiel dos scripts.
* **`imagem.png`**: Imagem de entrada utilizada como insumo para os algoritmos de visão computacional.

---

## 🔧 Pré-requisitos e Configuração do Ambiente (Virtualenv)

Para garantir o isolamento das dependências e evitar conflitos com pacotes globais do sistema, é altamente recomendável utilizar um ambiente virtual (`venv`). Siga as instruções abaixo de acordo com o seu sistema operacional para preparar o ambiente.

### 1. Clonar o Repositório
Navegue até a pasta de sua preferência e clone este repositório (ou acesse a pasta onde os arquivos estão localizados):
```bash
cd /home/luis/Documentos/atividade_iA
```

### 2. Criar o Ambiente Virtual (`venv`)
Execute o comando correspondente ao seu sistema para gerar a estrutura do ambiente isolado:
* **Linux / macOS**:
  ```bash
  python3 -m venv .venv
  ```
* **Windows (PowerShell)**:
  ```powershell
  python -m venv .venv
  ```

### 3. Ativar o Ambiente Virtual
Antes de instalar as bibliotecas, ative a `.venv`:
* **Linux / macOS**:
  ```bash
  source .venv/bin/activate
  ```
* **Windows (PowerShell)**:
  ```powershell
  .venv\Scripts\Activate.ps1
  ```
* **Windows (CMD tradicional)**:
  ```cmd
  .venv\Scripts\activate.bat
  ```
Quando ativado, o nome do ambiente virtual aparecerá no início da linha do terminal, ex: `(.venv) luis@luis-Nitro...`.

### 4. Instalar as Dependências (`requirements.txt`)
Com a `venv` ativa, utilize o gerenciador de pacotes `pip` para instalar todas as bibliotecas requeridas:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

*Nota: O conteúdo esperado do arquivo `requirements.txt` está detalhado ao final deste documento.*

---

## 📖 Explicação dos Módulos e Técnicas Utilizadas

### 1. Processamento de Linguagem Natural (`nlp.py`)

* **Propósito**: O objetivo deste script é realizar a limpeza e o tratamento inicial de uma string de texto em português, transformando dados textuais brutos em uma estrutura normalizada adequada para posterior mineração de dados ou análise de sentimentos.
* **Técnicas Utilizadas**:
    * **Tokenização (`word_tokenize`)**: Consiste na quebra de uma sequência fluida de texto em unidades estruturais mínimas chamadas *tokens* (palavras, pontuações, numerais). Essa etapa padroniza a entrada textual para processamento algorítmico sequencial.
    * **Remoção de Stop-Words**: Processo de filtragem que elimina palavras gramaticais funcionais recorrentes de altíssima frequência (como artigos, preposições, conjunções - ex: "o", "de", "e", "a") que não agregam valor semântico direto na identificação do tópico central ou na análise descritiva do texto.
* **Fluxo de Execução**:
    1. O script importa a biblioteca `nltk` e realiza o download sob demanda dos pacotes de dados linguísticos (`punkt`, `punkt_tab` e `stopwords`).
    2. A frase de teste em português é submetida ao tokenizador.
    3. Uma lista de stop-words nativa do idioma português é carregada e convertida em um conjunto (`set`) para otimizar a busca computacional.
    4. O script percorre os tokens gerados, remove termos irrelevantes usando normalização em caixa baixa (`.lower()`) e exibe o comparativo diretamente no terminal.


### 2. Visão Computacional: Segmentação e Detecção (`segmentacao.py`)

* **Propósito**: Este script implementa um pipeline completo de segmentação e reconhecimento visual de formas. Ele processa a imagem contendo armas de brinquedo (um machado e uma espada), isola as silhuetas do fundo e emprega uma métrica baseada em proporções geométricas para classificar e identificar individualmente cada objeto de forma automatizada.
* **Técnicas Utilizadas**:
    * **Conversão de Espaço de Cores (`BGR2RGB` / `BGR2GRAY`)**: O OpenCV carrega imagens nativamente no formato BGR. O script realiza a conversão para RGB (compatibilidade com a exibição do `matplotlib`) e para Tons de Cinza (Gray), reduzindo a dimensionalidade dos dados (de 3 canais de cor para apenas 1 canal de intensidade de brilho), facilitando análises baseadas em intensidade.
    * **Segmentação por Limiarização com Método de Otsu (`threshold`)**: Algoritmo matemático avançado que varre o histograma da imagem em tons de cinza para calcular automaticamente o valor ótimo de limiar (*threshold*). Ele maximiza a variância entre as classes de pixels (objeto vs. fundo). O modificador `THRESH_BINARY_INV` é aplicado para que os objetos (originalmente escuros) tornem-se brancos, e o fundo (originalmente claro) torne-se totalmente preto, gerando uma máscara binária nítida.
    * **Extração de Contornos (`findContours`)**: Algoritmo de busca topológica que rastreia as fronteiras contínuas de pixels brancos conectados dentro da máscara binária gerada no passo anterior.
    * **Filtragem por Área e Análise de Proporção (Bounding Box)**: 
        * Calcula a área interna de cada contorno (`contourArea`), descartando pequenas imperfeições que tenham área menor ou igual a 5000 pixels.
        * Para os contornos válidos, extrai as dimensões espaciais do retângulo delimitador (`boundingRect`): Posição (X, Y), Largura (W) e Altura (H).
        * Aplica uma regra geométrica condicional de classificação: como a **espada** possui um formato longilíneo marcante, a sua largura (W) é significativamente maior que o dobro de sua altura (H) no arranjo espacial fornecido (`w > h * 2`). Caso essa condição seja verdadeira, ela é rotulada como "Espada Identificada" (caixa verde); caso contrário, é classificada como "Machado" (caixa azul).
* **Fluxo de Execução**:
    1. Verifica a existência local do arquivo `imagem.png`.
    2. Lê, trata e aplica o fluxo sequencial de transformações (Cinza -> Blur -> Otsu).
    3. Localiza os contornos, avalia as métricas geométricas e renderiza as anotações visuais sobre a matriz da imagem original.
    4. Gera um painel comparativo tripartite (Imagem Original, Máscara de Otsu e Resultado Final Anotado) e salva o resultado fisicamente como um arquivo de imagem.

---

## 🖥️ Como Executar os Scripts

Certifique-se de que o ambiente virtual está ativo e execute os comandos abaixo diretamente no seu terminal:

### Executando o script de NLP:
```bash
python nlp.py
```
* **Resultado esperado**: Saída textual clara impressa no terminal discriminando a frase segmentada na sua totalidade e, em seguida, a listagem refinada contendo apenas as palavras-chave carregadas de significado.

### Executando o script de Visão Computacional (Segmentação):
```bash
python visao_computacional.py
```
* **Resultado esperado**: Exibição da confirmação de sucesso no console e a geração de um novo arquivo chamado **`resultado_segmentacao.png`** no mesmo diretório do projeto. Este arquivo contém a prova visual da segmentação pelo método de Otsu e as caixas envolventes indicando a detecção e classificação correta da espada e do machado.

---

## 📂 Arquivo `requirements.txt` Recomendado

Caso o seu diretório ainda não possua o arquivo `requirements.txt`, crie um arquivo com este nome exato e insira o conteúdo abaixo:

```text
nltk>=3.8.1
opencv-python>=4.8.0
matplotlib>=3.7.0
```

---
Este repositório cumpre integralmente os critérios metodológicos estabelecidos, demonstrando proficiência prática e estrutural na aplicação das ferramentas básicas de Inteligência Artificial.
