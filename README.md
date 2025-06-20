# Conversor Imagem - URL
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Projeto voltado para extraçaõ e conversão de imagens em **`URL`** com injeção **`html`**. Este projeto simples surgiu apartir da necessidade de injetar um arquivo html oriundo do notion na plataforma OneDrive

## Tecnologias
* **`beatifulSoup`** 
* **`API Cloudinary`**

## Arquivos
* `Esteiras.html`: Arquivo HTML original que contém as imagens que iremos converter em URLs.
* `extrair_imagens.py`: Script Python para a lógica de extração de imagens do arquivo `Esteiras.html` e criação e armazenamento do caminho das imagens em `forma_arquivo_saida.py`.
* `imagens_url.py`: Script Python central para geração de URLs a partir das imagens armazenadas em `forma_arquivo_saida.py` e armaena as urls geradas em `arquivo_urls.txt`.
* `altera_html.py`: Recebe as urls armazenadas em `forma_arquivo_saida.py` e armaena as urls geradas em `arquivo_urls.txt`.
