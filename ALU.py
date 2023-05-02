def LDA(reg1, reg2):
    reg1 = reg2


def STR(var, reg):
    var = reg


def PUSH(reg, var):
    reg = var


def AND(reg1, reg2):
    reg1 = reg1 and reg2


def OR(reg1, reg2):
    reg1 = reg1 or reg2


def NOT(reg):
    reg = not reg


def ADD(reg1, reg2):
    reg1 += reg2


def SUB(reg1, reg2):
    reg1 -= reg2


def DIV(reg1, reg2):
    reg1 = reg1 / reg2


def MUL(reg1, reg2):
    reg1 = reg1 * reg2


def MOD(reg1, reg2):
    reg1 = reg1 % reg2


def INC(reg):
    reg += 1


def DEC(reg):
    reg -= 1


def BEQ(reg1, reg2, address):
    if reg1 == reg2:
        JMP(address)


def BNE(reg1, reg2, address):
    if reg1 != reg2:
        JMP(address)


def BBG(reg1, reg2, address):
    if reg1 > reg2:
        JMP(address)


def BSM(reg1, reg2, address):
    if reg1 < reg2:
        JMP(address)


def JMP(address):
    # set program counter to address
    pass


def HLT():
    # stop execution
    pass
