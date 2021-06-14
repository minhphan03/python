class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        s = 0
        boxTypes.sort(key=lambda x:x[1])
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
