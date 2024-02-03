'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magHash = {item: 0 for item in magazine}
        ransomHash ={item: 0 for item in ransomNote}
        for item in magazine:
            magHash[item] = magHash.get(item, 0) + 1
        for item in ransomNote:
            ransomHash[item] = ransomHash.get(item, 0) + 1
        print(f' magHash dictionary is {magHash}')
        print(f' ransomHash dictionary is {ransomHash}')
        for item in ransomHash:
            ransomHash[item] = ransomHash.get(item) - magHash.get(item, 0)
        print(ransomHash)
        for value in ransomHash.values():
            if value  > 0:
                return False
        return True
'''
Time Complexity: O(M + N)
Space Complexity: O(M + N)
'''
