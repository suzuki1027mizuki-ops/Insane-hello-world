# 07. 16 進数を識別子に密輸する
#
# 識別子は数字で始められないが、アンダースコアで始めれば英数字を自由に並べられる。
# 68 65 6c 6c 6f 20 77 6f 72 6c 64 は "hello world" の 16 進表現。
# クラス名として持ち込み、先頭の "_" を分割代入で剥がし、
# bytearray.fromhex でミュータブルなバイト列に戻す。


class _68656c6c6f20776f726c64:
    pass


[_, *digits] = _68656c6c6f20776f726c64.__name__
message = bytearray.fromhex(bytearray().decode().join(digits))
print(message.decode())
