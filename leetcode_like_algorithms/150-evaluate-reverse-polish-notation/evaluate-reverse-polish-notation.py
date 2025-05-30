class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #division -> floor divsion //
        #no / by 0

        #[4,13,5,/2,3++]=

        #[10,6,12,-11*]
        #[10,6,-132/]
        #[10,-22*]=[-220,17][-237,5]

        stack = []
        operators = {'/','+','-','*'}

        for element in tokens:
            if element in operators:
                a=stack.pop()
                b=stack.pop()
            
                if element == '/':
                    ans = int(int(b)/int(a))
                   
                    
                    
                elif element == '*':
                    ans = int(b)*int(a)
                    
                    
                    
                elif element == '+':
                    ans = int(a)+int(b)
                    
                    
                    
                else: 
                    ans = int(b)-int(a)
                stack.append(ans)
                    
            else:
                stack.append(int(element))  
            
                
        return stack[0]
            





