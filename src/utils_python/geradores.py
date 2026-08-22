from random import randint


def gerar_cpf() -> str:
    """
    Gera um CPF (Cadastro de Pessoas Físicas) válido.

    :return: CPF gerado no padrão 'XXX.XXX.XXX-XX'.
    
    """

    def calcular_digito(cpf: str) -> int:
        soma = sum(int(digito) * peso for digito, peso in zip(cpf, range(len(cpf) + 1, 1, -1)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    cpf = ''.join(str(randint(0, 9)) for _ in range(9))
    cpf += str(calcular_digito(cpf))
    cpf += str(calcular_digito(cpf))

    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def gerar_cnpj() -> str:
    """
    Gera um CNPJ (Cadastro Nacional da Pessoa Jurídica) válido.

    :return: CNPJ gerado no padrão 'XX.XXX.XXX/0001-XX'.
    
    """

    def calcular_digito(cnpj: str) -> int:
        pesos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        soma = sum(int(digito) * peso for digito, peso in zip(cnpj, pesos))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    cnpj = ''.join(str(randint(0, 9)) for _ in range(12))
    cnpj += str(calcular_digito(cnpj))
    cnpj += str(calcular_digito(cnpj))

    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/0001-{cnpj[12:]}"

def gerar_telefone() -> str:
    """
    Gera um número de telefone válido no Brasil.

    :return: Telefone gerado no padrão '(XX) XXXXX-XXXX'.

    """

    ddd = randint(11, 99)
    numero = f"{randint(90000, 99999)}-{randint(1000, 9999)}"
    return f"({ddd}) {numero}"

def gerar_nome() -> str:
    """
    Gera um nome completo aleatório. Padrão 'Pessoa __numero__ Sobrenome __numero__'.

    :return: Nome completo gerado.

    """

    numero_nome = randint(1, 100)
    numero_sobrenome = randint(1, 100)

    nome = f"Pessoa {numero_nome} Sobrenome {numero_sobrenome}"
    return nome

def gerar_razao_social() -> str:
    """
    Gera uma razão social aleatória. Padrão 'Comércio/Industria/Serviço __numero__ MEI/ME/EPP/SA'.

    :return: Razão social gerada.

    """

    tipos = ['Comércio', 'Industria', 'Serviço']
    categorias = ['MEI', 'ME', 'EPP', 'SA']
    
    return f"{tipos[randint(0, len(tipos) - 1)]} {randint(1, 100)} {categorias[randint(0, len(categorias) - 1)]}"
