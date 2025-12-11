/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    //if it negative, return false or if the number modulo 10 is 0, it cant
    //get the last number by by dividing by 10
    //get the rest by modulo by 10
    let number = 0
    const original = x
    if(x<0){
        return false
    }
    while(x>0){
        let last = x%10
        x = Math.floor(x/10)
        number = (number*10)+last
        
    }
    
    if (number === original){
        return true
    }else{
        return false
    }

};