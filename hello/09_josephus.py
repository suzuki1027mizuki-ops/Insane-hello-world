# 09. ヨセフス問題で並べ替える
#
# 11 人 (= 11 文字) を円形に並べ、3 人目ごとに輪から外していく。
# 外れた順に並べると "hello_world" になるよう、あらかじめ逆算して並べた円が
#
#     l l h w o e d r l _ o
#
# これをクラス名として持ち込み、ミュータブルなリストの回転 (pop と append) だけで
# 処刑を実行する。最後に "_" (list.__len__ という名前から拝借) で単語に分ける。

zero = len([])
skip = [[], []]  # 2 人飛ばして 3 人目


class llhwoedrl_o:
    pass


circle = [*llhwoedrl_o.__name__]
fallen = []
while circle:
    for _ in skip:
        circle.append(circle.pop(zero))
    fallen.append(circle.pop(zero))

[underscore, *_] = list.__len__.__name__
print(*bytearray().decode().join(fallen).split(underscore))
