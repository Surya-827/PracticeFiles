import random as r

def tossACoin():
  return r.shuffle(["Head","Tail"])[0]


print(tossACoin())
