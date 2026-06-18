def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count_day(i):
        if i > days:
            return
        print(f"Day {i}")
        count_day(i + 1)

    count_day(1)
    print("Harvest time!")
