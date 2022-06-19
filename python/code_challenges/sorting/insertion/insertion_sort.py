
def insertion_sort(array):
    for i in range(1, len(array)):
        j = i - 1
        temp = array[i]
        while j >= 0 and temp < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp
    return array


if __name__ == '__main__':
    int_list = [5,12,7,5,5,7]
    result = insertion_sort(int_list)
    print(result)
