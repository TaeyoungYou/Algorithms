import sys

while True:
    nums=list(map(int, sys.stdin.readline().strip().split()))
    if not nums[0] and not nums[1] and not nums[2]:
        break

    max_num = max(nums)
    nums.remove(max_num)
    # 대안 코드: nums.sort()

    if pow(max_num,2) == pow(nums[0],2)+pow(nums[1],2):
        print("right")
    else:
        print("wrong") 