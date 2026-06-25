pythonは基本的にsys.srgvのリスト型でコマンドライン引数を管理する
for i in sys.argv[1:]
for index in range(1, len(sys.argv)):
    print(f"Argument {index}: {sys.argv[index]}")


返り値がTupleのとき
