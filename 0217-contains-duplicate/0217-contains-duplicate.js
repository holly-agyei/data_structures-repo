/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    //first use a set and compare the lenghts 
   return new Set(nums).size !== nums.length
};