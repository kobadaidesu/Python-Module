exceptionの例外タイプはいろいろある
as ~ でその変数にエラーの中身が入る


raiseってのは自分でerrorを発生させることができる


変な値が来た        -> ValueError
0で割った           -> ZeroDivisionError
ファイルがない      -> FileNotFoundError
型の使い方が変      -> TypeError


https://helve-blog.com/posts/python/python-user-defined-exceptions/
例外クラスを作成するときは基本的にException
Exception に message を渡すと、その message が error.args に保存される
except ... as error は例外オブジェクト全体を受け取る
Exception
  ↓
GardenError
  ↓
PlantError


Handles errors if a plant name is invalid and can’t be watered. In that case, stop
the test and immediately return to main.
これがあるからexceptionにはreturn 
出力整形だりぃ