import Vars

ls = Vars.ls

def find_max(nums):
    nums.sort()
    return nums[-1]


print(find_max(ls))
