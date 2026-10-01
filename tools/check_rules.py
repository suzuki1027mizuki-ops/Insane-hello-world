# ルール検査ツール (Hello World 本体ではないので、検査用の文字列リテラルは使っている)
#
# 標準ライブラリは import しない。ast モジュールの代わりに、組み込みの compile() に
# PyCF_ONLY_AST フラグ (0x400) を渡して構文木を直接受け取る。
#
# 使い方: 検査したいファイルのパスを 1 行に 1 つずつ標準入力に流す
#   ls hello/*.py | python tools/check_rules.py

ONLY_AST = 0x400

# 不変 (イミュータブル) な値をソースに直接書き込む構文
FORBIDDEN_NODES = {
    "Constant": "リテラル (文字列 / 数値 / bytes / True / False / None / ...)",
    "JoinedStr": "f 文字列",
    "TemplateStr": "t 文字列",
    "Tuple": "タプル",
    "Import": "import 文",
    "ImportFrom": "from ... import 文",
}

# イミュータブルな値を明示的に作る組み込み関数・定数
FORBIDDEN_NAMES = {
    "str", "int", "float", "complex", "bool", "tuple", "bytes", "frozenset",
    "range", "slice", "chr", "ord", "repr", "ascii", "format", "bin", "oct",
    "hex", "__import__", "Ellipsis", "NotImplemented",
}


def walk(node):
    yield node
    for field in node._fields:
        value = getattr(node, field, None)
        children = value if isinstance(value, list) else [value]
        for child in children:
            if hasattr(child, "_fields"):
                yield from walk(child)


def check(path):
    with open(path, encoding="utf-8") as handle:
        source = handle.read()
    tree = compile(source, path, "exec", ONLY_AST, dont_inherit=True)
    problems = []
    for node in walk(tree):
        kind = type(node).__name__
        line = getattr(node, "lineno", "?")
        if kind in FORBIDDEN_NODES:
            problems.append(f"{path}:{line}: {FORBIDDEN_NODES[kind]} は禁止")
        if kind == "Name" and node.id in FORBIDDEN_NAMES:
            problems.append(f"{path}:{line}: 組み込みの {node.id} は禁止")
    return problems


def main():
    failures = []
    checked = 0
    while True:
        try:
            path = input().strip()
        except EOFError:
            break
        if not path:
            continue
        checked += 1
        problems = check(path)
        failures += problems
        print(("NG  " if problems else "OK  ") + path)
    for problem in failures:
        print(problem)
    print(f"{checked} ファイル検査, 違反 {len(failures)} 件")
    if failures or not checked:
        raise SystemExit(1)


main()
