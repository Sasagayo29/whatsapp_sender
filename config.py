# config.py
import os

# 1. Configurações do Selenium e Chrome
# Caminho para o seu perfil do Chrome. É aqui que o login será salvo.
# ATENÇÃO: SUBSTITUA 'SEU_NOME_DE_USUÁRIO' pelo seu nome de usuário do Windows.
# Para encontrar o caminho correto, siga estas etapas:
# - Abra o Chrome
# - Na barra de endereços, digite 'chrome://version' e pressione Enter.
# - O caminho para o 'Profile Path' é o que você precisa. Exclua a última pasta 'Default' ou 'Profile 1' e use o restante do caminho.
CHROME_PROFILE_PATH = f"C:\\Users\\SEU_NOME_DE_USUÁRIO\\AppData\\Local\\Google\\Chrome\\User Data"

# Tempo máximo de espera (em segundos) para os elementos carregarem.
TEMPO_ESPERA = 60

# Tempo de espera (em segundos) entre cada envio para evitar sobrecarga.
DELAY_ENVIO = 2

# 2. Configurações da Planilha e Arquivos
# Nome e caminho da planilha Excel com os contatos e mensagens.
# Este caminho é relativo à pasta principal do seu projeto.
EXCEL_PATH = "arquivos/contatos.xlsx"

# Colunas obrigatórias na sua planilha Excel.
# Você pode adicionar mais colunas se precisar de mais dados.
COLUNAS_OBRIGATORIAS = ["tipo", "destino", "mensagem", "arquivos"]

# Separador para múltiplos arquivos na coluna 'arquivos'.
# Por exemplo, "arquivos/imagem1.jpg;arquivos/documento.pdf"
SEPARADOR_ARQUIVOS = ";"

# 3. Configurações de Localização
# Código DDI do país para o envio de mensagens (ex: Brasil = 55).
PAIS_DDI = "55"

# 4. Configurações de Log
# Caminhos para os arquivos de log de sucesso e erro.
# Eles serão criados automaticamente se não existirem.
LOG_SUCESSO = "logs/envio_sucesso.csv"
LOG_ERROS = "logs/erros_envio.csv"
