class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        reference: palindrome partioning
        new concept: no but enforcing intuition

        -a valid number u can add is 0<=x<=255 
        -a number shouldnt start with 0. 
        -only 0 is fine, but 02 or 0x is not accepted
        
        0 check:
        if len(s)==1 and s is 0:
            it's good
        if s>1 and s[0] is 0, not good. 
        """

        stack = [("", 0, 0)]
        res = []
        
        while stack:
            path, idx, segments= stack.pop()
            if idx == len(s) and segments ==4:
                res.append(path[:-1])
                continue #return in recursion
            for i in range(idx, len(s)):
                sub_ip = s[idx:i+1]
                #check for 0 lead
                if len(sub_ip)>1 and sub_ip[0]=="0":
                    break #leading 0's
                if int(sub_ip)<=255:
                    stack.append((path+sub_ip+".", i+1, segments+1))
        return res

 


