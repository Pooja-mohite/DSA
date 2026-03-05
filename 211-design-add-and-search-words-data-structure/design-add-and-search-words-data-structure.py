class WordDictionary(object):

    def __init__(self):
         self.trie = {}
        

    def addWord(self, word):
        node = self.trie
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node['#'] = True 
        

    def search(self, word):
        def dfs(index, current):
            for i in range(index, len(word)):
                ch = word[i]
                if ch == '.':
                    for key in current:
                        if key != '#' and dfs(i + 1, current[key]):
                            return True
                    return False
                else:
                                                                                                 if ch not in current:
                                                                                                     return False
                                                                                                 current = current[ch]
            return '#' in current
        return dfs(0, self.trie)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)