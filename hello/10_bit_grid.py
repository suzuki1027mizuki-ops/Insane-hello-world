# 10. 真理値ビットマップ
#
# 空リストは偽、空でないリストは真。それを 0 と 1 として 8 ビットの格子を描く。
# 復号では整数の足し算すら使わず、ミュータブルなリストを
#   「自分自身で伸ばす (acc += acc) = 2 倍」
#   「1 個追加する = +1」
# だけで育て、最後に len() で長さを測る。

O = []
I = [O]

grid = [
    [O, I, I, O, I, O, O, O],  # h
    [O, I, I, O, O, I, O, I],  # e
    [O, I, I, O, I, I, O, O],  # l
    [O, I, I, O, I, I, O, O],  # l
    [O, I, I, O, I, I, I, I],  # o
    [O, O, I, O, O, O, O, O],  # (空白)
    [O, I, I, I, O, I, I, I],  # w
    [O, I, I, O, I, I, I, I],  # o
    [O, I, I, I, O, O, I, O],  # r
    [O, I, I, O, I, I, O, O],  # l
    [O, I, I, O, O, I, O, O],  # d
]


def byte(row):
    acc = []
    for bit in row:
        acc += acc
        if bit:
            acc.append(bit)
    return len(acc)


print(bytearray(map(byte, grid)).decode())
