"""
  @author:"zzg"
  @file:dichotomy_method.py
  @time:2020/6/30 15:10
"""


def binary_search(list: list, item: int):
    """
    二分查找法，时间复杂度为log2n
    :param list: 一组有序的数据
    :param item: 查找的数据
    :return: 
    """
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = int((low + high) / 2)
        guess_data = list[mid]
        if guess_data == item:
            return mid
        if guess_data > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    data_list = [1, 2, 5, 7, 9, 12]
    res = binary_search(data_list, 5)
    print(res)
