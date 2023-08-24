class Patterns(object):

    @classmethod 
    def rightTriangle(cls,rows:int):
        for i in range(1,rows+1):
            for j in range(1,i+1):
                print("#",end=" ")
            print()

    @classmethod
    def leftTriangle(cls,rows:int):
        for i in range(1,rows+1):
            for j in range(rows-i,-1,-1):
                print("#",end=" ")
            print()


if __name__=="__main__":
    obj = Patterns()
    rows = int(input("Enter Number of rows : "))
    obj.rightTriangle(rows)
    obj.leftTriangle(rows)