class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        #using solution approach by dev-josh
        #using dictionaries to check occurrences
        return self.check(nums1,nums2) + self.check(nums2,nums1)
    
    def check(self, list1, list2):
        checkA = {}
        for i in list1:
            if (i*i) not in checkA:
                checkA[i*i] = 1
            else:
                checkA[i*i] +=1
        
        checkB = {}
        for i in range(len(list2)-1):
            for j in range(i+1,len(list2)):
                if list2[i]*list2[j] not in checkB:
                    checkB[list2[i]*list2[j]] = 1
                else:
                    checkB[list2[i]*list2[j]] +=1
        result = 0
        for i in checkA.keys():
            if i in checkB.keys():
                result += checkA[i]*checkB[i]
        return result
