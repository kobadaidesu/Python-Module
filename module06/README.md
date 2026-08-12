モジュール = 1つの.pyファイル
パッケージ = モジュールをまとめたフォルダ
import モジュール,
直接関数をimportをしたいときfrom モジュール import 関数
import パッケージの時は__init__ の公開APIに制限される

二段階公開APIのおかげてtransmutation2でalchemy.gold みたいに使える

dark の方ではわざと循環import を発生させてエラーを起こす、これは片方がimport を完了してないときにimport をするとエラーが出る
其れの解決方法として遅延importがある、片方は上に置いてもう片方は関数の中に置くことで循環import を解決することができる
