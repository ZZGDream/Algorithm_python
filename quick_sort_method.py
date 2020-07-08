"""
  @author:"zzg"
  @file:quick_sort_method.py
  @time:2020/7/8 15:10
  快递排序
"""


def quick_sort(arr):
    """
    快速排序也是用的递归实现，只不过是新的一种数学逻辑
    :param arr: 
    :return: 
    """
    if len(arr) < 2:  # 此处不要用==1的写法
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    res = quick_sort([10, 5, 6, 2, 3])
    print(res)
