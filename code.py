class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        p=''
        for word in words:
            p+=word
            if p==s:
                return True
            if len(s)<len(p):
                return False
        return False
        
