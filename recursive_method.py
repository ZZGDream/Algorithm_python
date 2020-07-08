"""
  @author:"zzg"
  @file:recursive_method.py
  @time:2020/7/8 9:46
  递归/栈的调用
"""

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


if __name__ == '__main__':
    res = fact(5)
    print(res)

