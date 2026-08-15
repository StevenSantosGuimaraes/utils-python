import json, os


def gravar_json(dados: list[dict] | dict, caminho_arquivo: str) -> bool:
    """
    Grava os dados em um arquivo JSON.

    :param dados: Dados a serem gravados no arquivo JSON, pode ser uma lista de dicionários ou um dicionário.
    :param caminho_arquivo: Caminho do arquivo onde os dados serão gravados, confirmando se o diretório existe.
    
    :return: True se o arquivo foi gravado com sucesso, False caso contrário.
    """

    # Se o diretório não existir, cria o diretório e imprime uma mensagem informando que o diretório foi criado
    if not os.path.exists(os.path.dirname(caminho_arquivo)):
        os.makedirs(os.path.dirname(caminho_arquivo), exist_ok=True)
        print(f'Diretório {os.path.dirname(caminho_arquivo)} criado.')

    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    return True
