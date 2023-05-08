import tkinter as tk

def func_lda(reg, y):
    print("LDA:", reg, "<--", y)
    if reg in list(variables)[0:3]:
        if y.isdigit():
            # If y is a number
            variables[reg] = int(y)
        elif y in variables:
            # If y is a variable
            variables[reg] = variables[y]
        else:
            raise ValueError(y, " must be an integer")
    else:
        print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")


def func_str(var, y):
    print("STR:", var, "<--", y)
    if var in list(variables)[0:3]:
        # If y is a register
        print("Error: Register stores are NOT ALLOWED.")
    if y.isdigit():
        # If y is a number
        variables[var] = int(y)
    else:
        # If y is a variable
        variables[var] = variables[y]


def func_push(var):
    print("PUSH: stack <--", var)
    global SP, stack
    if var.isdigit():
        # If y is a number
        stack[SP] = int(var)
    else:
        # If y is a variable
        stack[SP] = variables[var]
    SP += 1


def func_pop(var):
    global SP, stack
    if var in list(variables)[0:3]:
        # If y is a register
        SP -= 1
        variables[var] = stack[SP]
        print("POP:", var, " <-- stack")
    else:
        print("Error: Storing in a memory region is NOT ALLOWED.")


def func_and(reg1, var):
    print("AND:", reg1, "=", reg1, "and", var)
    if reg1 in list(variables)[0:3]:
        if var in variables:
            variables[reg1] = variables[reg1] and variables[var]
        elif var.isdigit():
            variables[reg1] = variables[reg1] and int(var)
        else:
            print(f"Error: {var} is not a valid register, variable, or constant")
    else:
        print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")


def func_or(reg1, var):
    print("OR:", reg1, "=", reg1, "or", var)
    if reg1 in list(variables)[0:3]:
        if var in variables:
            variables[reg1] = variables[reg1] or variables[var]
        elif var.isdigit():
            variables[reg1] = variables[reg1] or int(var)
        else:
            print(f"Error: {var} is not a valid register, variable, or constant")
    else:
        print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")


def func_not(reg):
    print("NOT:", reg, "= not", reg)
    if reg in list(variables)[0:3]:
        variables[reg] = not variables[reg]
    else:
        print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")


def func_add(reg, var):
    print("ADD:", reg, "=", reg, "+", var)
    if reg in list(variables)[0:3]:
        if var in variables:
            variables[reg] += variables[var]
        elif var.isdigit():
            variables[reg] += int(var)
        else:
            print(f"Error: {var} is not a valid register, variable, or constant")
    else:
        print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")


def func_sub(reg, var):
    print("SUB:", reg, "=", var, "-", reg)
    if reg in list(variables)[0:3]:
        if var in variables:
            variables[reg] = variables[var] - variables[reg]
        elif var.isdigit():
            variables[reg] = int(var) - variables[reg]
        else:
            print(f"Error: {var} is not a valid register, variable, or constant")
    else:
        print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")


def func_div(reg, var):
    print("DIV:", reg, "=", reg, "/", var)
    if reg in list(variables)[0:3]:
        if var == 0:
            print("Error: Division by zero")
        elif var in variables:
            variables[reg] //= variables[var]
        elif var.isdigit():
            variables[reg] //= int(var)
        else:
            print(f"Error: {var} is not a valid register, variable, or constant")
    else:
        print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")


def func_mul(reg, var):
    print("MUL:", reg, "=", reg, "*", var)
    if reg in list(variables)[0:3]:
        if var in variables:
            variables[reg] *= variables[var]
        elif var.isdigit():
            variables[reg] *= int(var)
        else:
            print(f"Error: {var} is not a valid register, variable, or constant")
    else:
        print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")


def func_mod(reg, var):
    if variables[var] == 0:
        raise ZeroDivisionError("Modulo by zero")
    print("MOD:", reg, "=", reg, "%", var)
    if reg in list(variables)[0:3]:
        if var in variables:
            variables[reg] = variables[reg] % variables[var]
        elif var.isdigit():
            variables[reg] = variables[reg] % int(var)
        else:
            print(f"Error: {var} is not a valid register, variable, or constant")
    else:
        print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")


def func_inc(reg):
    print("INC:", reg, "=", reg, "+ 1")
    if reg in list(variables)[0:3]:
        variables[reg] += 1
    else:
        print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")


def func_dec(reg):
    print("DEC:", reg, "=", reg, "- 1")
    if reg in list(variables)[0:3]:
        if variables[reg] == 0:
            raise ValueError("Cannot decrement register that already contains zero")
        else:
            variables[reg] -= 1
    else:
        print("Error: Memory regions loads are NOT ALLOWED. (Only registers)")


def func_beq(reg1, reg2, address):
    if reg1 & reg2 in variables:
        if variables[reg1] == variables[reg2]:
            func_jmp(address)
    elif reg1 in variables:
        if variables[reg1] == reg2:
            func_jmp(address)
    elif reg2 in variables:
        if reg1 == variables[reg2]:
            func_jmp(address)
    else:
        if reg1 == reg2:
            func_jmp(address)


def func_bne(reg1, reg2, address):
    if reg1 & reg2 in variables:
        if variables[reg1] != variables[reg2]:
            func_jmp(address)
    elif reg1 in variables:
        if variables[reg1] != reg2:
            func_jmp(address)
    elif reg2 in variables:
        if reg1 != variables[reg2]:
            func_jmp(address)
    else:
        if reg1 != reg2:
            func_jmp(address)



def func_bgg(reg1, reg2, address):
    if reg1 & reg2 in variables:
        if variables[reg1] > variables[reg2]:
            func_jmp(address)
    elif reg1 in variables:
        if variables[reg1] > reg2:
            func_jmp(address)
    elif reg2 in variables:
        if reg1 > variables[reg2]:
            func_jmp(address)
    else:
        if reg1 > reg2:
            func_jmp(address)


def func_bsm(reg1, reg2, address):
    if reg1 & reg2 in variables:
        if variables[reg1] < variables[reg2]:
            func_jmp(address)
    elif reg1 in variables:
        if variables[reg1] < reg2:
            func_jmp(address)
    elif reg2 in variables:
        if reg1 < variables[reg2]:
            func_jmp(address)
    else:
        if reg1 < reg2:
            func_jmp(address)


def func_jmp(address):
    # set program counter to address
    pass


def func_hlt():
    print("HLT: end the program execution!")
    # stop execution
    pass


def func_srl(reg, const):
    print("SRL:", reg, "=", reg, ">>", const)
    variables[reg] = variables[reg] // (2 ** int(const))


def func_srr(reg, const):
    print("SRR:", reg, "=", reg, "<<", const)
    variables[reg] = variables[reg] * (2 ** int(const))


filename = "example1.asm"
data_lines = []
code_lines = []

# Store from the .asm file the #DATA section lines and #CODE section lines in different tabs
with open("asm-examples/" + filename, "r") as file:
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

variables = {"T0": 0, "T1": 0, "T2": 0, "T3": 0}

# Execute #DATA section
print("\n#DATA section translated:")
print(data_lines, "\n")
for line in data_lines:
    # Split the line into variable name and initial value
    parts = line.split()
    var_name = parts[0]
    var_value = int(parts[1])

    # Dynamically create a variable with the given name and initial value
    variables[var_name] = var_value
    print(var_name, " = ", var_value)
print()
print(variables)


def execute_instruction(instruction, arguments):
    # Dictionary of instruction
    instructions = {
        "LDA": func_lda,
        "STR": func_str,
        "PUSH": func_push,
        "AND": func_and,
        "OR": func_or,
        "NOT": func_not,
        "ADD": func_add,
        "SUB": func_sub,
        "DIV": func_div,
        "MUL": func_mul,
        "MOD": func_mod,
        "INC": func_inc,
        "DEC": func_dec,
        "BEQ": func_beq,
        "BNE": func_bne,
        "BBG": func_bgg,
        "BSM": func_bsm,
        "JMP": func_jmp,
        "HLT": func_hlt
    }
    # Get the function from the switcher dictionary
    func = instructions.get(instruction)
    # Call the function with the arguments
    func(*arguments)


print("\n#CODE section result:")
print(code_lines, "\n")
# Execute #CODE section
for line in code_lines:
    # Separate the instruction from its arguments
    parts = line.split(" ")
    instruction = parts[0]
    args = parts[1:]
    # Execute the instruction with its arguments
    execute_instruction(instruction, args)
    t0_label = tk.Label(text="T0 = " + str(variables["T0"]))
    t0_label.pack()
    t1_label = tk.Label(text="T1 = " + str(variables["T1"]))
    t1_label.pack()
    t2_label = tk.Label(text="T2 = " + str(variables["T2"]))
    t2_label.pack()
    t3_label = tk.Label(text="T3 = " + str(variables["T3"]))
    t3_label.pack()

print(variables)


class App:

    def __init__(self, master):
        self.master = master
        master.title("Hello World")
        self.index = 0

        self.button = tk.Button(master, text="Next", command=self.next_element)
        self.button.pack()

        self.t0_value = 0
        self.t1_value = 0
        self.t2_value = 0
        self.t3_value = 0

        self.label = tk.Label(master, text="Registers :")
        self.label.pack()
        self.t0_label = tk.Label(master, text="T0 = " + str(variables["T0"]))
        self.t0_label.pack()
        self.t1_label = tk.Label(master, text="T1 = " + str(variables["T1"]))
        self.t1_label.pack()
        self.t2_label = tk.Label(master, text="T2 = " + str(variables["T2"]))
        self.t2_label.pack()
        self.t3_label = tk.Label(master, text="T3 = " + str(variables["T3"]))
        self.t3_label.pack()

        self.label = tk.Label(master, text="Variables :")
        self.label.pack()

        self.frame = tk.Frame(master)
        self.frame.pack()

    def next_element(self):
        if self.index < len(data_lines):
            element = data_lines[self.index].split()
            label_text = element[0] + " = " + element[1]
            tk.Label(self.frame, text=label_text).pack()
            self.index += 1


root = tk.Tk()
root.geometry("400x400")
app = App(root)
root.mainloop()


