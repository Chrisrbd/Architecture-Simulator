def LDA(reg1, reg2):
    reg1 = reg2
    return reg1


def STR(var, reg):
    var = reg
    return var

def PUSH(reg, var):
    reg = var
    return reg

def AND(reg1, reg2):
    reg1 = reg1 and reg2
    return reg1

def OR(reg1, reg2):
    reg1 = reg1 or reg2
    return reg1

def NOT(reg):
    reg = not reg
    return reg

def ADD(reg1, reg2):
    reg1 += reg2
    return reg1

def SUB(reg1, reg2):
    reg1 -= reg2


def DIV(reg1, reg2):
    reg1 = reg1 / reg2
    return reg1

def MUL(reg1, reg2):
    reg1 = reg1 * reg2
    return reg1

def MOD(reg1, reg2):
    reg1 = reg1 % reg2
    return reg1

def INC(reg):
    reg += 1
    return reg

def DEC(reg):
    reg -= 1
    return reg

def BEQ(reg1, reg2, address):
    if reg1 == reg2:
        JMP(address)
    return reg1

def BNE(reg1, reg2, address):
    if reg1 != reg2:
        JMP(address)
    return reg1

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
