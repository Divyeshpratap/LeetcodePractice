'''
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
'''
class Solution:
    def compress(self, chars: List[str]) -> int:

        groupLen = 0
        target = 0
        i = 0
        while i < len(chars):
            groupLen = 1
            while (i + groupLen) < len(chars) and chars[i + groupLen] == chars[i]:
                groupLen += 1
            chars[target] = chars[i]
            target += 1
            if groupLen > 1:
                groupList = list(str(groupLen))
                for j, item in enumerate(groupList):
                    chars[target + j] = item
                target += len(groupList)
            i = i + groupLen
        return target
'''
Time Complexity: O(len(chars))
Space Complexity: O(1)
'''
