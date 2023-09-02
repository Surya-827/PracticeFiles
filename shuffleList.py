
import random as r

class Solution(object):
  @classmethod
  def getShuffledList(cls,st:list)->list:
    r.shuffle(st)
    return st



if "__name__"=="__main__":
  obj = Solution()
  l = list(map(int,input().split()))
  print(obj.getShyffledList(l)
