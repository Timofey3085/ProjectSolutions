def max_rot(n):
    nums = list(n[1:]) + list(n[0])
    return "".join(nums)


print(max_rot('123'))
