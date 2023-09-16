#Expected number : As user gives a number 24 sum of digits is 6 then bin count of 1's should be odd 

class Solution(object):
  @classmethod
  def findNum(cls,n : int)->bool:
    digits_sum = sum([int(i) for i in str(n)]) 
    return [True if(str(bin(digits_sum)).count("1")%2==1) else False][0]

if "__name__"=="__main__":
  obj = Solution()
  n = int(input("Enter the number : "))
  print(obj.findNum(n))
