def func(x):
    return (x - 60.39636407237782) * (x - 60.39636407237782)


def for_back(function):
    x = 30  # 初始值
    step = 1  # 初始步长
    magnification = 2  # 放大倍数
    print(x, step, magnification)
    if function(x) > function(x+step):
        while function(x) > function(x + step):
            print(x + step)
            x = x + step
            step = step*magnification
        if function(x) <= function(x + step):
            print(x + step)
            return int(x-step/magnification), int(x + step)
    elif function(x) > function(x - step):
        while function(x) > function(x - step):
            print(x - step)
            x = x - step
            step = step * magnification
        if function(x) <= function(x - step):
            print(x - step)
            return int(x - step), int(x + step/magnification)
    else:
        print("测试点为最低点，请更改测试值。")


if __name__ == "__main__":
    print(for_back(func))

