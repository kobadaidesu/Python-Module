特殊変数__name__について
'__main__'ってのはpython fileがscriptとして直接実行されたときに__name__変数に設定される値
if __name__ == '__main__'という条件式はfileがscriptとして直接実行された場合にのみTrueになる
これがあるとほかのfileからimportされてるかどうかを判別できる
moduleの再利用に便利


classは設計図、instanceはその設計図から実際に作ったもの
class will be instantiated, then the attributes will be set


0.8みたいな少数派コンピュータ内部でピッタリ表示できないのでround()でたいしょ

ex1, 
ex2 では `Plant()` でインスタンスを作ったあと、外側から属性を代入して初期化していた。
ex3 では `__init__` を使うことで、`Plant("Rose", 25.0, 30)` のようにインスタンス作成と初期化を同時にできる。
この方法だとコードが短くなり、植物を作った直後から `show()` や `grow()` を使える。You need to streamline the plant creation process: instantiate and
initialize the class for a new plant at the same time.


get がない
-> rose._height を直接読む
-> 外側がクラスの内部構造に依存する

get がある
-> rose.get_height() で読む
-> 外側は内部構造を知らなくていい
-> 後から中身を変えやすい
-> 必要なら値を加工して返せる


継承は、親クラスの属性やメソッドを子クラスで再利用し、違う部分だけを追加・変更する仕組み。
super().__init__()を使うことで親クラスの初期化処理を再利用できる
親classにあるmethodは子classでもそのまま使える
子class で追加の表示や処理が必要な場合はsuper.method()で上書きする(オーバーライド)


@staticmethodについて
今回は独立した関数として書いてもいいけど課題文で指定されてるのであえてclassないで作成
classに属するけどselfを使わないmethodの練習用
@clssmethodについて
methodを書いたクラスに固定されるってより実際に呼び出したclassに合わせて動かせるmethod

nested class はあくまでPlant.Statics classであるからStaticsのobject は存在しない
だからそのためにself._stats = Plant.Statics()
Plantを作成するとき自動でStaticsもPlantの持ち物として自動生成する