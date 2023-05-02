import ALU

filename = "example1.asm"
data_lines = []
code_lines = []

with open("asm-examples/"+filename, "r") as file:

    is_data_section = False
    is_code_section = False

    for line in file:
        # Remove comments and store the filtered code in filtered_lines
        parts = line.split("!", 1)
        filtered_lines = parts[0].strip()

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

print(data_lines)
print(code_lines)