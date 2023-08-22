/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const result = Array.from(arr);
    for (let i = 0; i < result.length; i++) {
        result[i] = fn(result[i], i);
    }
    return result;
};