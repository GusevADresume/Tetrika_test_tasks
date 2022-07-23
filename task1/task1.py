def task(array) -> int:
    element = len(array)//2
    start = 0
    end = len(array)
    if len(array) > 2 and array[-1] != '1':
        while True:
            if array[element] == '1':
                start = element
                element += (len(array)-element) // 2
            if array[element] == '0' and array[element-1] == '0':
                end = element
                element -= (element-start)//2
            if array[element] == '0' and array[element-1] == '1':
                return element
    else:
        return -1

print(task("111111111110000000000000000"))