"""
208. Implement Trie (Prefix Tree)
A trie (pronounced as "try") or prefix tree is a
tree data structure used to efficiently store and retrieve keys in a dataset of strings.
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word)
Returns true if the string word is in the trie (i.e., was inserted before),
 and false otherwise.
boolean startsWith(String prefix)
Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.

"""


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()
        # use dict as node

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            if c not in node:
                node[c] = dict()

            node = node[c]

        node['END'] = True
        # use 'END' key to check isEnd or not

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c not in node:
                return False

            node = node[c]

        if 'END' in node:
            return node['END']

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]

        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

"""
Runtime: 128 ms, faster than 91.56% of Python3 online submissions for Implement Trie (Prefix Tree).
Memory Usage: 27.9 MB, less than 77.77% of Python3 online submissions for Implement Trie (Prefix Tree).
"""
