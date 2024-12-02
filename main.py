import tkinter as tk
from PIL import Image, ImageTk
from modulo_dragao import caca_ao_dragao


class DragonHunterApp:
    def __init__(self, root):
        self.root = root
        self.configurar_janela()
        self.carregar_widgets()
        self.campos_visiveis = False

    def configurar_janela(self):
        self.root.title("Caça ao Dragão! 🐉")
        largura_janela = 819
        altura_janela = 819
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        x_central = int((largura_tela - largura_janela) / 2)
        y_central = int((altura_janela - largura_janela) / 2)
        self.root.geometry(f"{largura_janela}x{largura_janela}+{x_central}+{y_central}")
        self.root.resizable(False, False)

        # Adicionando o background
        self.background_image = ImageTk.PhotoImage(Image.open("assets/background.png"))
        self.background_label = tk.Label(self.root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

    def carregar_widgets(self):
        # Botão principal
        self.botao_imagem = ImageTk.PhotoImage(Image.open("assets/hunt_button.png").resize((50, 50)))
        self.botao_cacar = tk.Button(
            self.root,
            image=self.botao_imagem,
            command=self.mostrar_campos,
            bg="#2b2b2b",
            bd=0,
            activebackground="#1E1E1E",
        )
        # Posicionar o botão no canto inferior direito
        self.botao_cacar.place(relx=0.95, rely=0.95, anchor="se")

    def mostrar_campos(self):
        if not self.campos_visiveis:
            # Campo para inserir poderes dos dragões
            self.dragao_label = tk.Label(
                self.root,
                text="Poder dos Dragões (separados por vírgula):",
                bg="#2b2b2b",
                fg="#FFD700",
                font=("Helvetica", 12),
            )
            self.dragao_label.place(relx=0.1, rely=0.2, anchor="w")

            self.dragao_entry = tk.Entry(
                self.root, font=("Helvetica", 12), width=50, bg="#1E1E1E", fg="#FFD700", insertbackground="#FFD700"
            )
            self.dragao_entry.place(relx=0.1, rely=0.25, anchor="w")

            # Campo para inserir o poder mágico
            self.poder_label = tk.Label(
                self.root,
                text="Seu Poder Mágico:",
                bg="#2b2b2b",
                fg="#FFD700",
                font=("Helvetica", 12),
            )
            self.poder_label.place(relx=0.1, rely=0.35, anchor="w")

            self.poder_entry = tk.Entry(
                self.root, font=("Helvetica", 12), width=15, bg="#1E1E1E", fg="#FFD700", insertbackground="#FFD700"
            )
            self.poder_entry.place(relx=0.1, rely=0.4, anchor="w")

            # Botão para iniciar a análise
            self.botao_analisar = tk.Button(
                self.root,
                text="Capturar Dragões 🐉🐉🐉",
                command=self.iniciar_caca,
                bg="#FFD700",
                fg="#2b2b2b",
                font=("Helvetica", 12, "bold"),
            )
            self.botao_analisar.place(relx=0.1, rely=0.5, anchor="w")

            self.campos_visiveis = True

    def resetar_campos(self):
        # Esconde todos os inputs e labels
        if hasattr(self, "dragao_entry"):
            self.dragao_entry.place_forget()
            self.poder_entry.place_forget()
            self.botao_analisar.place_forget()
            self.dragao_label.place_forget()
            self.poder_label.place_forget()
            self.campos_visiveis = False

    def iniciar_caca(self):
        # Obter os valores inseridos pelo usuário
        try:
            poderes_dragao = list(map(int, self.dragao_entry.get().split(",")))
            poder_magico = int(self.poder_entry.get())
        except ValueError:
            self.exibir_erro("Por favor, insira valores válidos!")
            return

        # Usar a função do módulo para determinar os dragões capturáveis
        indices_capturados = caca_ao_dragao(poderes_dragao, poder_magico)

        # Exibir resultados
        self.exibir_saida(poderes_dragao, poder_magico, indices_capturados)

    def exibir_saida(self, poderes_dragao, poder_magico, indices_capturados):
        # Criar a área de saída se ainda não existir
        if hasattr(self, "output_frame"):
            self.output_frame.destroy()  # Remove a área existente

        self.output_frame = tk.Frame(
            self.root, bg="#333333", highlightthickness=2, highlightbackground="#FFD700", relief="raised"
        )
        self.output_frame.place(relx=0.5, rely=0.6, anchor="center", width=600, height=300)

        # Botão "close" dentro da área de saída
        self.close_icon = ImageTk.PhotoImage(Image.open("assets/close_icon.png").resize((20, 20)))
        self.close_button = tk.Button(
            self.output_frame,
            image=self.close_icon,
            bg="#333333",
            bd=0,
            activebackground="#444444",
            command=self.resetar_tela,
        )
        self.close_button.place(x=570, y=5)

        # Exibir poderes dos dragões
        dragao_label = tk.Label(
            self.output_frame,
            text="Poder dos Dragões:",
            bg="#333333",
            fg="#FFD700",
            font=("Helvetica", 12, "bold"),
        )
        dragao_label.place(x=10, y=30)

        dragao_texto = self.formatar_lista_com_quebra(poderes_dragao, largura=10)
        dragao_valor = tk.Label(
            self.output_frame,
            text=dragao_texto,
            bg="#333333",
            fg="#FFD700",
            font=("Courier", 12),
            justify="left",
        )
        dragao_valor.place(x=10, y=60)

        # Exibir poder mágico em azul
        poder_label = tk.Label(
            self.output_frame,
            text=f"Seu Poder Mágico: {poder_magico}",
            bg="#333333",
            fg="#00BFFF",  # Azul destacado
            font=("Courier", 12, "bold"),
        )
        poder_label.place(x=10, y=120)

        # Exibir dragões capturados
        capturados_label = tk.Label(
            self.output_frame,
            text="Dragões Capturados (Índices):",
            bg="#333333",
            fg="#FFFFFF",
            font=("Helvetica", 12, "bold"),
        )
        capturados_label.place(x=10, y=160)

        capturados_text = self.formatar_lista_com_quebra(indices_capturados, largura=10) if indices_capturados else "Nenhum"
        capturados_valor = tk.Label(
            self.output_frame,
            text=capturados_text,
            bg="#333333",
            fg="#FFD700",
            font=("Courier", 12),
            justify="left",
        )
        capturados_valor.place(x=10, y=190)

    def formatar_lista_com_quebra(self, lista, largura=10):
        """
        Formata uma lista para exibir com quebras de linha.
        A quebra só ocorrerá se o tamanho da lista for maior que 10.
        """
        if len(lista) > largura:
            return "\n".join(", ".join(map(str, lista[i:i + largura])) for i in range(0, len(lista), largura))
        return ", ".join(map(str, lista))

    def exibir_erro(self, mensagem):
        erro_popup = tk.Toplevel(self.root)
        erro_popup.title("Erro")
        erro_popup.geometry("300x100")
        erro_label = tk.Label(erro_popup, text=mensagem, fg="red", font=("Helvetica", 12))
        erro_label.pack(pady=20)
        tk.Button(erro_popup, text="Fechar", command=erro_popup.destroy).pack()

    def resetar_tela(self):
        # Remove a área de saída e reseta a tela inicial
        if hasattr(self, "output_frame"):
            self.output_frame.destroy()
            del self.output_frame
        self.resetar_campos()


if __name__ == "__main__":
    root = tk.Tk()
    app = DragonHunterApp(root)
    root.mainloop()
