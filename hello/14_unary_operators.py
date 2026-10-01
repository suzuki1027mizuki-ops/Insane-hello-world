# 14. 単項演算子だけの DSL
#
# Ink は 3 つの単項演算子を乗っ取ったミュータブルなオブジェクト。
#   +ink  … 筆に 1 滴足す   (+1)
#   -ink  … 筆の墨を倍にする (×2)
#   ~ink  … 紙に 1 文字書いて筆を洗う
# 単項演算子は右から左へ評価されるので、各行は右端から読む。
# たとえば h (104 = 0b1101000) は
#   + - + - - + - - -  (適用順)  →  1 2 3 6 12 13 26 52 104
# これを左右反転して書いたのが ~---+--+-+ink である。


class Ink:
    def __init__(self):
        self.brush = []
        self.paper = bytearray()

    def __pos__(self):
        self.brush.append([])
        return self

    def __neg__(self):
        self.brush += self.brush
        return self

    def __invert__(self):
        self.paper.append(len(self.brush))
        self.brush.clear()
        return self

    def __str__(self):
        return self.paper.decode()


ink = Ink()

~---+--+-+ink  # h
~+--+---+-+ink  # e
~--+-+--+-+ink  # l
~--+-+--+-+ink  # l
~+-+-+-+--+-+ink  # o
~-----+ink  # (空白)
~+-+-+--+-+-+ink  # w
~+-+-+-+--+-+ink  # o
~-+---+-+-+ink  # r
~--+-+--+-+ink  # l
~--+---+-+ink  # d

print(ink)
