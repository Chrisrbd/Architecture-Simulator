import tkinter as tk


class App:
    def __init__(self, master):
        self.master = master
        master.title("Hello World")

        self.alphabet = ['A 10', 'B 15', 'RES 0']
        self.index = 0

        self.button = tk.Button(master, text="Next", command=self.next_element)
        self.button.pack()

        self.t0_value = 0
        self.t1_value = 0
        self.t2_value = 0
        self.t3_value = 0

        self.label = tk.Label(master, text="Registers :")
        self.label.pack()
        self.t0_label = tk.Label(master, text="T0 = " + str(self.t0_value))
        self.t0_label.pack()
        self.t1_label = tk.Label(master, text="T1 = " + str(self.t1_value))
        self.t1_label.pack()
        self.t2_label = tk.Label(master, text="T2 = " + str(self.t2_value))
        self.t2_label.pack()
        self.t3_label = tk.Label(master, text="T3 = " + str(self.t3_value))
        self.t3_label.pack()

        self.label = tk.Label(master, text="Variables :")
        self.label.pack()

        self.frame = tk.Frame(master)
        self.frame.pack()

    def next_element(self):
        if self.index < len(self.alphabet):
            element = self.alphabet[self.index].split()
            label_text = element[0] + " = " + element[1]
            tk.Label(self.frame, text=label_text).pack()
            self.index += 1

        self.t0_value += 1
        self.t0_label.configure(text="T0 = " + str(self.t0_value))


root = tk.Tk()
app = App(root)
root.mainloop()
