import json

from utils_python.arquivos import gravar_json


def test_gravar_dicionario(tmp_path):
    
    dados = {
        "nome": "João",
        "idade": 30
    }

    caminho_arquivo = tmp_path / "dados.json"

    resultado = gravar_json(dados, str(caminho_arquivo))

    assert resultado is True
    assert caminho_arquivo.exists()

    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        dados_gravados = json.load(arquivo)

    assert dados_gravados == dados