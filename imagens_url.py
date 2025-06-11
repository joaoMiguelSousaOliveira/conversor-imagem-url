from dotenv import load_dotenv
load_dotenv()

import cloudinary
import cloudinary.uploader

import os

cloudinary.config(
    cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key = os.getenv('CLOUDINARY_API_KEY'),
    api_secret = os.getenv('CLOUDINARY_API_SECRET'),
    secure = True
)

def upload_imagens(imagem_entrada):
    response = cloudinary.uploader.upload(imagem_entrada)
    return response['secure_url']

def processar_imagens_ordem(arquivo_ordenado, diretorio_imagens, arquivo_urls):
    
    urls_geradas = []
    imagens_processadas = 0

    with open(arquivo_ordenado, 'r', encoding='utf-8') as f_ordem:
        nomes_imagens = [linha.strip() for linha in f_ordem if linha.strip()]
    
    for nome_img in nomes_imagens:
        caminho_completo_imagem = os.path.join(diretorio_imagens, nome_img)
        url = upload_imagens(caminho_completo_imagem)
        if url:
            urls_geradas.append(url)
            imagens_processadas += 1

    with open(arquivo_urls, 'w', encoding='utf-8') as f_saida:
        for url in urls_geradas:
            f_saida.write(url + '\n')

    print(f"Total de imagens processadas {imagens_processadas}")


if __name__ == "__main__":
    ordenado = "C:/Users/Mapia/Desktop/Automação - HTML/arquivo_saida_corrigos.txt"
    imagens_diretorio = "C:/Users/Mapia/Desktop/Esteiras - Notion"
    arquivo_com_urls = "C:/Users/Mapia/Desktop/Automação - HTML/arquivo_urls.txt"

    processar_imagens_ordem(ordenado, imagens_diretorio, arquivo_com_urls)