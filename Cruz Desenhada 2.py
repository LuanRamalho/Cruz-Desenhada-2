import tkinter as tk
import random

def desenhar_cruz(canvas, x, y, tamanho, cor):
    """Desenha uma cruz no canvas."""
    # Linha vertical
    canvas.create_line(x, y - tamanho, x, y + tamanho, fill=cor, width=2)
    # Linha horizontal
    canvas.create_line(x - tamanho, y, x + tamanho, y, fill=cor, width=2)

def desenhar_cruzes(canvas, largura, altura):
    """Desenha várias cruzes no canvas."""
    quantidade = random.randint(5, 20)  # Define uma quantidade aleatória de cruzes
    for _ in range(quantidade):
        x = random.randint(0, largura)
        y = random.randint(0, altura)
        tamanho = random.randint(10, 50)  # Define um tamanho aleatório para a cruz
        cor = "#%06x" % random.randint(0, 0xFFFFFF)  # Define uma cor aleatória
        desenhar_cruz(canvas, x, y, tamanho, cor)

def main():
    largura = 800
    altura = 600

    # Criar a janela principal
    root = tk.Tk()
    root.title("Cruz Aleatórias")

    # Criar o canvas
    canvas = tk.Canvas(root, width=largura, height=altura, bg="white")
    canvas.pack()

    # Desenhar as cruzes
    desenhar_cruzes(canvas, largura, altura)

    # Iniciar o loop principal
    root.mainloop()

if __name__ == "__main__":
    main()
