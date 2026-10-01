# 04. 継承チェーン (MRO) で綴る
#
# 1 文字 = 1 クラス。単一継承の鎖を作ると、最も派生したクラスの __mro__ は
# 「自分 → 親 → 祖父 → … → object」の順に並ぶ。
# それを逆順にして object を捨てれば、祖先から順に単語が読める。
#
# 同じ名前のクラスを 2 回定義しても問題ない (class l(l) は直前の l を継承する)。
# だから "ll" も綴れる。


def spell(youngest):
    lineage = [*youngest.__mro__]
    lineage.pop()  # 最後の object を捨てる
    lineage.reverse()  # 祖先から順に
    return bytearray().decode().join([ancestor.__name__ for ancestor in lineage])


class h:
    pass


class e(h):
    pass


class l(e):
    pass


class l(l):
    pass


class o(l):
    pass


hello = o


class w:
    pass


class o(w):
    pass


class r(o):
    pass


class l(r):
    pass


class d(l):
    pass


world = d

print(spell(hello), spell(world))
