class Solution(object):
  @classmethod
  def containsNumbers(cls,st:str)->bool:
    return [ True if type(i)==num for i in st else False ]


if __name__=="__main__":
  obj = Solution()
  s = input("Enter the str : ")
  print(obj.containsNumbers)
