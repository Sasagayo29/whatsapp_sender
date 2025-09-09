import pandas as pd

# Dados fornecidos
data = [
    {
        "tipo": "contato",
        "destino": "9876543210",
        "mensagem": "Olá, esta é uma mensagem de teste.",
        "arquivos": ""
    },
    {
        "tipo": "contato",
        "destino": "9987654321",
        "mensagem": "Esta mensagem tem um arquivo.",
        "arquivos": "arquivos/imagem_teste.jpg"
    },
    {
        "tipo": "grupo",
        "destino": "Grupo de Teste",
        "mensagem": "Enviando um arquivo para o grupo.",
        "arquivos": "arquivos/documento_teste.pdf"
    },
    {
        "tipo": "contato",
        "destino": "9123456789",
        "mensagem": "Mensagem com dois arquivos.",
        "arquivos": "arquivos/audio_teste.mp3;arquivos/documento2.pdf"
    }
]

# Criar DataFrame
df = pd.DataFrame(data)

# Salvar como arquivo Excel
df.to_excel("mensagens_planilha.xlsx", index=False)
