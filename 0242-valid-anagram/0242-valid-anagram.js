/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    //first approach 
    const sort = (str) => str.split("").sort().join("")
    return sort(s) === sort(t)
};