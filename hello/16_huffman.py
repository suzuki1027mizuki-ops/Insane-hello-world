# 16. ハフマン符号の復号
#
# 出現頻度 (l:3, o:2, その他:1) から作ったハフマン木を、入れ子のリストで持つ。
# 葉は 1 文字ずつのクラス (名前がそのまま文字になる)。gap は単語の区切り。
#
#                 *
#           /           \
#         *               *
#       /   \           /   \
#     *       o       l       *
#    / \                    /   \
#   d  gap                *       *
#                        / \     / \
#                       h   e   w   r
#
# 左 = O (空リスト = 偽), 右 = I (中身のあるリスト = 真)。
# ビット列を先頭から辿り、葉に着いたら根に戻る。


class h:
    pass


class e:
    pass


class l:
    pass


class o:
    pass


class w:
    pass


class r:
    pass


class d:
    pass


class gap:
    pass


tree = [[[d, gap], o], [l, [[h, e], [w, r]]]]

O = []
I = [O]

stream = [
    I, I, O, O,  # h
    I, I, O, I,  # e
    I, O,  # l
    I, O,  # l
    O, I,  # o
    O, O, I,  # gap
    I, I, I, O,  # w
    O, I,  # o
    I, I, I, I,  # r
    I, O,  # l
    O, O, O,  # d
]

word = []
words = [word]
node = tree
for bit in stream:
    [left, right] = node
    node = right if bit else left
    if isinstance(node, list):
        continue
    if node is gap:
        word = []
        words.append(word)
    else:
        word.append(node.__name__)
    node = tree

print(*[bytearray().decode().join(letters) for letters in words])
