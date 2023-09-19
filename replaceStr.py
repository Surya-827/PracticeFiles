
def manipulateStr(st:str):
  vowels = ["a","e","i","o","u"]
  for i in st:
    if i in vowels:
      st.replace(str(i),str(chr(ord(i)+1)))
  return st


s = input("Enter the string : ")
print(manipulateStr(s))
