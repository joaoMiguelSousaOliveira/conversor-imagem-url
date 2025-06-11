from bs4 import BeautifulSoup

def extrair_src(caminho_html, caminho_arquivo_saida):

    with open(caminho_html, 'r', encoding='utf-8') as f:
        conteudo_html = f.read()

    dados_pagina = BeautifulSoup(conteudo_html, 'html.parser')

    caminhos_src = []

    for img_tag in dados_pagina.find_all('img'):
        src = img_tag.get('src')
        if src:
            caminhos_src.append(src)

    with open(caminho_arquivo_saida, 'w', encoding='utf-8') as f_out:
        for caminho in caminhos_src:
            f_out.write(caminho + '\n')

    print(f"Sucesso. Número de caminhos src {len(caminhos_src)}")

if __name__ == "__main__":

    pagina = 'C:/Users/Mapia/Desktop/Esteiras - Notion/Esteiras.html'            
    caminho_saida = 'C:/Users/Mapia/Desktop/Automação - HTML/arquivo_saida.txt'

    extrair_src(pagina, caminho_saida)



