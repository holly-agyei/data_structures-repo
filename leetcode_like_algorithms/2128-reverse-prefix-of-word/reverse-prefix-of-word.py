class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        #handle case where the ch is not in word
        if ch not in set(word):
            return word
        #trying to combine everything together
        return "".join(word[word.find(ch)::-1])+word[word.find(ch)+1:]

        
        