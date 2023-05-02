filename = "example1.asm"

with open("asm-examples/"+filename, "r") as f:

    for line in f:
        # Remove comments (filter)
        parts = line.split("!", 1)
        filtered_line = parts[0].strip()
        if filtered_line:
            # Print the code without comments
            print(filtered_line)
