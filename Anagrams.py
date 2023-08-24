

class Solution(object):
    @classmethod
    def isAnagrams(cls,a:str,b:str)->bool:
        return [ True if(sorted(list(a))==sorted(list(b))) else False][0]


if __name__=="__main__":
    obj = Solution()
    str1 = input("Enter Str 1 : ")
    str2 = input("Enter str 2 : ")
    print(obj.isAnagrams(str1,str2))
    
