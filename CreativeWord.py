
def fun(s,n):
  new_str=""
  for i in s:
    new_str+=chr(ord(i)-n)
  return new_str

s = input("Enter the string : ")
n = int(input("Enter the limit : "))
print(fun(s,n))
