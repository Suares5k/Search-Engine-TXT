import tkinter as tk
from tkinter import filedialog
import os

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def extract_and_save():
    file_path = file_entry.get()
    
    if not file_path:
        result_label.config(text="Por favor, selecione um arquivo.")
        return
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        
        results = []
        for line in lines:
            parts = line.split(':')
            if len(parts) > 1:
                result = parts[0]  # Pega a parte antes do primeiro ":"
                results.append(result + '\n')
        
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
root.title("Extração de Texto de Arquivo .txt")

tk.Label(root, text="Selecione o arquivo:").grid(row=0, column=0, padx=10, pady=10)
file_entry = tk.Entry(root, width=50)
file_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_file).grid(row=0, column=2, padx=10, pady=10)

tk.Button(root, text="Extrair e Salvar", command=extract_and_save).grid(row=1, column=1, padx=10, pady=20)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
