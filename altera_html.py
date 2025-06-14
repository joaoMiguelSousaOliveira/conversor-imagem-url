from bs4 import BeautifulSoup

def html_corrigido(caminho_html, caminho_urls, caminho_arquivo_saida):
    
    with open(caminho_html, 'r', encoding='utf-8') as f:
        conteudo_html = f.read()
    
    dados = BeautifulSoup(conteudo_html, 'html.parser')

    with open(caminho_urls, 'r', encoding='utf-8') as f:
        conteudo_urls = [line.strip() for line in f if line.strip()]
    
    images = dados.find_all('img')

    numero_img = len(images)
    numero_urls = len(conteudo_urls)

    if numero_urls < numero_img:
        print(f"Existe {numero_img} imagens no HTML, mas apenas {numero_urls} urls")

    for i, img_tag in enumerate(images):
        if i < numero_urls:
            img_tag['src'] = conteudo_urls[i]
        else:
            print(f"Não há mais urls disponíveis para substituir a imagem {img_tag.prettify()}")
            break
    
    with open(caminho_arquivo_saida, 'w', encoding='utf-8') as f:
        f.write(str(dados))
    
if __name__ == "__main__":
    arquivo_html = 'Esteiras.html'
    arquivo_urls = 'arquivo_urls.txt'
    arquivo_saida = 'Esteiras_corrigido.html'

    html_corrigido(arquivo_html, arquivo_urls, arquivo_saida)