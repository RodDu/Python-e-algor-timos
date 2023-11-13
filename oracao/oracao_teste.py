import tkinter as tk


class TextPresenter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x400")
        self.root.title("Apresentador de Texto")

        # Adicionando o campo de entrada
        tk.Label(self.root, text="Insira aqui o seu texto").grid(
            row=0, column=0, padx=5, pady=35
        )

        # Criando um Frame como contêiner para o Text widget
        frame = tk.Frame(self.root)
        frame.grid(row=1, column=1, sticky="nsew")

        # Configurando as linhas e colunas para expandir corretamente
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        # Modificando o Text widget para usar o gerenciador de geometria grid
        self.text_entry = tk.Text(self.root, height=12, width=45, font=("Arial", 16))
        self.text_entry.place(relx=0.5, rely=0.5, anchor="center")

        self.text_entry.bind("<Key>", self.key_press)

        # Variáveis de controle
        self.running = False
        self.paused = False
        self.words = []
        self.index = 0

        self.root.mainloop()

    def key_press(self, event):
        if event.char == "4":  # Iniciar
            if not self.running:
                self.start_display()
        elif event.char == "5":  # Pausar
            self.paused = True
        elif event.char == "6":  # Continuar
            if self.paused:
                self.paused = False
                self.display_word()
        elif event.char == "0":  # Reiniciar
            self.running = False
            self.text_entry.delete(1.0, tk.END)
            self.words = []
            self.index = 0

    def start_display(self):
        self.running = True
        self.paused = False
        text = self.text_entry.get(1.0, tk.END).strip()
        self.words = text.split()
        self.index = 0
        self.display_word()

    def display_word(self):
        if self.paused or self.index >= len(self.words):
            return

        word = self.words[self.index]
        self.text_entry.delete(1.0, tk.END)
        self.text_entry.insert(tk.END, word)

        # Define o tempo baseado no comprimento da palavra
        delay = len(word) * 100  # Tempo em milissegundos

        # Pausas adicionais para , e .
        if "," in word:
            delay += 500
        elif "." in word:
            delay += 1500

        self.index += 1

        # Agendar a exibição da próxima palavra
        self.root.after(delay, self.display_word)


if __name__ == "__main__":
    TextPresenter()
