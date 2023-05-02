t0, t1, t2, t3 = 500, 0, 0, 0
filename = "input2.asm"

with open("asm-examples/"+filename, "r") as f:
    lines = f.readlines()

for i in range(len(lines)):
    line = lines[i]
    if "#DATA" in line:
        for j in range(i + 1, len(lines)):
            var_line = lines[j].split()
            if len(var_line) >= 2:
                var_name = var_line[0]
                var_value = int(var_line[1])
                locals()[var_name] = var_value
            else:
                break


def add(x, y):
    x = x + y
    return x

print(t0)
print(laptop)
print(add(t0, laptop))
