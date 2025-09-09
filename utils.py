# utils.py
import os
import re
import pandas as pd
from config import EXCEL_PATH, COLUNAS_OBRIGATORIAS, SEPARADOR_ARQUIVOS, LOG_SUCESSO, LOG_ERROS


def validar_numero(numero):
    """Valida e limpa número de telefone"""
    numero = re.sub(r'\D', '', str(numero))
    return numero if len(numero) in [10, 11] else None


def carregar_planilha(path):
    """Carrega o Excel e valida colunas"""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Arquivo {path} não encontrado.")

    df = pd.read_excel(path).fillna('')
    for coluna in COLUNAS_OBRIGATORIAS:
        if coluna not in df.columns:
            raise ValueError(
                f"Coluna obrigatória '{coluna}' não está presente.")
    return df


def log_sucesso(linha):
    salvar_log(linha, LOG_SUCESSO)


def log_erro(linha, erro):
    linha["erro"] = str(erro)
    salvar_log(linha, LOG_ERROS)


def salvar_log(dados, caminho):
    df = pd.DataFrame([dados])
    header = not os.path.exists(caminho)
    df.to_csv(caminho, mode="a", index=False, header=header)


def dividir_arquivos(caminho_str):
    if not isinstance(caminho_str, str) or not caminho_str.strip():
        return []

    caminhos = [c.strip() for c in caminho_str.split(SEPARADOR_ARQUIVOS)]
    return [c for c in caminhos if os.path.exists(c)]
