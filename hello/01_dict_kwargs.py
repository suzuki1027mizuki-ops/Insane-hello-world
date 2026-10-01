# 01. dict のキーワード引数
#
# 文字列リテラルは一切書かない。キーワード引数の「名前」は識別子であって
# リテラルではないが、dict に入った瞬間にキー (実行時に生まれた文字列) になる。
# 値はすべて空のミュータブル (list / dict / set / bytearray)。

greeting = {}
greeting.update(hello=[])
greeting.update(world=bytearray())

# dict をアンパックするとキーが順番どおりに出てくる (挿入順は保証されている)
print(*greeting)
