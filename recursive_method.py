"""
  @author:"zzg"
  @file:recursive_method.py
  @time:2020/7/8 9:46
  递归/栈的调用(栈是先进后出)
"""


def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


def sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + sum(arr[1:])


if __name__ == '__main__':
    res = fact(5)
    print(res)
