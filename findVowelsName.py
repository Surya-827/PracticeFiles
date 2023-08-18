
class Solution(object):
    @classmethod
    def findVowelsInGivenName(cls,name : str) -> list:
        vowel_list = ['a', 'e','i' ,'o']
        return sorted(list(set([ char for char in list(name) if char in vowel_list])))
    
    @classmethod
    def findConsonantsGivenName(cls,name:str) -> list:
        cons_list = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        return sorted(list(set([ char for char in list(name) if char in cons_list])))
    
    @classmethod
    def findAsciiSumOfGivenName(cls,name:str) -> int:
        ascii_sum=sum([ord(i) for i in list(name)])
        return ascii_sum
    
    @classmethod 
    def findAsciiSumOfOddValues(cls,name:str) -> int:
        ascii_sum = sum([ord(i) for i in list(name) if ord(i)%2==1])
        return ascii_sum

if __name__=="__main__":
    obj = Solution()
    name = input("Enter the Name : ")
    print("\nThe Vowels are : ",obj.findVowelsInGivenName(name))
    print("\nThe Consonants are : ",obj.findConsonantsGivenName(name))
    