# Example:
# You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:
#
# Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
# Output: 8
# Explanation: There are:
# - 1 box of the first type that contains 3 units.
# - 2 boxes of the second type that contain 2 units each.
# - 3 boxes of the third type that contain 1 unit each.
# You can take all the boxes of the first and second types, and one box of the third type.
# The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        s = 0
        
        # sort by number of units in a box, which is the second value in the pair
        boxTypes.sort(key=lambda x:x[1])
        
        #after sort, the max unit boxes is at the end of the array. Iterate reversely from the back.
        max_idx =  len(boxTypes)-1
        
        while (truckSize > 0 and max_idx >=0):
            if boxTypes[max_idx][0] > truckSize:
                s += boxTypes[max_idx][1]*truckSize
                truckSize = 0
                max_idx = -1
                
            else:
                s += boxTypes[max_idx][0]*boxTypes[max_idx][1]
                truckSize -= boxTypes[max_idx][0]
                max_idx -=1
                
        
        return s
