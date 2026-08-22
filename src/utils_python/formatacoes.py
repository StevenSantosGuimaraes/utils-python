def formatar_monetario(valor: float) -> str:
    """
    Formata um valor monetário no padrão brasileiro.

    :param valor: Valor a ser formatado.
    
    :return: Valor formatado no padrão 'R$ 1.000,00'.
    
    """

    return f"R$ {valor:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")

def formatar_cpf(cpf: str) -> str:
    """
    Formata um CPF (Cadastro de Pessoas Físicas) no padrão brasileiro.

    :param cpf: CPF a ser formatado, que pode conter apenas números ou já estar parcialmente formatado.
    
    :return: CPF formatado no padrão 'XXX.XXX.XXX-XX'.

    """

    cpf = ''.join(filter(str.isdigit, cpf))  # Remove qualquer caractere que não seja dígito
    if len(cpf) != 11:
        raise ValueError("CPF deve conter exatamente 11 dígitos.")
    
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

def formatar_cnpj(cnpj: str) -> str:
    """
    Formata um CNPJ (Cadastro Nacional da Pessoa Jurídica) no padrão brasileiro.

    :param cnpj: CNPJ a ser formatado, que pode conter apenas números ou já estar parcialmente formatado.
    
    :return: CNPJ formatado no padrão 'XX.XXX.XXX/XXXX-XX'.
    
    """

    cnpj = ''.join(filter(str.isdigit, cnpj))  # Remove qualquer caractere que não seja dígito
    if len(cnpj) != 14:
        raise ValueError("CNPJ deve conter exatamente 14 dígitos.")
    
    return f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"

def formatar_telefone(telefone: str) -> str:
    """
    Formata um número de telefone no padrão brasileiro.

    :param telefone: Número de telefone a ser formatado, que pode conter apenas números ou já estar parcialmente formatado.
    
    :return: Telefone formatado no padrão '(XX) XXXXX-XXXX' ou '(XX) XXXX-XXXX'.
    
    """

    telefone = ''.join(filter(str.isdigit, telefone))  # Remove qualquer caractere que não seja dígito
    if len(telefone) == 10:
        return f"({telefone[:2]}) {telefone[2:6]}-{telefone[6:]}"
    elif len(telefone) == 11:
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    else:
        raise ValueError("Telefone deve conter 10 ou 11 dígitos.")
