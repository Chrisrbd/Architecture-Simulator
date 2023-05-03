def func_lda(x, y):
    if y.isdigit():
        # If y is a number
        data_vars[x] = int(y)
    elif y in data_vars:
        # If y is a variable
        data_vars[x] = data_vars[y]
    else:
        raise ValueError(f"Variable {y} not found in data_vars")


def func_add(x, y):
    if y in data_vars:
        # If y is a variable
        y_value = data_vars[y]
    else:
        y_value = int(y)
    data_vars[x] += y_value


def func_str(x, y):
    if y.isdigit():
        # If y is a number
        data_vars[x] = int(y)
    elif x.startswith("T"):
        # If y is a register
        print("Error: Register stores are not allowed.")
    else:
        # If y is a variable
        data_vars[x] = data_vars[y]


filename = "example1.asm"
data_vars = {"T0": 0, "T1": 0, "T2": 0, "T3": 0}
code_lines = []

with open("asm-examples/"+filename) as f:
    for line in f:
        # Remove comments (filter)
        parts = line.split("!", 1)
        filtered_line = parts[0].strip()
        if filtered_line:
            # Append the filtered line to the list of code lines
            code_lines.append(filtered_line)

for i in range(len(code_lines)):
    line = code_lines[i]
    if "#DATA" in line:
        for j in range(i + 1, len(code_lines)):
            var_line = code_lines[j].split()
            if len(var_line) >= 2:
                var_name = var_line[0]
                var_value = int(var_line[1])
                data_vars[var_name] = var_value
            else:
                print("Initial data values :")
                print(data_vars)
                print("")
                break
    elif "#CODE" in line:
        for j in range(i + 1, len(code_lines)):
            instr_line = code_lines[j].split()
            instr_name = instr_line[0]

            if len(instr_line) >= 2:
                if instr_name == "gerg":
                    print("salut")

            if len(instr_line) >= 3:
                operand1 = instr_line[1]
                operand2 = instr_line[2]
                if instr_name == "LDA":
                    func_lda(operand1, operand2)
                    print("LDA : " + operand1 + " ← " + operand2)
                    print(data_vars)
                    print("")
                if instr_name == "ADD":
                    func_add(operand1, operand2)
                    print("ADD : " + operand1 + " ← " + operand1 + " + " + operand2)
                    print(data_vars)
                    print("")
                if instr_name == "STR":
                    func_str(operand1, operand2)
                    print("STR : " + operand1 + " ← " + operand1 + " + " + operand2)
                    print(data_vars)
                    print("")

## Voici la syntaxe pour les dictionnaires
## print(data_vars["A"])
## print("A =" + str(data_vars["A"]))
