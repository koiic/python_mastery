"""class Trie:
    def __init__(self):
        self.root = {"*":"*"}

    def add_word(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in curr_node:
                curr_node[letter] ={}
            curr_node = curr_node[letter]
        curr_node["*"] = "*"

    def does_word_exist(self, word):
        curr_node = self.root
        for letter in word:
            if letter not in word:
                return False
            curr_node = curr_node[letter]
        return "*" in curr_node

"""
class TrieNode:
    def __init__(self,letter):
        self.letter = letter
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = {"*","*"}

    def add_word(self, letter):
        pass




if __name__ == '__main__':
    trie = Trie()
    words = ["wait", "waiter", "shop", "shopper"]
    for word in words:
        trie.add_word(word)

    print(trie.does_word_exist("wait"))
    print(trie.does_word_exist(""))
    print(trie.does_word_exist("waite"))
    print(trie.does_word_exist("shop"))
    print(trie.does_word_exist("shoppp"))
