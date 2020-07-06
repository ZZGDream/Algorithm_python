"""
  @author:"zzg"
  @file:select_sort.py
  @time:2020/7/6 16:43
  选择排序
"""


def find_smallest(arr):
    """
    找出最小值的索引
    :param arr: 
    :return: 
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index # 返回是索引


def select_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


if __name__ == '__main__':
    res = select_sort([5, 3, 6, 2, 10])
    print(res)
