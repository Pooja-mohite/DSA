class Trie(object):

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
    
    def insert(self, word):
        current = self
        for char in word:
            if char not in current.children:
                current.children[char] = Trie()
            current = current.children[char]
        current.is_end_of_word = True   

    def search(self, word):
        current = self
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word
        

    def startsWith(self, prefix):
        current = self
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)