# 05. メソッド名の考古学
#
# ミュータブルな組み込み型 (bytearray / dict) のメソッド名や型名は、
# 実行時に取り出せる文字列だ。それを分割代入で 1 文字ずつ発掘する。
#
#   bytearray.hex   -> h e x
#   bytearray.lower -> l o w e r
#   dict            -> d i c t
#
# 結合には空文字列が必要だが、それすら「空の bytearray を decode したもの」で作る。

[h, e, _] = bytearray.hex.__name__
[l, o, w, _, r] = bytearray.lower.__name__
[d, *_] = dict.__name__

nothing = bytearray().decode()
print(nothing.join([h, e, l, l, o]), nothing.join([w, o, r, l, d]))
