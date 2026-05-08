import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        self.expression = ""
        self.input_text = tk.StringVar()
        
        # Create display
        self.display = tk.Entry(
            root,
            textvar=self.input_text,
            font=("Arial", 24),
            borderwidth=2,
            relief="solid",
            justify="right",
            state="readonly"
        )
        self.display.pack(fill="both", padx=10, pady=20, ipady=10)
        
        # Create buttons frame
        button_frame = tk.Frame(root)
        button_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C", "←"]
        ]
        
        for row in buttons:
            row_frame = tk.Frame(button_frame)
            row_frame.pack(fill="both", expand=True, pady=5)
            
            for btn_text in row:
                btn = tk.Button(
                    row_frame,
                    text=btn_text,
                    font=("Arial", 18),
                    command=lambda x=btn_text: self.on_button_click(x)
                )
                btn.pack(side="left", fill="both", expand=True, padx=5)
    
    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
            self.input_text.set("")
        elif char == "←":
            self.expression = self.expression[:-1]
            self.input_text.set(self.expression)
        elif char == "=":
            try:
                result = eval(self.expression)
                self.input_text.set(str(result))
                self.expression = str(result)
            except:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += char
            self.input_text.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
