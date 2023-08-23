import cowsay as c

Class Solution(object):
    @classmethod
    def WelcomeUser(cls,st:str):
		c.daemon(f"Welcome ! {st.capitalize()}")


if __name__=="__main__":
	obj = Solution()
	name =input("Enter your name : ")
	obj.WelcomeUser(name)
