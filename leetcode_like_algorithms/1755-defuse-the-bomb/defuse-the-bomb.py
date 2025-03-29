class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        #there have to be a way to get  the element at the ith index if it's greater tan n.
        results = []
        #k =0
        if k ==0:
            return [0 for i in code]
        
        elif k > 0:
            #GET A WINDOW OF K
            #if k>len(arr)
            summ =0
            for i in range(1, k+1):
                summ+=code[i%len(code)]
            pointer =0
            while pointer < len(code):
                results.append(summ)

                if pointer+1<len(code):
                
                    summ = summ-code[pointer+1] + code[(k+1)%len(code)]
                    k+=1
                    pointer+=1
                else:
                    break
            
        elif k < 0:
            l = k
            summ,i,right = 0, 0, 0
            summ = sum(code[k:])
            
            while right< len(code):
                results.append(summ)
                summ= summ-code[k]+code[i%len(code)]
                i+=1
                k+=1
                right+=1
        return results

            