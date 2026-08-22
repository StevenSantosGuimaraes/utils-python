import os


def criar_diretorio_se_nao_existir(diretorio: str) -> None:
    """
    Cria o diretório especificado se ele não existir.

    :param diretorio: Caminho do diretório a ser criado.

    """

    if not os.path.exists(diretorio):
        os.makedirs(diretorio, exist_ok=True)
        print(f'Diretório {diretorio} criado.')
