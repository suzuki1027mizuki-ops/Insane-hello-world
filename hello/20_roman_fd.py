# 20. ローマ数字を print なしでファイル記述子 1 に直接書く
#
# 文字コードをローマ数字で書き、キーワード引数の名前として持ち込む。
#   CIV = 104 (h)   CI = 101 (e)   CVIII = 108 (l)   CXI = 111 (o)   XXXII = 32 (空白)
#   CXIX = 119 (w)  CXIV = 114 (r) C = 100 (d)       X = 10 (改行)
# dict のキーは重複できないので、2 回目以降の l と o は「異綴り」で書く。
#   LLVIII = LXXXXXVIII = 108,  LLXI = 111   (どれも右から読む加減算規則で正しく解釈できる)
#
# 各記号の値も数値リテラルではなく、単項リストの連結で作る (V = I が 5 つ、…)。
# 出力は print を使わず、標準出力のファイル記述子 (= 1) をバイナリモードで開いて
# bytearray をそのまま流し込む。モード "wb" は swapcase の 2 文字目と bytearray の頭文字。

I = [[]]
V = I + I + I + I + I
X = V + V
L = X + X + X + X + X
C = L + L
glyphs = dict(I=I, V=V, X=X, L=L, C=C)

scroll = dict(
    CIV=[],
    CI=[],
    CVIII=[],
    LLVIII=[],
    CXI=[],
    XXXII=[],
    CXIX=[],
    LLXI=[],
    CXIV=[],
    LXXXXXVIII=[],
    C=[],
    X=[],
)


def parse(numeral):
    total = len([])
    peak = len([])
    letters = [*numeral]
    letters.reverse()
    for letter in letters:
        worth = len(glyphs[letter])
        if worth < peak:
            total -= worth
        else:
            total += worth
            peak = worth
    return total


page = bytearray(map(parse, scroll))

[_, w, *_] = bytearray.swapcase.__name__
[b, *_] = bytearray.__name__

with open(len(I), bytearray().decode().join([w, b]), closefd=not I) as stdout:
    stdout.write(page)
