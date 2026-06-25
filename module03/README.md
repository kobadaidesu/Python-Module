pythonは基本的にsys.srgvのリスト型でコマンドライン引数を管理する
for i in sys.argv[1:]
for index in range(1, len(sys.argv)):
    print(f"Argument {index}: {sys.argv[index]}")


返り値がTupleのとき


set は重複しない要素だけを持つコレクション？
それぞれの関数の性質


KeyはUnique
辞書型はkey: valueで構成されていて一発で情報にアクセスできる
リスト型は順番があってインデックスのような番号でアクセスできる
一覧やループ処理がしやすい


普通関数ってreturn するけどyieldを使うときは基本的にReturnをしない
そのためにgenerator objectを使って返す関数になる
だからyieldを使うときはgeneratorの型を書く
typing.Generator[
    yield で外に出す値の型,
    send() で中に受け取る値の型,
    return で最後に返す値の型
]
next()でyieldを呼び出せる
yield, Generator, next()はハッピーセットの関係
Generator関数とはyieldで値を１個ずつ出せる関数
https://zenn.dev/nakurei/articles/understanding-python-generators
Return、Yieldのそれぞれの利点


capitalizeは文字列にしか適用できない
リストはだめ


リスト内包表記[入れたい値 for 変数 in 元のデータ if 条件]
辞書内包表記{key: value for 変数 in 元データ}
