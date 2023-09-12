

class Solution(object):
    @classmethod
    def solve1(cls,s:str)->bool:
        x,y = s.count("z"), s.count("o")
        if((2*x)==y):
            return "Yes"
        else:
            return "No"
    
    @classmethod
    def solve2(cls,s:str)->bool:
        return ["Yes" if (2*x==y) else "No"][0]


s = input()[:20]
obj = Solution()
print(obj.solve1(s))
