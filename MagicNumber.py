class Solution1(object):
  @classmethod
  def isMagicNumber(cls,num:int)->bool:
    return [True if num%9==1 else False ][0]

class Solution2(object):
  @classmethod
  def isMagicNumber(cls,num:int):
    st = sum([ int(i) for i in list(str(num)) ])
    if(len(str(st))>1):
      return isMagicNumber(st)
    else:
      if(st==1):print("isMagic number")
      else:print("Not Magic Number")



if __name__=="__main__":
  obj = Solution1()
  print(obj.isMagicNumber(int(input())))
