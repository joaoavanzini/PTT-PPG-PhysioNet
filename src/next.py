import tkinter as tk
from PIL import Image, ImageTk
import os

# Diretório onde as imagens estão localizadas
image_directory = "/home/palhares/Documents/PTT-PPG-PhysioNet/figures"

# Lista de nomes de arquivos de imagem
image_files = [
    "s10_run.png", "s13_sit.png", "s16_walk.png", "s1_run.png",
    "s22_sit.png", "s4_walk.png", "s8_run.png", "s10_sit.png",
    "s13_walk.png", "s17_run.png", "s1_sit.png", "s22_walk.png",
    "s5_run.png", "s8_sit.png", "s10_walk.png", "s14_run.png",
    "s17_sit.png", "s1_walk.png", "s2_run.png", "s5_sit.png",
    "s8_walk.png", "s11_run.png", "s14_sit.png", "s17_walk.png",
    "s20_run.png", "s2_sit.png", "s5_walk.png", "s9_run.png",
    "s11_sit.png", "s14_walk.png", "s18_run.png", "s20_sit.png",
    "s2_walk.png", "s6_run.png", "s9_sit.png", "s11_walk.png",
    "s15_run.png", "s18_sit.png", "s20_walk.png", "s3_run.png",
    "s6_sit.png", "s9_walk.png", "s12_run.png", "s15_sit.png",
    "s18_walk.png", "s21_run.png", "s3_sit.png", "s6_walk.png",
    "s12_sit.png", "s15_walk.png", "s19_run.png", "s21_sit.png",
    "s3_walk.png", "s7_run.png", "s12_walk.png", "s16_run.png",
    "s19_sit.png", "s21_walk.png", "s4_run.png", "s7_sit.png",
    "s13_run.png", "s16_sit.png", "s19_walk.png", "s22_run.png",
    "s4_sit.png", "s7_walk.png"
]

# Função para mostrar a próxima imagem
def show_next_image():
    global current_image_index
    if current_image_index < len(image_files):
        image_path = os.path.join(image_directory, image_files[current_image_index])
        img = Image.open(image_path)
        img = img.resize((800, 600), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        label.config(image=img)
        label.image = img
        current_image_index += 1
    else:
        current_image_index = 0  # Volta ao começo
    root.after(100, show_next_image)  # Aguarda 0.1 segundo antes de mostrar a próxima imagem

# Configura a janela principal
root = tk.Tk()
root.title("Wavelength")
root.geometry("800x600")

# Inicializa variáveis
current_image_index = 0

# Cria um rótulo para exibir as imagens
label = tk.Label(root)
label.pack(expand="true", fill="both")

# Inicia a exibição das imagens
show_next_image()

root.mainloop()
