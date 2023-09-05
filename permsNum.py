from itertools import permutations as p

class Solution(object):
  @classmethod
  def getPermsOfNum(cls,n:int)->list:
    temp = list(p(n))
    out = ["".join(map(str,i)) for i in temp]
    return out


if "__name__"=="__main__":
  obj = Solution()
  k = int(input("Enter the Number : "))
  print(obj.getPermsOfNum(k))
