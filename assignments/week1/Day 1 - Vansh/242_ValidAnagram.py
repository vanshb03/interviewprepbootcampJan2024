# Vansh B
# Date: Jan 2, 2023

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Converted both strings into lists
        list1 = list(s)
        list2 = list(t)
        
        #Sorted both lists:
        list1.sort()
        list2.sort()

        #If both lists are same, then the ANagram is Valid else it is Not Valid.
        if list1 == list2:
            return True
        else:
            return False