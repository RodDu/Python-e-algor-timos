import tkinter as tk


class TextPresenter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Apresentador de Texto")

        # Adicionando o campo de entrada
        tk.Label(self.root, text="Insira aqui o seu texto").pack(padx=20, pady=5)
        self.text_entry = tk.Text(self.root, height=10, width=40, font=("Arial", 16))
        self.text_entry.pack(padx=20, pady=5)
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
