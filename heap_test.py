import heapq

nums = [9,7,5,3,1]

print(nums)

# using heapify to convert list into heap
heapq.heapify(nums)
print(nums)

heapq.heappop(nums)
print(nums)

heapq.heappop(nums)
print(nums)

print(nums[0])