/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    if (arr.length === 0) {
        return [];
    }
    const result = [];
    let innerArr = [arr[0]];
    for (let i = 1; i < arr.length; i++) {
        if (i % size === 0) {
            result.push(innerArr);
            innerArr = [];
        }
        innerArr.push(arr[i]);
    }
    if (innerArr.length > 0) {
        result.push(innerArr);
    }
    return result;
};