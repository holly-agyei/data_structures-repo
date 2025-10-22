class Solution:
    def numberToWords(self, num: int) -> str:
        #get map of ones, and tens.
        if num<=0:
            return "Zero"
        onesMap = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10:"Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15:"Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen"
        }
        
        tensMap = {
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
        }
        #now given a word we just want to divide it into threes and process it.
        #we will have two main part of the code
        #one that takes three parts and name it
        #one that take the name and add the billion,+++

        def get_name(n):
            lst = []
            #123, 101, 100, 000-
            if n:
                hundred = n//100
                if hundred:
                    lst.append(onesMap[hundred] + " Hundred")
            last_two = num%100
            if last_two>=20:
                #23
                tens, ones = last_two//10, last_two%10
                lst.append(tensMap[tens*10])
                if ones: #ones could be 0
                    lst.append(onesMap[ones])
            elif last_two: #thus less than 20 and not 0
                lst.append(onesMap[last_two])
            return " ".join(lst)
        
        res = []
        post_fix = ["", " Thousand", " Million", " Billion"]
        i = 0

        while num:
            three_digits = num%1000
            s = get_name(three_digits)
            if s:
                res.append(s + post_fix[i])
            num = num//1000
            i+=1
        return " ".join(res[::-1])





           
                
















