# Conversor Imagem - URL

# Este projeto consiste em um vonjunto de scripts Python que convertem imagens para URLs e realiza a injeção das URLs geradas em um arquivo .html.

## Tecnologias
Foram utilizadas bibliotecas como
* beatifulSoup para extração do caminho das imagens no html original e inserção no html alterado
* API Cloudinary

## Arquivos
* `Esteiras.html`: Arquivo HTML original que contém as imagens que iremos converter em URLs.
* `extrair_imagens.py`: Script Python para a lógica de extração de imagens do arquivo `Esteiras.html` e criação e armazenamento do caminho das imagens em `forma_arquivo_saida.py`.
* `imagens_url.py`: Script Python central para geração de URLs a partir das imagens armazenadas em `forma_arquivo_saida.py` e armaena as urls geradas em `arquivo_urls.txt`.
* `altera_html.py`: Recebe as urls armazenadas em `forma_arquivo_saida.py` e armaena as urls geradas em `arquivo_urls.txt`.
