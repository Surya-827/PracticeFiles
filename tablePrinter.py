class Solution(object):
  @classmethod
  def tablePrinter(cls,x:int,n:int):
    for i in range(1,n+1):
        print(f"{x} x {i} = {x*i}")

 @classmethod
 def findEvensInTable(cls,x:int,n:int):
   evens,odds=[],[]
   dic = dict(zip(list(range(1,n+1)),[x*i for i in list(range(1,n+1)) ]))
   for j in list(dict.values()):
       if(j%2==0):evens.append(j)
       if(j%2==1):odds.append(j)
   return evens


if __name__=="__main__":
  obj = Solution()
  table = int(input("Enter the Table : ")
  n = int(input("Enter multiple limit : "))
  obj.tablePrinter(table,n)
  print(obj.findEvensInTable(table,n))
