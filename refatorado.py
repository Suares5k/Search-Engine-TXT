import tkinter as tk
from tkinter import filedialog
import os

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def search_and_save():
    file_path = file_entry.get()
    search_word = search_entry.get()
    
    if not file_path or not search_word:
        result_label.config(text="Por favor, selecione um arquivo e insira uma palavra para buscar.")
        return
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        results = []
        for line in lines:
            if search_word in line:
                # Extrair a parte após o último ":"
                parts = line.split(':')
                if len(parts) > 2:
                    result = ':'.join(parts[-2:])  # Pega as duas últimas partes
                    results.append(result)
        
        if results:
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            output_file = os.path.join(desktop, 'resultados.txt')
            
            with open(output_file, 'w', encoding='utf-8') as output:
                output.writelines(results)
            
            result_label.config(text=f"Resultados salvos em: {output_file}")
        else:
            result_label.config(text="Nenhuma ocorrência encontrada.")
    except Exception as e:
        result_label.config(text=f"Ocorreu um erro: {e}")

# Configuração da GUI
root = tk.Tk()
root.title("Busca em Arquivo .txt")

tk.Label(root, text="Selecione o arquivo:").grid(row=0, column=0, padx=10, pady=10)
file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Palavra para buscar:").grid(row=1, column=0, padx=10, pady=10)
search_entry = tk.Entry(root, width=50)
search_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Buscar e Salvar", command=search_and_save).grid(row=2, column=1, padx=10, pady=20)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
