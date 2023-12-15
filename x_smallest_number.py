def getX(x, nums):
  # write your code here
  if x > len(nums) or len(nums) == 0:
    return 0
  sorted_nums = sorted(nums)
  return sorted_nums[x-1]


print(getX(7, [6, 3, -1, 5]))