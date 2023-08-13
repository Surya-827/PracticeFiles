
class Solution(object):
    @classmethod
    def findVowelsInGivenName(name : str) -> list:
        vowel_list = ['a', 'e','i' ,'o']
        return *[ char for char in list(name) if char in vowel_list]
    

if __name__=="__main__":
    obj = Solution()
    name = input("Enter the Name : ")
    print("\nThe Vowels are : ",obj.findVowelsInGivenName(name))