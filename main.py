import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import os


class ALU:
    def __init__(self, variables, sp):
        # Dictionary of instruction
        self.variables = variables
        self.SP = sp
        self.instructions = {
            "LDA": self.func_lda,
            "STR": self.func_str,
            "PUSH": self.func_push,
            "POP": self.func_pop,
            "AND": self.func_and,
            "OR": self.func_or,
            "NOT": self.func_not,
            "ADD": self.func_add,
            "SUB": self.func_sub,
            "DIV": self.func_div,
            "MUL": self.func_mul,
            "MOD": self.func_mod,
            "INC": self.func_inc,
            "DEC": self.func_dec,
            "BEQ": self.func_beq,
            "BNE": self.func_bne,
            "BBG": self.func_bgg,
            "BSM": self.func_bsm,
            "JMP": self.func_jmp,
            "HLT": self.func_hlt,
            "SRL": self.func_srl,
            "SRR": self.func_srr
        }

    def func_lda(self, reg, y):
        print("LDA:", reg, "<--", y)
        if reg in list(self.variables)[0:3]:
            if y.isdigit():
                # If y is a number
                self.variables[reg] = int(y)
            elif y in self.variables:
                # If y is a variable
                self.variables[reg] = self.variables[y]
            else:
                raise ValueError(y, " must be an integer")
        else:
            print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")

    def func_str(self, var, y):
        print("STR:", var, "<--", y)
        if var in list(self.variables)[0:3]:
            # If y is a register
            print("Error: Register stores are NOT ALLOWED.")
        if y.isdigit():
            # If y is a number
            self.variables[var] = int(y)
        else:
            # If y is a variable
            self.variables[var] = self.variables[y]

    def func_push(self, var):
        print("PUSH: stack <--", var)
        if var.isdigit():
            # If y is a number
            self.variables["Stack"] = int(var)
        else:
            # If y is a variable
            self.variables["Stack"] = self.variables[var]
        self.SP += 1

    def func_pop(self, var):
        if var in list(self.variables)[0:3]:
            # If y is a register
            self.SP -= 1
            self.variables[var] = self.variables["Stack"]
            print("POP:", var, " <-- stack")
        else:
            print("Error: Storing in a memory region is NOT ALLOWED.")

    def func_and(self, reg1, var):
        print("AND:", reg1, "=", reg1, "and", var)
        if reg1 in list(self.variables)[0:3]:
            if var in self.variables:
                self.variables[reg1] = self.variables[reg1] and self.variables[var]
            elif var.isdigit():
                self.variables[reg1] = self.variables[reg1] and int(var)
            else:
                print(f"Error: {var} is not a valid register, variable, or constant")
        else:
            print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")

    def func_or(self, reg1, var):
        print("OR:", reg1, "=", reg1, "or", var)
        if reg1 in list(self.variables)[0:3]:
            if var in self.variables:
                self.variables[reg1] = self.variables[reg1] or self.variables[var]
            elif var.isdigit():
                self.variables[reg1] = self.variables[reg1] or int(var)
            else:
                print(f"Error: {var} is not a valid register, variable, or constant")
        else:
            print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")

    def func_not(self, reg):
        print("NOT:", reg, "= not", reg)
        if reg in list(self.variables)[0:3]:
            self.variables[reg] = not self.variables[reg]
        else:
            print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")

    def func_add(self, reg, var):
        print("ADD:", reg, "=", reg, "+", var)
        if reg in list(self.variables)[0:3]:
            if var in self.variables:
                self.variables[reg] += self.variables[var]
            elif var.isdigit():
                self.variables[reg] += int(var)
            else:
                print(f"Error: {var} is not a valid register, variable, or constant")
        else:
            print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")

    def func_sub(self, reg, var):
        print("SUB:", reg, "=", var, "-", reg)
        if reg in list(self.variables)[0:3]:
            if var in self.variables:
                self.variables[reg] = self.variables[var] - self.variables[reg]
            elif var.isdigit():
                self.variables[reg] = int(var) - self.variables[reg]
            else:
                print(f"Error: {var} is not a valid register, variable, or constant")
        else:
            print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")

    def func_div(self, reg, var):
        print("DIV:", reg, "=", reg, "/", var)
        if reg in list(self.variables)[0:3]:
            if var == 0:
                print("Error: Division by zero")
            elif var in self.variables:
                self.variables[reg] //= self.variables[var]
            elif var.isdigit():
                self.variables[reg] //= int(var)
            else:
                print(f"Error: {var} is not a valid register, variable, or constant")
        else:
            print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")

    def func_mul(self, reg, var):
        print("MUL:", reg, "=", reg, "*", var)
        if reg in list(self.variables)[0:3]:
            if var in self.variables:
                self.variables[reg] *= self.variables[var]
            elif var.isdigit():
                self.variables[reg] *= int(var)
            else:
                print(f"Error: {var} is not a valid register, variable, or constant")
        else:
            print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")

    def func_mod(self, reg, var):
        if self.variables[var] == 0:
            raise ZeroDivisionError("Modulo by zero")
        print("MOD:", reg, "=", reg, "%", var)
        if reg in list(self.variables)[0:3]:
            if var in self.variables:
                self.variables[reg] = self.variables[reg] % self.variables[var]
            elif var.isdigit():
                self.variables[reg] = self.variables[reg] % int(var)
            else:
                print(f"Error: {var} is not a valid register, variable, or constant")
        else:
            print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")

    def func_inc(self, reg):
        print("INC:", reg, "=", reg, "+ 1")
        if reg in list(self.variables)[0:3]:
            self.variables[reg] += 1
        else:
            print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")

    def func_dec(self, reg):
        print("DEC:", reg, "=", reg, "- 1")
        if reg in list(self.variables)[0:3]:
            if self.variables[reg] == 0:
                raise ValueError("Cannot decrement register that already contains zero")
            else:
                self.variables[reg] -= 1
        else:
            print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")

    def func_beq(self, reg1, reg2, address):
        if reg1 & reg2 in self.variables:
            if self.variables[reg1] == self.variables[reg2]:
                self.func_jmp(address)
        elif reg1 in self.variables:
            if self.variables[reg1] == reg2:
                self.func_jmp(address)
        elif reg2 in self.variables:
            if reg1 == self.variables[reg2]:
                self.func_jmp(address)
        else:
            if reg1 == reg2:
                self.func_jmp(address)

    def func_bne(self, reg1, reg2, address):
        if reg1 & reg2 in self.variables:
            if self.variables[reg1] != self.variables[reg2]:
                self.func_jmp(address)
        elif reg1 in self.variables:
            if self.variables[reg1] != reg2:
                self.func_jmp(address)
        elif reg2 in self.variables:
            if reg1 != self.variables[reg2]:
                self.func_jmp(address)
        else:
            if reg1 != reg2:
                self.func_jmp(address)

    def func_bgg(self, reg1, reg2, address):
        if reg1 & reg2 in self.variables:
            if self.variables[reg1] > self.variables[reg2]:
                self.func_jmp(address)
        elif reg1 in self.variables:
            if self.variables[reg1] > reg2:
                self.func_jmp(address)
        elif reg2 in self.variables:
            if reg1 > self.variables[reg2]:
                self.func_jmp(address)
        else:
            if reg1 > reg2:
                self.func_jmp(address)

    def func_bsm(self, reg1, reg2, address):
        if reg1 & reg2 in self.variables:
            if self.variables[reg1] < self.variables[reg2]:
                self.func_jmp(address)
        elif reg1 in self.variables:
            if self.variables[reg1] < reg2:
                self.func_jmp(address)
        elif reg2 in self.variables:
            if reg1 < self.variables[reg2]:
                self.func_jmp(address)
        else:
            if reg1 < reg2:
                self.func_jmp(address)

    def func_jmp(self, address):
        # set program counter to address
        pass

    def func_hlt(self):
        print("HLT: end the program execution!")
        # stop execution
        pass

    def func_srl(self, reg, const):
        print("SRL:", reg, "=", reg, ">>", const)
        self.variables[reg] = self.variables[reg] // (2 ** int(const))

    def func_srr(self, reg, const):
        print("SRR:", reg, "=", reg, "<<", const)
        self.variables[reg] = self.variables[reg] * (2 ** int(const))


class ProgramCounter:
    def __init__(self):
        self.pc = 0

    def next(self):
        self.pc += 1


class Simulator:
    def __init__(self):
        # Creation of the stack + stack pointer to follow the current position in the stack
        self.stack = [0] * 4096
        self.SP = 0  # Stack pointer initialized to 0

        self.variables = {"T0": 0, "T1": 0, "T2": 0, "T3": 0,
                          "Stack": self.stack}  # Stack is the last element in the Stack
        self.alu = ALU(self.variables, self.SP)
        self.program_counter = ProgramCounter()

    def load_program(self, filename):
        # Store from the .asm file the #DATA section lines and #CODE section lines in different tabs
        with open(filename, "r") as file:
            # 2 shared memories, one to store the data and another to store the code
            data_lines = []
            code_lines = []
            is_data_section = False
            is_code_section = False

            for line in file:
                # Remove comments and store the filtered code in filtered_lines
                parts = line.split("!", 1)
                filtered_lines = parts[0].strip()

                # Separate #DATA section and #CODE section in different tabs
                for line in filtered_lines.splitlines():
                    # If the line starts with #DATA, set is_data_section to True and is_code_section to False
                    if line.startswith("#DATA"):
                        is_data_section = True
                        is_code_section = False
                    # If the line starts with #CODE, set is_code_section to True and is_data_section to False
                    elif line.startswith("#CODE"):
                        is_data_section = False
                        is_code_section = True
                    # Otherwise, if the current section is #DATA, add the line to data_lines
                    elif is_data_section:
                        data_lines.append(line.strip())
                    # Otherwise, if the current section is #CODE, add the line to code_lines
                    elif is_code_section:
                        code_lines.append(line.strip())

        return data_lines, code_lines

    def execute_program(self, data_lines, code_lines, line):
        # Execute #DATA section
        print("\n#DATA section translated:")
        print(data_lines, "\n")
        for l in data_lines:
            # Split the line into variable name and initial value
            parts = l.split()
            var_name = parts[0]
            var_value = int(parts[1])

            # Dynamically create a variable with the given name and initial value
            self.variables[var_name] = var_value
            print(var_name, " = ", var_value)
        print()
        print(self.variables)

        print("\n#CODE section result:")
        print(code_lines, "\n")
        # Execute #CODE section
        # Separate the instruction from its arguments
        parts = line.split(" ")
        instruction = parts[0]
        args = parts[1:]
        # Look if operations are in the list of operations in ALU and execute the corresponding function
        if instruction in self.alu.instructions.keys():
            self.alu.instructions[instruction](*args)
        else:
            print("Error: Operation not found")
        print(self.variables)


def gui():
    simulator = Simulator()
    root = tk.Tk()
    root.title("Assembly Simulator")

    filename = ""
    data_lines, code_lines = [], []

    instructions_frame = ttk.LabelFrame(root, text="Instruction")
    instructions_frame.grid(row=0, column=0, padx=10, pady=10)

    registers_frame = ttk.LabelFrame(root, text="Registers")
    registers_frame.grid(row=1, column=0, padx=10, pady=10)

    variables_frame = ttk.LabelFrame(root, text="Variables")
    variables_frame.grid(row=0, column=1, padx=10, pady=10)

    stack_frame = ttk.LabelFrame(root, text="Stack")
    stack_frame.grid(row=1, column=1, padx=10, pady=10)

    filename_label = ttk.Label(root, text="File name:")
    filename_label.grid(row=2, column=0, padx=10, pady=10)

    instructions_label = ttk.Label(root, text="Next instruction:")
    instructions_label.grid(row=3, column=0, padx=10, pady=10)

    instructions_text = tk.Text(instructions_frame, wrap=tk.WORD, height=10, width=30)
    instructions_text.pack(padx=10, pady=10)

    variables_text = tk.Text(variables_frame, wrap=tk.WORD, height=10, width=30)
    variables_text.pack(padx=10, pady=10)

    registers_text = tk.Text(registers_frame, wrap=tk.WORD, height=10, width=30)
    registers_text.pack(padx=10, pady=10)
    for register in ["T0", "T1", "T2", "T3"]:
        value = simulator.variables.get(register)
        registers_text.insert(tk.END, f"{register}: {value}\n")

    stack_text = tk.Text(stack_frame, wrap=tk.WORD, height=10, width=30)
    stack_text.pack(padx=10, pady=10)

    def update_text():
        # Clear the existing content of the Text widgets
        instructions_text.delete('1.0', tk.END)
        variables_text.delete('1.0', tk.END)
        registers_text.delete('1.0', tk.END)
        stack_text.delete('1.0', tk.END)

        # update instructions
        for i in code_lines:
            instructions_text.insert(tk.END, i + "\n")

        # update registers
        for register in ["T0", "T1", "T2", "T3"]:
            value = simulator.variables.get(register)
            registers_text.insert(tk.END, f"{register}: {value}\n")

        # update variables
        for i in data_lines:
            variables_text.insert(tk.END, f"{i}\n")

        # update stack
        for i in range(simulator.SP - 1, -1, -1):
            value = simulator.variables["Stack"]
            stack_text.insert(tk.END, f"{value} ")

        # update filename
        filename_label.configure(text="File name: " + filename)

        # update intruction
        if simulator.program_counter.pc != len(code_lines) - 1:
            instructions_label.configure(text="Next instruction: " + code_lines[simulator.program_counter.pc])
        else:
            instructions_label.configure(text="Next instruction: Program completed")

    def load_file_button_click():
        nonlocal data_lines, code_lines, filename
        file_path = filedialog.askopenfilename(
            filetypes=[("Assembly files", "*.asm"), ("All files", "*.*")])
        filename = os.path.basename(file_path)

        if file_path:
            simulator = Simulator()
            data_lines, code_lines = simulator.load_program(file_path)
            update_text()

    def on_run_click():
        for i in code_lines:
            simulator.execute_program(data_lines, code_lines, i)
            simulator.program_counter.pc = len(code_lines) - 1
            update_text()

    def on_step_click():
        if simulator.program_counter.pc < len(code_lines):
            line = code_lines[simulator.program_counter.pc]
            simulator.execute_program(data_lines, code_lines, line)
            update_text()
            simulator.program_counter.next()
        else:
            print("Programme terminé")


    load_button = ttk.Button(root, text="Load File", command=load_file_button_click)
    load_button.grid(row=2, column=1, padx=10, pady=10)

    run_button = ttk.Button(root, text="Run", command=on_run_click)
    run_button.grid(row=3, column=1, pady=10)

    step_button = ttk.Button(root, text="Step", command=on_step_click)
    step_button.grid(row=4, column=1, pady=10)

    root.mainloop()


if __name__ == "__main__":
    gui()
