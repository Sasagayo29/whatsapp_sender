# sender.py
import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import quote
from config import CHROME_PROFILE_PATH, TEMPO_ESPERA, DELAY_ENVIO, PAIS_DDI
from utils import validar_numero


def iniciar_driver():
    """Inicia o WebDriver do Chrome com perfil de usuário para manter a sessão."""
    options = Options()
    options.add_argument(f"user-data-dir={CHROME_PROFILE_PATH}")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # Desabilita notificações
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.get("https://web.whatsapp.com")
    return driver


def esperar_login(driver):
    """Espera o usuário fazer o login escaneando o QR code."""
    WebDriverWait(driver, TEMPO_ESPERA * 2).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div[role='textbox'], input[type='text']"))
    )


def abrir_conversa(driver, tipo, destino):
    """Abre uma conversa com um contato ou grupo."""
    wait = WebDriverWait(driver, TEMPO_ESPERA)

    if tipo == "contato":
        numero = validar_numero(destino)
        if not numero:
            raise ValueError(
                "Número de telefone inválido ou formato incorreto.")

        url = f"https://web.whatsapp.com/send?phone={PAIS_DDI}{numero}"
        driver.get(url)

        try:
            # Espera até que o campo de mensagem esteja visível para confirmar que a conversa foi aberta
            wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[role='textbox']")))
        except Exception:
            raise Exception(
                "Não foi possível abrir a conversa com o contato. O número pode não ter WhatsApp.")

    elif tipo == "grupo":
        # Tentativa de busca por nome de grupo
        try:
            campo_busca = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[contenteditable='true'][data-tab='3']")))
            campo_busca.send_keys(destino)
            # Pequena pausa para os resultados da busca aparecerem
            time.sleep(2)

            # Encontra o grupo na lista de resultados
            grupo = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, f"span[title='{destino}']")))
            grupo.click()
            time.sleep(DELAY_ENVIO)

        except Exception:
            raise Exception(
                "Não foi possível encontrar ou abrir a conversa com o grupo.")
    else:
        raise ValueError("Tipo de destino inválido. Use 'contato' ou 'grupo'.")


def enviar(driver, mensagem, arquivos):
    """Envia uma mensagem de texto e/ou arquivos."""
    wait = WebDriverWait(driver, TEMPO_ESPERA)

    if mensagem:
        try:
            campo_mensagem = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR,
                 "div[contenteditable='true'][role='textbox']")
            ))
            campo_mensagem.send_keys(mensagem)
        except Exception:
            raise Exception("Não foi possível encontrar o campo de mensagem.")

    if arquivos:
        try:
            clip_btn = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div[title='Anexar']")
            ))
            clip_btn.click()

            # O input do arquivo é sempre do tipo 'file'
            input_file = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[type='file']")
            ))

            for arquivo in arquivos:
                full_path = os.path.abspath(arquivo)
                input_file.send_keys(full_path)
                time.sleep(2)  # Espera o upload do arquivo

            # Espera o botão de enviar aparecer após o upload
            botao_enviar = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "span[data-icon='send']")
            ))
            botao_enviar.click()

        except Exception:
            raise Exception("Não foi possível anexar ou enviar o arquivo.")

    else:
        # Se não houver arquivo, envia apenas a mensagem de texto
        try:
            botao_enviar = wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "span[data-icon='send']")
            ))
            botao_enviar.click()
        except Exception:
            raise Exception(
                "Não foi possível encontrar o botão de envio para a mensagem.")

    time.sleep(DELAY_ENVIO)
