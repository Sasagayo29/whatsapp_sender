# app.py
import tkinter as tk
from tkinter import messagebox, filedialog
from sender import iniciar_driver, esperar_login, abrir_conversa, enviar
from utils import carregar_planilha, dividir_arquivos, log_sucesso, log_erro
import threading
import time


class WhatsAppApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WhatsApp Sender")
        self.root.geometry("600x400")
        self.driver = None

        self.frame_top = tk.Frame(root)
        self.frame_top.pack(fill="x", pady=10, padx=10)

        self.label_path = tk.Label(
            self.frame_top, text="Caminho do Excel:", anchor="w")
        self.label_path.pack(fill="x")
        self.excel_path_entry = tk.Entry(self.frame_top)
        self.excel_path_entry.pack(fill="x")
        self.btn_browse = tk.Button(
            self.frame_top, text="Procurar", command=self.browse_excel)
        self.btn_browse.pack(pady=5)

        self.btn_iniciar = tk.Button(
            root, text="Iniciar envio", command=self.iniciar_thread_envio)
        self.btn_iniciar.pack(pady=10)

        self.status = tk.Label(root, text="Pronto para começar.", anchor="w")
        self.status.pack(fill="x", pady=10, padx=10)

        self.log_area = tk.Text(root, height=15, state="disabled")
        self.log_area.pack(fill="both", expand=True, padx=10, pady=10)

    def browse_excel(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel files", "*.xlsx")]
        )
        if file_path:
            self.excel_path_entry.delete(0, tk.END)
            self.excel_path_entry.insert(0, file_path)

    def log(self, texto):
        print(texto)
        self.status.config(text=texto)
        self.log_area.config(state="normal")
        self.log_area.insert(tk.END, texto + "\n")
        self.log_area.config(state="disabled")
        self.log_area.see(tk.END)
        self.root.update()

    def iniciar_thread_envio(self):
        thread = threading.Thread(target=self.executar_envio)
        thread.start()

    def executar_envio(self):
        excel_path = self.excel_path_entry.get()
        if not excel_path:
            messagebox.showerror(
                "Erro", "Por favor, selecione um arquivo Excel.")
            return

        try:
            df = carregar_planilha(excel_path)
        except Exception as e:
            messagebox.showerror("Erro", str(e))
            self.log_area.delete("1.0", tk.END)
            return

        self.driver = iniciar_driver()
        self.log("Aguardando login...")

        try:
            esperar_login(self.driver)
        except Exception as e:
            messagebox.showerror(
                "Erro", f"Login falhou. Verifique sua conexão ou se a sessão do Chrome está corrompida. Erro: {e}")
            self.driver.quit()
            return

        self.log("Login realizado com sucesso. Iniciando envios.")

        for i, row in df.iterrows():
            tipo = str(row['tipo']).lower()
            destino = str(row['destino'])
            mensagem = str(row.get('mensagem', ''))
            arquivos = dividir_arquivos(str(row.get('arquivos', '')))

            try:
                self.log(f"Enviando para {tipo}: {destino}")
                abrir_conversa(self.driver, tipo, destino)
                enviar(self.driver, mensagem, arquivos)
                log_sucesso(row.to_dict())
                self.log(f"Mensagem enviada com sucesso para {destino}.")

            except Exception as e:
                log_erro(row.to_dict(), str(e))
                self.log(f"Erro ao enviar para {destino}: {e}")
                self.log("Tentando continuar com os próximos envios...")

        if self.driver:
            self.driver.quit()
            self.log("Envios finalizados.")
            messagebox.showinfo(
                "Finalizado", "Todos os envios foram processados.")


if __name__ == "__main__":
    root = tk.Tk()
    app = WhatsAppApp(root)
    root.mainloop()
