# whatsapp_sender

WhatsApp Sender - Automação de Mensagens e Arquivos
Este é um projeto de automação em Python para enviar mensagens e arquivos em massa através do WhatsApp Web, usando a biblioteca Selenium. O projeto é modular, com uma interface gráfica simples (Tkinter) e um sistema robusto de logs.

🚀 Funcionalidades
Envio de Mensagens e Mídia: Envia mensagens de texto, imagens, documentos, e áudios.

Leitura de Planilha Excel: Utiliza um arquivo Excel para carregar os dados de destino (números de telefone ou nomes de grupos) e o conteúdo a ser enviado.

Sessão Persistente: Mantém o login no WhatsApp Web para evitar a necessidade de escanear o QR code em todas as execuções.

Interface Gráfica: Uma interface simples para iniciar o processo e acompanhar o status dos envios.

Sistema de Logs: Cria arquivos de log para registrar envios com sucesso e erros.

📦 Estrutura do Projeto
A arquitetura do projeto é dividida em módulos para facilitar a manutenção e o desenvolvimento:

whatsapp_sender/
│
├── app.py # Código principal e interface gráfica
├── config.py # Arquivo com todas as configurações globais
├── sender.py # Lógica de automação de envio com Selenium
├── utils.py # Funções utilitárias (validação, logs, etc.)
├── arquivos/
│ ├── contatos.xlsx # Planilha de entrada
│ └── imagens, pdfs # (Subpastas opcionais para seus arquivos)
└── logs/
├── envio_sucesso.csv # Logs de envios bem-sucedidos
└── erros_envio.csv # Logs de envios que falharam

⚙️ Instalação e Configuração
Pré-requisitos
Python 3.6 ou superior

Navegador Google Chrome instalado

Instalação das dependências
Abra o terminal na pasta do projeto e execute o seguinte comando:

pip install -r requirements.txt

Nota: Você precisará criar o arquivo requirements.txt com as dependências do projeto. O conteúdo é:

selenium
pandas
openpyxl

Você pode criar este arquivo e salvar na pasta do projeto.

Configuração
Ajuste o config.py:

Abra o arquivo config.py.

Altere a variável CHROME_PROFILE_PATH para o caminho do seu perfil de usuário do Chrome.

Prepare a Planilha de Entrada:

Abra o arquivo arquivos/contatos.xlsx ou crie um novo com o mesmo nome e as colunas obrigatórias: tipo, destino, mensagem e arquivos.

▶️ Como Usar
Execute o Aplicativo:
Abra o terminal na pasta do projeto e execute:

python app.py

Login no WhatsApp Web:
Na primeira execução, uma janela do Chrome será aberta. Escaneie o QR code para fazer o login. A sessão será salva para as próximas execuções.

Iniciar o Envio:
Na interface gráfica, clique no botão "Iniciar envio". O aplicativo processará a planilha e começará a enviar as mensagens e arquivos.

⚠️ Solução de Problemas
ModuleNotFoundError: Este erro indica que as dependências não estão instaladas. Certifique-se de executar pip install -r requirements.txt no ambiente correto.

Login Falhou: Verifique se você escaneou o QR code corretamente.

ElementNotFoundException: Se o script não encontrar um elemento na página, isso pode ser causado por uma atualização do WhatsApp Web. Tente inspecionar a página e ajustar os seletores no arquivo sender.py.
