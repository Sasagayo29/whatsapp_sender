# 📲 WhatsApp Sender - Automação de Mensagens e Arquivos

Projeto de automação em **Python** para envio em massa de mensagens e arquivos via **WhatsApp Web**, utilizando a biblioteca **Selenium**. Conta com uma **interface gráfica (Tkinter)** e um sistema robusto de **logs**.

---

## 🚀 Funcionalidades

- **Envio de Mensagens e Mídia:** Suporte a texto, imagens, documentos e áudios.
- **Leitura de Planilha Excel:** Importa contatos e mensagens de um arquivo `.xlsx`.
- **Sessão Persistente:** Mantém o login ativo no WhatsApp Web (sem necessidade de novo QR code).
- **Interface Gráfica:** UI simples para controle do processo.
- **Sistema de Logs:** Registro detalhado de envios bem-sucedidos e falhas.

---

## 📦 Estrutura do Projeto
````bash
whatsapp_sender/
│
├── app.py                  # Código principal e interface gráfica
├── config.py               # Arquivo com todas as configurações globais
├── sender.py               # Lógica de automação de envio com Selenium
├── utils.py                # Funções utilitárias (validação, logs, etc.)
├── arquivos/
│   ├── contatos.xlsx       # Planilha de entrada
│   └── imagens, pdfs       # (Subpastas opcionais para seus arquivos)
└── logs/
    ├── envio_sucesso.csv   # Logs de envios bem-sucedidos
    └── erros_envio.csv     # Logs de envios que falharam
````

---

## ⚙️ Instalação e Configuração

### ✅ Pré-requisitos

- Python **3.6+**
- Google Chrome instalado

### 📥 Instalação das Dependências

No terminal, dentro da pasta do projeto, execute:

```bash
pip install -r requirements.txt
selenium
pandas
openpyxl
