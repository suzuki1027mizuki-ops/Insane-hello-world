# 12. ペアノ算術 (入れ子リスト)
#
#   0      = []
#   n の次 = [n]
#
# 自然数を「リストの入れ子の深さ」で表し、足し算と掛け算を再帰で定義する。
#   a + 0 = a          a + S(b) = S(a + b)
#   a * 0 = 0          a * S(b) = a * b + a
# 文字コードは 100 + 4 のような式で組み立て、最後に深さを数えて取り出す。


def succ(n):
    return [n]


def add(a, b):
    if not b:
        return a
    [pred] = b
    return succ(add(a, pred))


def mul(a, b):
    if not b:
        return []
    [pred] = b
    return add(mul(a, pred), a)


def depth(n):
    trail = []
    while n:
        [n] = n
        trail.append(n)
    return len(trail)


zero = []
one = succ(zero)
two = succ(one)
three = succ(two)
four = succ(three)
five = succ(four)
eight = mul(two, four)
nine = succ(eight)
ten = mul(two, five)
hundred = mul(ten, ten)

h = add(hundred, four)
e = add(hundred, one)
l = add(hundred, eight)
o = add(hundred, add(ten, one))
space = mul(mul(four, four), two)
w = add(hundred, add(ten, nine))
r = add(hundred, add(ten, four))
d = hundred

print(bytearray(map(depth, [h, e, l, l, o, space, w, o, r, l, d])).decode())
