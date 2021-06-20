class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        cpdomains = [x.split() for x in cpdomains]
        cpdomains = [[x[0],x[1].split(".")] for x in cpdomains]
        result = {}
        for i,var in enumerate(cpdomains):
            temp = []
            while (len(var[1]) >0):
                temp.insert(0,var[1].pop())
                if ".".join(temp) not in result.keys():
                    count = int(var[0])
                    for j in range(i,len(cpdomains)):
                        if set(temp).issubset(set(cpdomains[j][1])):
                            count += int(cpdomains[j][0])


                    result[".".join(temp)]=count
        return [str(values)+" "+key for key,values in result.items()]
