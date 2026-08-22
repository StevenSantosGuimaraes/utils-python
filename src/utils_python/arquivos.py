import json, os

import pandas as pd

from .diretorios import criar_diretorio_se_nao_existir


def gravar_json(dados: list[dict] | dict, caminho_arquivo: str) -> bool:
    """
    Grava os dados em um arquivo JSON.

    :param dados: Dados a serem gravados no arquivo JSON, pode ser uma lista de dicionários ou um dicionário.
    :param caminho_arquivo: Caminho do arquivo onde os dados serão gravados, confirmando se o diretório existe.
    
    :return: True se o arquivo foi gravado com sucesso, False caso contrário.
    """

    criar_diretorio_se_nao_existir(os.path.dirname(caminho_arquivo))

    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

    return True

def ler_json(caminho_arquivo: str) -> list[dict] | dict:
    """
    Lê os dados de um arquivo JSON.

    :param caminho_arquivo: Caminho do arquivo JSON a ser lido.
    
    :return: Dados lidos do arquivo JSON, que podem ser uma lista de dicionários ou um dicionário.
    """

    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)

    return dados

def listar_arquivos(diretorio: str, extensao: str) -> list[str]:
    """
    Lista todos os arquivos com a extensão especificada em um diretório.

    :param diretorio: Caminho do diretório onde os arquivos serão listados.
    :param extensao: Extensão dos arquivos a serem listados (ex: '.pdf').
    
    :return: Lista de caminhos completos dos arquivos encontrados.
    """

    if not os.path.exists(diretorio):
        raise FileNotFoundError(f"O diretório {diretorio} não existe.")

    arquivos_encontrados = [
        os.path.join(diretorio, arquivo)
        for arquivo in os.listdir(diretorio)
        if arquivo.lower().endswith(extensao.lower()) and os.path.isfile(os.path.join(diretorio, arquivo))
    ]

    return arquivos_encontrados

def gravar_xlsx(dados: list[dict], cabecalho: list[str], caminho_arquivo: str) -> bool:
    """
    Grava os dados em um arquivo Excel (.xlsx).

    :param dados: Lista de dicionários a serem gravados no arquivo Excel.
    :param caminho_arquivo: Caminho do arquivo onde os dados serão gravados, confirmando se o diretório existe.
    
    :return: True se o arquivo foi gravado com sucesso, False caso contrário.
    """

    criar_diretorio_se_nao_existir(os.path.dirname(caminho_arquivo))

    df = pd.DataFrame(dados)
    if cabecalho:
        df = df[cabecalho]
    df.to_excel(caminho_arquivo, index=False)

    return True

def ler_xlsx(caminho_arquivo: str) -> pd.DataFrame:
    """
    Lê os dados de um arquivo Excel (.xlsx).

    :param caminho_arquivo: Caminho do arquivo Excel a ser lido.
    
    :return: DataFrame contendo os dados lidos do arquivo Excel.
    """

    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"O arquivo {caminho_arquivo} não existe.")

    df = pd.read_excel(caminho_arquivo)

    return df
