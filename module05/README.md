(ABC)ってのは@abstractmethodを機能させるための土台
@abstractmethodはabstract methodを指定するデコレータ　
オーバーライド＝メソッドオーバーライド
@abstractmethodに指定することでこのメソッドは絶対オーバーライドしろと強制するもの
これをすることによって実装忘れの発見、このクラスを継承するならこのメソッドを必ずという認識ができる、可読性

n.validate と書くと、. の本体(__getattribute__)が:

オブジェクトが持つクラスリンク(n.__class__)を見る ← ここが「型を知る」部分。関数呼び出しじゃなく、埋め込まれたリンクを読むだけ
そのクラスの MRO(NumericProcessor → DataProcessor → ...)を上から探す
最初に見つかった validate を取る
self=n を埋めた bound method にして返す
同じインターフェース(validate/ingest)への1つの呼び出しが、オブジェクトの実際の型に応じて異なる実装として振る舞う性質


ABC	Protocol
種類	サブタイプ多態(名前的)	構造的多態 / 静的ダックタイピング
考え方	「継承を宣言したから DataProcessor だ」	「形が合ってるから ExportPlugin だ」
例え	血統書(is-a を宣言)	見た目(acts-like)


軸	ABC	Protocol
適合の仕方	継承を書く(class X(Base))	形が合うだけ(継承不要)
強制する人	Python 実行時 + mypy(二重)	mypy のみ(実行時ノーガード)
破ったとき	インスタンス化で TypeError	呼んだ時 AttributeError / 事前に mypy
実装の共有	できる(output等を継承)	できない(契約のみ)
所有してない型	適合させられない	適合させられる
結合度	密(相手が自分を継承)	疎(相手は自分を知らない)

継承したらsuper()したら前処理を引き継げるけどprotocol は継承しないので持ってこれない、そこの違いもある