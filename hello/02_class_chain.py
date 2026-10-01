# 02. クラスオブジェクトの連結リスト
#
# クラスはミュータブルなオブジェクトなので、定義した後から属性を生やせる。
# クラスそのものを「ノード」にして連結リストを組み、__name__ を辿って読む。


class hello:
    pass


class world:
    pass


# クラスに後から next を生やして鎖をつなぐ。終端は空リスト (偽)
hello.next = world
world.next = []

words = []
node = hello
while node:
    words.append(node.__name__)
    node = node.next

print(*words)
