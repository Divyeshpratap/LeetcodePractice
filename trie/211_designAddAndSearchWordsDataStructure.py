'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
'''
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endNode = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()


    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.endNode = True

    def search(self, word: str) -> bool:
        def recSearch(j, root):
            curr = root
            for i in range(j, len(word)):
                if word[i] == '.':
                    for child in curr.children.values():
                        if recSearch(i+1, child):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            return curr.endNode
        return recSearch(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
'''
Time Complexity: For addWord O(llen(word)), For search in worst case O(26^(len(word))
Space Complexity: O(26^len(word))
*********************************
Summary Statistics:
Runtime: 1567 ms, faster than 57.35% of Python3 online submissions for Design Add and Search Words Data Structure.
Memory Usage: 64.2 MB, less than 64.80% of Python3 online submissions for Design Add and Search Words Data Structure.
'''
