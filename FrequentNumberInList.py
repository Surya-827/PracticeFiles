class Solution(object):
  @classmethod
  def findFreqOccNum(cls,x:list)->int:
    return max(set(a), key = a.count)


if "__name__"=="__main__":
  obj = Solution()
  x=list(map(int,input().split(" ")))
  print(obj.findFreqOccNum(x))
