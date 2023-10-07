class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di ={}
        for index,word in enumerate(strs):
            currentword = ''.join(sorted(word))
            if di.get(currentword,False):
                di[currentword].append(strs[index])
            else:
                di[currentword] = [strs[index]]
        arr=[]
        for x in di.keys():
            arr.append(di.get(x,[]))
        return arr