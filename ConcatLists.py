
class Solution(object):
  @classmethod
  def joinLists(cls,x:list,y:list)->list:
    return x+y

if "__name__"=="__main__":
  obj = Solution()
  x=list(map(int,input().split(" ")))
  y=list(map(int,input().split(" ")))
  print(obj.joinList(x,y))
