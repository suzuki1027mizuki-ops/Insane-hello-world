# Insane hello world

**ミュータブルなオブジェクトだけを使って** Python で `hello world` を出力する、20 通りの方法。

```
$ python hello/14_unary_operators.py
hello world
```

## ルール

すべての `hello/*.py` は次のルールを守っています。ルールは [`tools/check_rules.py`](tools/check_rules.py) が構文木を調べて機械的に検査します。

| 禁止 | 例 |
| --- | --- |
| 標準ライブラリ (`import` / `from ... import` / `__import__`) | `import sys` |
| イミュータブルなリテラル | `"hello"` `b"x"` `104` `1.0` `True` `False` `None` `...` |
| f 文字列 / t 文字列 | `f"{x}"` |
| タプル (分割代入の左辺も含む) | `(a, b)` `a, b = ...` → 代わりに `[a, b] = ...` |
| イミュータブルを作る組み込み | `str` `int` `bool` `tuple` `bytes` `frozenset` `range` `chr` `ord` `repr` `format` `hex` … |

ソースコードに書いてよいのは `[]` `{}` `{x}` `bytearray()` `dict()` `set()` 、自作クラスのインスタンス、関数 (関数オブジェクトもミュータブル) だけです。

### 言い訳 (避けられないもの)

- `print` や `len` などの**組み込み関数**は使います。これは言語の一部で、標準ライブラリの import ではありません。
- **実行時に**インタプリタが生むイミュータブル (`len()` の戻り値の `int` 、最終的に表示する `str` など) は避けられません。そこで「ソースコードにイミュータブルを一切書き込まない」こと、そして文字列や数値は必ずミュータブルなものから**導出**することをルールにしています。
- コメントはリテラルではありません (18 番はそれを悪用しています)。

## 20 通りのアプローチ

| # | ファイル | 文字の出どころ | 仕組み |
| --- | --- | --- | --- |
| 01 | [dict_kwargs](hello/01_dict_kwargs.py) | キーワード引数の名前 | `dict.update(hello=[])` でキーを作り、`print(*dict)` |
| 02 | [class_chain](hello/02_class_chain.py) | クラス名 | クラスに後から `next` 属性を生やして連結リストにし、辿る |
| 03 | [getattr_recorder](hello/03_getattr_recorder.py) | 存在しない属性名 | `__getattr__` が属性名をリストに録音。`Recorder().hello.world()` |
| 04 | [mro_spelling](hello/04_mro_spelling.py) | 1 文字クラスの継承 | `h ← e ← l ← l ← o` の継承チェーンの `__mro__` を逆順に読む |
| 05 | [method_archaeology](hello/05_method_archaeology.py) | 組み込み型のメソッド名 | `bytearray.hex` / `bytearray.lower` / `dict` の名前を分割代入で発掘 |
| 06 | [exception_mining](hello/06_exception_mining.py) | エラーメッセージ | `[][0]` `{[]}` `[[], {}].sort()` で怒らせ、メッセージから文字を採掘 |
| 07 | [hex_smuggling](hello/07_hex_smuggling.py) | 16 進数の識別子 | クラス名 `_68656c6c6f20776f726c64` を `bytearray.fromhex` で戻す |
| 08 | [rot13_table](hello/08_rot13_table.py) | 暗号文 `uryyb jbeyq` | 256 バイトの変換テーブルを自力で組み、`islower()` で小文字を探して ROT13 |
| 09 | [josephus](hello/09_josephus.py) | 撹乱された文字列 `llhwoedrl_o` | ヨセフス問題 (3 人目ごとに脱落) をリストの回転で実行 |
| 10 | [bit_grid](hello/10_bit_grid.py) | 真理値のビットマップ | `[]` = 0、`[[]]` = 1。`acc += acc` (×2) と `append` (+1) だけで復号 |
| 11 | [set_algebra](hello/11_set_algebra.py) | 集合の濃度 | 2^i 個の新品原子を重みに持つビット集合。`w = o ^ {b4, b3}` のように集合演算で文字を導出 |
| 12 | [peano](hello/12_peano.py) | 入れ子リストの深さ | ペアノ算術。`0 = []`、`S(n) = [n]`、足し算・掛け算を再帰で定義 |
| 13 | [church](hello/13_church.py) | 関数の適用回数 | チャーチ数 (ラムダ計算)。評価時にリストへ追記させて回数を数える |
| 14 | [unary_operators](hello/14_unary_operators.py) | 単項演算子の並び | `+` で +1、`-` で ×2、`~` で 1 文字出力。`~---+--+-+ink` が `h` |
| 15 | [fibonacci_coding](hello/15_fibonacci_coding.py) | フィボナッチ符号のビット列 | ゼッケンドルフ表現 + 終端 `11` の自己同期符号。メモ化に「ミュータブルなデフォルト引数」の罠を使う |
| 16 | [huffman](hello/16_huffman.py) | ハフマン符号 | 入れ子リストのハフマン木を、真偽値のビット列で辿る |
| 17 | [brainfuck](hello/17_brainfuck.py) | Brainfuck プログラム | 命令を関数オブジェクトで表した BF 仮想機械。テープは `bytearray` |
| 18 | [self_reading](hello/18_self_reading.py) | 自分自身のコメント | 自分のソースを `bytearray` に読み込み、最終行のコメントを取り出す |
| 19 | [line_numbers](hello/19_line_numbers.py) | **行番号** | 104 行目で例外を起こす関数が `h`。トレースバックの `tb_lineno` が文字コード |
| 20 | [roman_fd](hello/20_roman_fd.py) | ローマ数字 | `CIV` = 104 などを解析し、`print` を使わずファイル記述子 1 に直接書き込む |

## 実行

```bash
bash run_all.sh
```

全プログラムを実行して出力が `hello world` であることを確かめ、続けてルール検査を行います。単体で動かすなら:

```bash
python hello/19_line_numbers.py
```

GitHub Actions で Python 3.10〜3.14 × Ubuntu / Windows の全組み合わせを検証しています。

## 注意

- **19 番は 1 行でも増減すると壊れます。** 行番号がデータそのものなので。
- 18 番は自分のファイルの最終行を読むので、最終行のコメントを消すと壊れます。
- 06 番は CPython のエラーメッセージに依存しています (3.10〜3.14 で確認)。
