import tkinter as tk


class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create the entry widget for displaying the result
        self.result_entry = tk.Entry(master, width=20, justify="right")
        self.result_entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Create the calculator buttons and add them to the grid layout
        self.create_button("7", 1, 0)
        self.create_button("8", 1, 1)
        self.create_button("9", 1, 2)
        self.create_button("/", 1, 3)
        self.create_button("4", 2, 0)
        self.create_button("5", 2, 1)
        self.create_button("6", 2, 2)
        self.create_button("*", 2, 3)
        self.create_button("1", 3, 0)
        self.create_button("2", 3, 1)
        self.create_button("3", 3, 2)
        self.create_button("-", 3, 3)
        self.create_button("0", 4, 0)
        self.create_button(".", 4, 1)
        self.create_button("=", 4, 2)
        self.create_button("+", 4, 3)
        self.create_button("C", 5, 0, columnspan=2)
        self.create_button("CE", 5, 2, columnspan=2)

    def create_button(self, text, row, column, columnspan=1):
        button = tk.Button(self.master, text=text, width=5, height=2, command=lambda: self.button_click(text))
        button.grid(row=row, column=column, columnspan=columnspan, padx=5, pady=5)

    def button_click(self, text):
        if text == "C":
            self.result_entry.delete(0, tk.END)
        elif text == "CE":
            self.result_entry.delete(0, tk.END)
        elif text == "=":
            try:
                result = eval(self.result_entry.get())
                self.result_entry.delete(0, tk.END)
                self.result_entry.insert(0, str(result))
            except:
                self.result_entry.delete(0, tk.END)
                self.result_entry.insert(0, "Error")
        else:
            self.result_entry.insert(tk.END, text)


root = tk.Tk()
calculator = Calculator(root)
root.mainloop()
