
class Solution(object):
  @classmethod
  def generateSquares(cls,n:int)->list:
    return [i**2 for i in range(1,n)]

if "__name__"=="__main__":
  obj = Solution()
  x = int(input("Enter the number : "))
  print(obj.generateSquares(x))
