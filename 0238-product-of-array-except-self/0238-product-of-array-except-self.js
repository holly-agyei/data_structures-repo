/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    //create to arrays
    //1-left product up to self(exc), 2-right product up to self(exc)

    let left_arr = []
    let right_arr = []

    prod =1
    prodl = 1
    let idx = nums.length-1

    for (const num of nums){
        left_arr.push(prod)
        prod = prod*num
        right_arr[idx] = prodl
        prodl = prodl*nums[idx]
        idx--
        
    }

    
    // prodl = 1
    // for(let i = nums.length-1; i>=0; i--){
    //     right_arr[i] = prodl
    //     prodl = prodl*nums[i]
    // }

    let result = [];
    for (let i = 0; i < nums.length; i++) {
        result[i] = left_arr[i] * right_arr[i];
    }
    return result;


};