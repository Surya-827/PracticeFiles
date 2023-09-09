
class Solution(object):
  @classmethod
  def getUniCode(cls,s :str):
    return "\U0001F600"+" "+s


if "__name__"=="__main__":
  obj =Solution()
  s = input("Enter the name : ")
  print(obj.getUniCode(s))
