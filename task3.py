nums = [1,2,3,7,4,3,4,5,9]
new = []
temp = []

for i in range(len(nums)-1):
    if nums[i-1] == nums[-1]:
        prev = None
    else:
        prev = nums[i-1]
    current = nums[i]
    next = nums[i+1]
    if not prev and current < next:
        temp.append(current)
        temp.append(next)
    elif prev and current < next:
        if current not in temp:
            temp.append(current)
        temp.append(next)
    elif prev and current > next:
        if len(temp) != 0:
            new.append(temp)
            temp = []
        else:
            pass
    if next == nums[-1]:
        new.append(temp)

for i in new:
    print(i)
