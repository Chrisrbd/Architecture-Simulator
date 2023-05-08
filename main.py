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


def func_and(reg1, reg2):
    print("AND:", reg1, "=", reg1, "and", reg2)
    variables[reg1] = variables[reg1] and variables[reg2]


def func_or(reg1, reg2):
    print("OR:", reg1, "=", reg1, "or", reg2)
    variables[reg1] = variables[reg1] or variables[reg2]


def func_not(reg):
    print("NOT:", reg, "= not", reg)
    variables[reg] = not variables[reg]


def func_add(x, y):
    print("ADD: ", x, "=", x, "+", y)
    variables[x] += variables[y]


def func_sub(reg1, reg2):
    print("SUB:", reg1, "=", reg1, "-", reg2)
    variables[reg1] -= variables[reg2]


def func_div(reg1, reg2):
    print("DIV:", reg1, "=", reg1, "/", reg2)
    variables[reg1] /= variables[reg2]


def func_mul(reg1, reg2):
    print("MUL:", reg1, "=", reg1, "*", reg2)
    variables[reg1] *= variables[reg2]


def func_mod(reg1, reg2):
    print("MOD:", reg1, "=", reg1, "%", reg2)
    variables[reg1] %= variables[reg2]


def func_inc(reg):
    print("INC:", reg, "=", reg, "+ 1")
    variables[reg] += 1


def func_dec(reg):
    print("DEC:", reg, "=", reg, "- 1")
    variables[reg] -= 1


def func_beq(reg1, reg2, address):
    if variables[reg1] == variables[reg2]:
        func_jmp(address)


def func_bne(reg1, reg2, address):
    if variables[reg1] != variables[reg2]:
        func_jmp(address)


def func_bgg(reg1, reg2, address):
    if variables[reg1] > variables[reg2]:
        func_jmp(address)


def func_bsm(reg1, reg2, address):
    if variables[reg1] < variables[reg2]:
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
# 2 shared memories, one to store the data and another to store the code
data_lines = []
code_lines = []

# Creation of the stack + stack pointer to follow the current position in the stack
stack = [0] * 4096
SP = 0  # Stack pointer initialized to 0

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

variables = {"T0": 0, "T1": 0, "T2": 0, "T3": 0, "Stack": stack[SP]}  # Stack is the last element in the Stack

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
        "POP": func_pop,
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
        "HLT": func_hlt,
        "SRL": func_srl,
        "SRR": func_srr
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

# Conversion of registers to bin
for key in variables:
    if key.startswith("T"):
        decimal_value = variables[key]
        binary_value = bin(decimal_value)[2:]  # Convert to binary and remove the "0b" prefix
        variables[key] = binary_value

print(variables)
