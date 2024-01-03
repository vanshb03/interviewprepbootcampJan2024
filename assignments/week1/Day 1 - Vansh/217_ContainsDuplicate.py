#Brute Force 
#Time Complexity of (O(n^2))
#Space Complexity of 1
class Solution:
    def containsDuplicate(self, nums) -> bool:#List[int]) -> bool:
        for i in range(len(nums)): #n
            for j in range(i+1,len(nums)): #n
                if nums[i] == nums[j]:
                    return True

        return False

#Hash Maps
#Time Complexity of O(1)
#Space Complexity of (O(n))
class Solution:
    def containsDuplicate(self, nums) -> bool: #List[int]) -> bool:
        map1 = {} #Maps are called dictionaries, maps are short for hashmaps.
        for i in nums:
            if i in map1:
                return True
            else:
                map1[i] = True

        return False
    

#Solution3
class Solution:
    def containsDuplicate(self, nums) -> bool: #List[int]) -> bool:
        return len(set(nums)) != len(nums)