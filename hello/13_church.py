# 13. チャーチ数 (ラムダ計算)
#
# 数 n を「関数 f を n 回適用する関数」で表す。関数オブジェクトもミュータブルだ
# (属性を自由に生やせる)。
# 評価するときは「空のリストに 1 個追記する」という副作用を n 回起こしてもらい、
# リストの長さを測る。

zero = lambda f: lambda x: x
succ = lambda n: lambda f: lambda x: f(n(f)(x))
plus = lambda m: lambda n: lambda f: lambda x: m(f)(n(f)(x))
times = lambda m: lambda n: lambda f: m(n(f))
power = lambda m: lambda n: n(m)


def stroke(pile):
    pile.append([])
    return pile


def tally(n):
    return len(n(stroke)([]))


one = succ(zero)
two = succ(one)
four = times(two)(two)
five = succ(four)
ten = times(two)(five)
hundred = power(ten)(two)

h = plus(hundred)(four)
e = succ(hundred)
l = plus(hundred)(times(two)(four))
o = plus(hundred)(succ(ten))
space = power(two)(five)
w = plus(hundred)(plus(ten)(plus(five)(four)))
r = plus(hundred)(plus(ten)(four))
d = hundred

print(bytearray(map(tally, [h, e, l, l, o, space, w, o, r, l, d])).decode())
