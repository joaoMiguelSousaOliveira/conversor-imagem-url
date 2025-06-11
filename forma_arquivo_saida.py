def corrigir_nomes(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, 'r', encoding='utf-8') as f_in:
        with open(arquivo_saida, 'w', encoding='utf-8') as f_out:
            for linha in f_in:
                linha_corrigida = linha.replace('%20', ' ')
                f_out.write(linha_corrigida)
    print(f"Nomes corrigidos em {arquivo_saida}")

if __name__ == "__main__":
    entrada = 'C:/Users/Mapia/Desktop/Automação - HTML/arquivo_saida.txt'
    saida = 'C:/Users/Mapia/Desktop/Automação - HTML/arquivo_saida_corrigos.txt'

    corrigir_nomes(entrada, saida)