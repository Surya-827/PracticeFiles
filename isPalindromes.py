class Solution(object):
  @classmethod
  def isPalindromes(cls,a:str,b:str)->bool:
    return [True if(a==b[::-1] or a[::-1]==b) else False][0]


if __name__=="__main__":
  obj = Solution()
  x=input("Enter the first word : ")
  y=input("Enter the second word : ")
  print(obj.isPalindromes(x,y))
