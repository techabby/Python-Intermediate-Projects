import tkinter as tk
from tkinter import filedialog

class TextEditor():
    def __init__(self, root):
        self.root = root 
        self.root.title("Text Editor")
        Menu_bar = tk.Menu(self.root)
        self.root.config(menu=Menu_bar)
        
        # File Menu
        FileMenu = tk.Menu(Menu_bar, tearoff=0)
        FileMenu.add_command(label="New", command=self.new_file)
        FileMenu.add_command(label="Open", command=self.open_file)
        FileMenu.add_command(label="Save", command=self.save_file)
        FileMenu.add_separator()
        FileMenu.add_command(label="Exit", command=self.root.quit)
        Menu_bar.add_cascade(label="File", menu=FileMenu)
        
        # Font Menu
        FontMenu = tk.Menu(Menu_bar, tearoff=0)
        Fonts = [
            "Arial", "Courier New", "Times New Roman", 
            "Helvetica", "Symbol", "Georgia", 
            "Comic Sans MS", "Verdana", "Impact", 
            "Trebuchet MS"
        ]
        for Font in Fonts:
            FontMenu.add_command(label=Font, command=lambda f=Font: self.set_font(f))
        Menu_bar.add_cascade(label="Fonts", menu=FontMenu)

        self.TextArea = tk.Text(self.root)
        self.TextArea.pack(fill=tk.BOTH, expand=True)

    def new_file(self):
        self.TextArea.delete('1.0', tk.END)

    def open_file(self):
        Path = filedialog.askopenfilename()
        with open(Path, 'r') as f:
            self.TextArea.delete('1.0', tk.END)
            self.TextArea.insert(tk.END, f.read())

    def save_file(self):
        Path = filedialog.asksaveasfilename()
        if Path:
            with open(Path, 'w') as f:
                f.write(self.TextArea.get('1.0', tk.END))

    def set_font(self, Font):
        self.TextArea.tag_configure("my_font", font=(Font, 12))
        self.TextArea.tag_add("my_font", "1.0", tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    TextEditor(root)
    root.mainloop()
