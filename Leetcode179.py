selection sort
def largestNumber3(self, nums):
    for i in xrange(len(nums), 0, -1):
        tmp = 0
        for j in xrange(i):
            if not self.compare(nums[j], nums[tmp]):
                tmp = j
        nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
    return str(int("".join(map(str, nums))))

//

import itertools
def largest(nums):
  nums2 = list(itertools.permutations(nums,len(nums)))
  nums3=[]
  for i in range(0,len(nums2)):
    nums3.append(list(nums2[i]))
  for i in range(0,len(nums3)):
    nums3[i]=list(map(str,nums3[i]))
  for i in range(0,len(nums3)):
    nums3[i]="".join(nums3[i]) #여기서 리스트 "".join은 문자열에서만 가능하다고
  nums3=list(map(int,nums3))
  nums3.sort(reverse=True)
  return nums3[0]

//
# 179. largest-number
def swap(n1, n2):
    return str(n1) + str(n2) < str(n2) + str(n1)  # bool 

# 3, 10 -> 103, 310
nums = [3,30,34,5,9]

i = 1
while i < len(nums):
    j = i
    while j > 0 and swap(nums[j-1], nums[j]):
        nums[j], nums[j-1] = nums[j-1], nums[j]  # swap
        j -= 1  # 큰 걸 앞으로 보낼 수 있도록!
        print(nums)
    i += 1
    
str(int("".join(map(str, nums))))
