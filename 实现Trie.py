from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children=defaultdict(TrieNode)
        self.end=False

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur=self.root
        for w in word:
            cur=cur.children[w]
        cur.end=True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur=self.root
        for w in word:
            if w not in cur.children:
                return False
            cur=cur.children[w]
        if cur.end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur=self.root
        for p in prefix:
            if p not in cur.children:
                return False
            cur=cur.children[p]
        return True