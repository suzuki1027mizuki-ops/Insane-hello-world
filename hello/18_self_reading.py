# 18. 自分自身のソースを読む
#
# コメントはリテラルではない。だからこのファイルの最終行のコメントに答えを書いておき、
# 実行時に自分自身を開いて読み出す。
#
# open() のモード "rb" すら手書きしない:
#   bytearray.replace の頭文字 -> r
#   bytearray         の頭文字 -> b
# 読み込んだ中身は bytearray に入れ、splitlines / split もミュータブルなまま行う。

[r, *_] = bytearray.replace.__name__
[b, *_] = bytearray.__name__

with open(__file__, bytearray().decode().join([r, b])) as me:
    source = bytearray(me.read())

[*_, last_line] = source.splitlines()
[_, *words] = last_line.split()
print(*[word.decode() for word in words])

# hello world
