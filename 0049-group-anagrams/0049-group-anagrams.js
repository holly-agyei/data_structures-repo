/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    dict = {}
    const sort = (t)=>t.split("").sort().join()

    for( const word of strs){
        const key = sort(word)
        if(dict.hasOwnProperty(key)){
            dict[key].push(word)
        }else{
        dict[key] = [word] //put the word itself first
    }
    }

    //extract all the keys into an array
    array = []
    for (const [key, value] of Object.entries(dict)){
        array.push(value)
    }
    return array 
};

