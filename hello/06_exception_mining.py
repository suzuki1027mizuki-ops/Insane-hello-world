# 06. 例外メッセージの採掘
#
# ミュータブルなオブジェクトにわざと無茶をさせて、インタプリタに文句を言わせる。
# そのエラーメッセージ (実行時に生まれた文字列) から必要な文字を掘り出す。
#
#   [][0]            -> IndexError: list index out of range
#   {[]}             -> TypeError: unhashable type: 'list'
#   [[], {}].sort()  -> TypeError: '<' not supported between instances of 'dict' and 'list'
#
# Python 3.14 から unhashable のメッセージは少し長くなったが、
# 後ろから数えれば同じ場所に "h" がいる。


def complain(deed):
    try:
        deed()
    except Exception as oops:
        [message] = oops.args
        return message


# "list index out of range" — l, 空白, d, e, o, r をまとめて掘る
[l, _, _, _, space, _, _, d, e, _, _, o, *_, r, _, _, _, _] = complain(lambda: [][len([])])

# "...unhashable type: 'list'..." — unhashable の後ろから 5 文字目が h
[*_, unhashable, _, _] = complain(lambda: {[]}).split()
[*_, h, _, _, _, _] = unhashable

# "'<' not supported between instances of ..." — between の 4 文字目が w
[_, _, _, between, *_] = complain(lambda: [[], {}].sort()).split()
[_, _, _, w, *_] = between

print(bytearray().decode().join([h, e, l, l, o, space, w, o, r, l, d]))
