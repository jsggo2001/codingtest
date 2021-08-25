import time

nums = []
prenum = input()
answer = 0
for i in prenum:
    nums.append(int(i))
exp = []
for i in range(0, len(nums)):
    if nums[i] == 0 or nums[i] == 1:
        exp.append(int(0))
    else:
        exp.append(int(1))
# exp.pop()
print(exp)
answer = 1
for i in range(0, len(nums)):
    if exp[i] == 0:
        answer += nums[i]
    elif exp[i] == 1:
        answer *= nums[i]

print(answer)
