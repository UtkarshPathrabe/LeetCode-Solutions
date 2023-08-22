/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    const hashMap = new Map();
    const transArr = [];
    let val;
    for (let i = 0; i < arr.length; i++) {
        val = fn(arr[i]);
        transArr.push(val);
        hashMap.set(val, arr[i]);
    }
    transArr.sort((a, b) => (Number(a) - Number(b)));
    const result = [];
    for (let i = 0; i < transArr.length; i++) {
        result.push(hashMap.get(transArr[i]));
    }
    return result;
};