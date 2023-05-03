import ALU

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

# Print #DATA Section
print(data_lines)
# Print #CODE Section
print(code_lines)

# Execute #DATA section
print("\n#DATA section translated:")
variables = {}
for line in data_lines:
    # Split the line into variable name and initial value
    parts = line.split()
    var_name = parts[0]
    var_value = int(parts[1])

    # Dynamically create a variable with the given name and initial value
    globals()[var_name] = var_value
    print(var_name, " = ", var_value)

# Registers creation
T0 = T1 = T2 = T3 = 0


def execute_instruction(instruction, arguments):
    # Dictionary of instruction
    switcher = {
        "LDA": ALU.LDA,
        "STR": ALU.STR,
        "PUSH": ALU.PUSH,
        "AND": ALU.AND,
        "OR": ALU.OR,
        "NOT": ALU.NOT,
        "ADD": ALU.ADD,
        "SUB": ALU.SUB,
        "DIV": ALU.DIV,
        "MUL": ALU.MUL,
        "MOD": ALU.MOD,
        "INC": ALU.INC,
        "DEC": ALU.DEC,
        "BEQ": ALU.BEQ,
        "BNE": ALU.BNE,
        "BBG": ALU.BBG,
        "BSM": ALU.BSM,
        "JMP": ALU.JMP,
        "HLT": ALU.HLT
    }
    # Get the function from the switcher dictionary
    func = switcher.get(instruction)
    print(func)
    # Call the function with the arguments
    if instruction == "HLT":
        func(*arguments)
    else:
        arguments[0] = func(*arguments)

print("\n#CODE section result:")
print(code_lines)
# Execute #CODE section
for line in code_lines:
    # Separate the instruction from its arguments
    parts = line.split(" ")
    instruction = parts[0]
    args = parts[1:]  # args is a tab of arguments
    # Execute the instruction with its arguments
    execute_instruction(instruction, args)

print("T0 = ", T0, " | T1 = ", T1, "T2 = ", T2, " | T3 = ", T3,"| RES = ", RES)  # don't worry RES is initialized line 49