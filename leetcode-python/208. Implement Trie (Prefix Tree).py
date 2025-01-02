# 제출 코드 - Runtime 61.76 Memory 18.39
class Trie:

    def __init__(self):
        self.val = ""
        self.children = {}
        return

    def insert(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                child = Trie()
                child.val = char
                node.children[char] = child
            node = node.children[char]
        node.children[""] = Trie()
        return

    def search(self, word: str) -> bool:
        node = self
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return True if "" in node.children else False

    def startsWith(self, prefix: str) -> bool:
        node = self
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
