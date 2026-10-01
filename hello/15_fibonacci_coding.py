# 15. フィボナッチ符号 × ミュータブルなデフォルト引数
#
# Python で有名な罠「デフォルト引数のリストは呼び出しをまたいで共有される」を
# あえてメモ化キャッシュとして使う。fibonacci() の memo は関数に住み着いて育ち続ける。
# フィボナッチ数そのものも「長さ」で表した単項リストで、足し算はリストの連結。
#
# 文字コードはゼッケンドルフ表現 (隣り合わないフィボナッチ数の和) を
# 下位桁から並べ、末尾に 1 を足したフィボナッチ符号で書かれている。
# ゼッケンドルフ表現には 1 が連続しないので、"1 1" が現れたら 1 文字の終わり。
# つまり区切りのない 1 本のビット列から、自己同期的に文字を切り出せる。

O = []
I = [O]


def fibonacci(rank, memo=[[[]], [[], []]]):
    while len(memo) <= len(rank):
        [*_, a, b] = memo
        memo.append(a + b)
    return memo[len(rank)]


stream = [
    O, I, O, O, O, I, O, O, O, I, I,  # h = 2 + 13 + 89
    I, O, I, O, I, O, O, O, O, I, I,  # e = 1 + 3 + 8 + 89
    I, O, O, I, O, I, O, O, O, I, I,  # l = 1 + 5 + 13 + 89
    I, O, O, I, O, I, O, O, O, I, I,  # l
    I, O, O, O, O, O, I, O, O, I, I,  # o = 1 + 21 + 89
    O, O, I, O, I, O, I, I,  # (空白) = 3 + 8 + 21
    I, O, O, O, I, O, I, O, O, I, I,  # w = 1 + 8 + 21 + 89
    I, O, O, O, O, O, I, O, O, I, I,  # o
    I, O, I, O, O, O, I, O, O, I, I,  # r = 1 + 3 + 21 + 89
    I, O, O, I, O, I, O, O, O, I, I,  # l
    O, O, I, O, I, O, O, O, O, I, I,  # d = 3 + 8 + 89
]


def decode(bits):
    page = bytearray()
    word = []
    rank = []
    previous = O
    for bit in bits:
        if bit and previous:
            page.append(len(word))
            word = []
            rank = []
            previous = O
            continue
        if bit:
            word += fibonacci(rank)
        rank.append(bit)
        previous = bit
    return page


print(decode(stream).decode())
