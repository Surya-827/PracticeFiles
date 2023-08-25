class Solution(object):
  @classmethod
  def tablePrinter(cls,x:int,n:int):
    for i in range(1,n+1):
        print(f"{x} x {i} = {x*i}")


if __name__=="__main__":
  obj = Solution()
  table = int(input("Enter the Table : ")
  n = int(input("Enter multiple limit : "))
  obj.tablePrinter(table,n)
