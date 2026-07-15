"""
=========================================
Simple Language Translation Tool
CodeAlpha Internship Project
Only 3 Languages: English, Urdu, Arabic
=========================================
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from deep_translator import GoogleTranslator
import pyperclip


LANGUAGES = {
    "English": "en",
    "Urdu": "ur",
    "Arabic": "ar"
}


COLORS = {
    "bg_main": "#C7C2C2",
    "bg_secondary": "#FFFDFD",
    "primary": "#002441",
    "accent": "#FF6B6B",
    "success": "#6AD977",
    "warning": "#B96914",
    "danger": "#E92C2C",
    "neutral": "#1E262E",
    "text": "#000000",
    "border": "#111213"
}


class LanguageTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("LANGUAGE TRANSLATION TOOL")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        self.root.config(bg=COLORS["bg_main"])
        
    
        self.create_ui()
    
    def create_ui(self):
        # Title
        title = tk.Label(
            self.root,
            text="🌐 Language Translation Tool",
            font=("Segoe UI", 20, "bold"),
            fg=COLORS["primary"],
            bg=COLORS["bg_main"]
        )
        title.pack(pady=15)
        
    
        lang_frame = tk.Frame(self.root, bg=COLORS["bg_secondary"], relief=tk.RIDGE, bd=1)
        lang_frame.pack(pady=12, padx=15, fill="x")
        
       
        tk.Label(
            lang_frame,
            text="From:",
            font=("Segoe UI", 11, "bold"),
            bg=COLORS["bg_secondary"],
            fg=COLORS["primary"]
        ).grid(row=0, column=0, padx=10, pady=10)
        
        self.source_lang = ttk.Combobox(
            lang_frame,
            values=list(LANGUAGES.keys()),
            state="readonly",
            width=12,
            font=("Segoe UI", 10)
        )
        self.source_lang.grid(row=0, column=1, padx=5, pady=10)
        self.source_lang.current(0)
        
       
        tk.Label(
            lang_frame,
            text="To:",
            font=("Segoe UI", 11, "bold"),
            bg=COLORS["bg_secondary"],
            fg=COLORS["primary"]
        ).grid(row=0, column=2, padx=10, pady=10)
        
        self.target_lang = ttk.Combobox(
            lang_frame,
            values=list(LANGUAGES.keys()),
            state="readonly",
            width=12,
            font=("Segoe UI", 10)
        )
        self.target_lang.grid(row=0, column=3, padx=5, pady=10)
        self.target_lang.current(1)
        
    
        tk.Label(
            self.root,
            text="📝 Enter Text:",
            font=("Segoe UI", 11, "bold"),
            bg=COLORS["bg_main"],
            fg=COLORS["primary"]
        ).pack(pady=(12, 5), padx=15, anchor="w")
        
        self.input_text = scrolledtext.ScrolledText(
            self.root,
            width=80,
            height=5,
            font=("Segoe UI", 10),
            wrap=tk.WORD,
            bg=COLORS["bg_secondary"],
            fg=COLORS["text"],
            relief=tk.FLAT,
            bd=1,
            insertbackground=COLORS["primary"]
        )
        self.input_text.pack(pady=5, padx=15, fill="both", expand=True)
        
        
        btn_frame = tk.Frame(self.root, bg=COLORS["bg_main"])
        btn_frame.pack(pady=10)
        
     
        tk.Button(
            btn_frame,
            text="🔄 Translate",
            bg=COLORS["success"],
            fg="white",
            font=("Segoe UI", 10, "bold"),
            width=14,
            relief=tk.FLAT,
            activebackground="#40C057",
            command=self.translate_text
        ).grid(row=0, column=0, padx=5)
        
     
        tk.Button(
            btn_frame,
            text="🗑️ Clear",
            bg=COLORS["danger"],
            fg="white",
            font=("Segoe UI", 10),
            width=14,
            relief=tk.FLAT,
            activebackground="#FA5252",
            command=self.clear_text
        ).grid(row=0, column=1, padx=5)
        
     
        tk.Button(
            btn_frame,
            text="⇄ Swap",
            bg=COLORS["neutral"],
            fg="white",
            font=("Segoe UI", 10),
            width=14,
            relief=tk.FLAT,
            activebackground="#5C7080",
            command=self.swap_languages
        ).grid(row=0, column=2, padx=5)
        
      
        tk.Label(
            self.root,
            text="✨ Translated Text:",
            font=("Segoe UI", 11, "bold"),
            bg=COLORS["bg_main"],
            fg=COLORS["primary"]
        ).pack(pady=(10, 5), padx=15, anchor="w")
        
        self.output_text = scrolledtext.ScrolledText(
            self.root,
            width=80,
            height=5,
            font=("Segoe UI", 10),
            wrap=tk.WORD,
            bg="#E8F5E9",
            fg=COLORS["text"],
            relief=tk.FLAT,
            bd=1,
            state=tk.DISABLED
        )
        self.output_text.pack(pady=5, padx=15, fill="both", expand=True)
  
        tk.Button(
            self.root,
            text="📋 Copy to Clipboard",
            bg=COLORS["primary"],
            fg="white",
            font=("Segoe UI", 10, "bold"),
            width=22,
            relief=tk.FLAT,
            activebackground="#1F3A5F",
            command=self.copy_text
        ).pack(pady=8)
        
     
        self.status = tk.Label(
            self.root,
            text="✅ Ready to translate!",
            bd=0,
            anchor="w",
            font=("Segoe UI", 9),
            bg=COLORS["primary"],
            fg="white",
            padx=10,
            pady=5
        )
        self.status.pack(fill="x", side="bottom")
    
    def translate_text(self):
      
        text = self.input_text.get("1.0", tk.END).strip()
        
    
        if text == "":
            messagebox.showwarning(
                "Warning",
                "Please enter some text to translate!"
            )
            return
        
 
        source = LANGUAGES[self.source_lang.get()]
        target = LANGUAGES[self.target_lang.get()]
        
        try:
           
            self.status.config(text="⏳ Translating...", bg=COLORS["warning"])
            self.root.update()
            
           
            translated = GoogleTranslator(
                source=source,
                target=target
            ).translate(text)
        
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, translated)
            self.output_text.config(state=tk.DISABLED)
            
            self.status.config(text="✅ Translation successful!", bg=COLORS["success"])
            
        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Translation failed: {str(e)}"
            )
            self.status.config(text="❌ Translation failed", bg=COLORS["danger"])
    
    def clear_text(self):

        self.input_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state=tk.DISABLED)
        self.status.config(text="🧹 Cleared all text", bg=COLORS["primary"])
    
    def swap_languages(self):
      
        source = self.source_lang.get()
        target = self.target_lang.get()
        
        self.source_lang.set(target)
        self.target_lang.set(source)
        
        self.status.config(text="🔄 Languages swapped!", bg=COLORS["primary"])
    
    def copy_text(self):
       
        text = self.output_text.get("1.0", tk.END).strip()
        
        if text == "":
            messagebox.showinfo(
                "Info",
                "Nothing to copy! First translate some text."
            )
            return
        
        pyperclip.copy(text)
        messagebox.showinfo(
            "Success",
            "✅ Text copied to clipboard!"
        )
        self.status.config(text="📋 Copied to clipboard!", bg=COLORS["primary"])


if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslator(root)
    root.mainloop()