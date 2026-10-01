# 17. Brainfuck 仮想機械
#
# 命令 + - > < . [ ] をそれぞれ Python の関数 (= ミュータブルなオブジェクト) で表し、
# プログラムは「関数への参照を並べたリスト」として書く。文字列のソースコードは存在しない。
# テープは bytearray、出力先も bytearray。
#
# 元の Brainfuck:
#   ++++++++++[>++++++++++>+++>++++++++++++<<<-]
#   >++++.---.+++++++..+++.>++.>-.<<.+++.------.--------.

zero = len([])
one = len([[]])


def P(vm):  # +
    vm.tape[vm.ptr] += one


def M(vm):  # -
    vm.tape[vm.ptr] -= one


def R(vm):  # >
    vm.ptr += one


def L(vm):  # <
    vm.ptr -= one


def W(vm):  # .
    vm.out.append(vm.tape[vm.ptr])


def B(vm):  # [
    if not vm.tape[vm.ptr]:
        vm.pc = vm.jump[vm.pc]


def E(vm):  # ]
    if vm.tape[vm.ptr]:
        vm.pc = vm.jump[vm.pc]


program = [
    P, P, P, P, P, P, P, P, P, P,
    B, R, P, P, P, P, P, P, P, P, P, P,
    R, P, P, P,
    R, P, P, P, P, P, P, P, P, P, P, P, P,
    L, L, L, M, E,
    R, P, P, P, P, W,  # h
    M, M, M, W,  # e
    P, P, P, P, P, P, P, W, W,  # l l
    P, P, P, W,  # o
    R, P, P, W,  # (空白)
    R, M, W,  # w
    L, L, W,  # o
    P, P, P, W,  # r
    M, M, M, M, M, M, W,  # l
    M, M, M, M, M, M, M, M, W,  # d
]


class Machine:
    def __init__(self, code):
        self.code = code
        self.tape = bytearray(len(code))
        self.out = bytearray()
        self.ptr = zero
        self.pc = zero
        self.jump = {}
        pending = []
        here = zero
        for op in code:
            if op is B:
                pending.append(here)
            if op is E:
                there = pending.pop()
                self.jump[here] = there
                self.jump[there] = here
            here += one

    def run(self):
        while self.pc < len(self.code):
            self.code[self.pc](self)
            self.pc += one
        return self.out


print(Machine(program).run().decode())
