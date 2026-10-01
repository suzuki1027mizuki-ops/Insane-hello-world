# 11. 集合代数
#
# Atom は中身のない (でも属性を生やせる) ミュータブルなオブジェクト。
# 同一性でハッシュされるので、作るたびに「別の原子」になる。
#
# 7 つの「ビット原子」b0〜b6 に、それぞれ 2**i 個の新品原子からなる「重さ」を持たせる。
# 文字はビット原子の集合として表し、文字同士は 和 | ・差 - ・対称差 ^ で導出する。
# 最後に、含まれるビットの重さを全部合併した集合の濃度 (len) が文字コードになる。


class Atom:
    pass


def fresh(pattern):
    return {Atom() for _ in pattern}


bits = [Atom(), Atom(), Atom(), Atom(), Atom(), Atom(), Atom()]
[b0, b1, b2, b3, b4, b5, b6] = bits

weight = {}
grain = {Atom()}
for bit in bits:
    weight[bit] = grain
    grain = fresh(grain) | fresh(grain)  # 次のビットは 2 倍の、しかも全部新品の原子

h = {b6, b5, b3}
e = {b6, b5, b2, b0}
l = h | {b2}
o = l | {b1, b0}
space = {b5}
w = o ^ {b4, b3}
r = w - {b2, b0}
d = e - {b0}


def weigh(letter):
    mass = set()
    for bit in letter:
        mass |= weight[bit]
    return len(mass)


print(bytearray(map(weigh, [h, e, l, l, o, space, w, o, r, l, d])).decode())
