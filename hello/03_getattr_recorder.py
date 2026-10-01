# 03. 存在しない属性へのアクセスを録音する
#
# __getattr__ は「見つからなかった属性名」を文字列で受け取る。
# 属性アクセスを鎖のように繋げると、その名前がミュータブルなリストに溜まっていく。
# 最後に呼び出すと、録音したものを再生する。


class Recorder:
    def __init__(self):
        self.tape = []

    def __getattr__(self, name):
        self.tape.append(name)
        return self

    def __call__(self):
        print(*self.tape)
        self.tape.clear()


Recorder().hello.world()
