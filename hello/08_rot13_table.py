# 08. ROT13 と手作りの変換テーブル
#
# 暗号文 "uryyb jbeyq" をキーワード引数の名前として持ち込み、ROT13 で解読する。
# 変換テーブル (256 バイト) は数値リテラルなしで組み立てる:
#   1. [[]] を 8 回倍々にして長さ 256 のリストを作る
#   2. 「今のテーブルの長さ」を自分自身に追記し続けて恒等テーブルを作る
#   3. bytearray.islower() で小文字 a〜z を自力で探し、半分 (13) ずらして書き換える
# エンコーディング名 "ascii" すら bytearray.isascii というメソッド名から掘り出す。

one = len([[]])

span = [[]]
for _ in [[], [], [], [], [], [], [], []]:
    span += span

table = bytearray()
while len(table) < len(span):
    table.append(len(table))

alphabet = bytearray()
for code in table:
    if bytearray([code]).islower():
        alphabet.append(code)

half = len(alphabet) >> one
shifted = alphabet[half:] + alphabet[:half]
shifted.reverse()
for code in alphabet:
    table[code] = shifted.pop()

[_, _, *codec] = bytearray.isascii.__name__
codec = bytearray().decode().join(codec)

secret = dict(uryyb=[], jbeyq=[])
print(*[bytearray(word, codec).translate(table).decode() for word in secret])
