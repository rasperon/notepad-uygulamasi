import tkinter as tk
from tkinter import messagebox

# Tema değişkenleri
dark_theme = {
    "bg": "black",
    "fg": "white",
}

light_theme = {
    "bg": "white",
    "fg": "black",
}

# Başlangıç teması olarak açık temasını ayarla
current_theme = light_theme

# Kopyala işlemi
def copy_text():
    text_widget.clipboard_clear()
    text_widget.clipboard_append(text_widget.selection_get())

# Yapıştır işlemi
def paste_text():
    try:
        text_widget.insert(tk.INSERT, text_widget.clipboard_get())
    except tk.TclError:
        pass

# Kaydet işlemi
def save_text():
    content = text_widget.get("1.0", tk.END)
    with open("rasperonpad.txt", "w") as file:
        file.write(content)
    messagebox.showinfo("Bilgi", "Dosya kaydedildi.")

# Geri alma işlemi
def undo_text():
    text_widget.edit_undo()

# İleri alma işlemi
def redo_text():
    text_widget.edit_redo()

# Tema değiştirme işlemi
def toggle_theme():
    global current_theme
    if current_theme == light_theme:
        current_theme = dark_theme
        text_widget.config(**dark_theme)  # Tema değiştiğinde metin rengini güncelle
    else:
        current_theme = light_theme
        text_widget.config(**light_theme)  # Tema değiştiğinde metin rengini güncelle

# Ana pencereyi oluştur
root = tk.Tk()
root.title("RasperonPad")
root.iconbitmap('icon.ico')

# Pencere boyutunu ayarla
root.geometry("800x600")

# Metin düzenleme alanını oluştur
text_widget = tk.Text(root, **current_theme)
text_widget.pack(fill=tk.BOTH, expand=True)

# Metin düzenleme alanına odaklan
text_widget.focus_set()

# Metni belirgin hale getirmek için bir etiket kullanalım
watermark_label = tk.Label(text_widget, text="RASPERON", font=("Helvetica", 30), fg=current_theme["bg"])
watermark_label.place(relx=0.5, rely=0.5, anchor="center")

# Menü çubuğunu oluştur
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Dosya menüsünü oluştur
file_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Dosya", menu=file_menu)
file_menu.add_command(label="Kopyala (Ctrl+C)", command=copy_text)
file_menu.add_command(label="Yapıştır (Ctrl+V)", command=paste_text)
file_menu.add_command(label="Kaydet (Ctrl+S)", command=save_text)

# Düzen menüsünü oluştur
edit_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Düzen", menu=edit_menu)
edit_menu.add_command(label="Geri Al (Ctrl+Z)", command=undo_text)
edit_menu.add_command(label="İleri Al (Ctrl+Y)", command=redo_text)

# Tema menüsünü oluştur
theme_menu = tk.Menu(menu_bar)
menu_bar.add_cascade(label="Tema", menu=theme_menu)
theme_menu.add_command(label="Tema Değiştir", command=toggle_theme)

# Ana döngüyü başlat
root.mainloop()
