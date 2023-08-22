/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    const hashMap = new Map();
    let key;
    let val;
    for (let i = 0; i < this.length; i++) {
        key = fn(this[i]);
        if (hashMap.has(key)) {
            val = hashMap.get(key);
            val.push(this[i]);
            hashMap.set(key, val);
        }
        else {
            hashMap.set(key, [this[i]]);
        }
    }
    return Object.fromEntries(hashMap.entries());
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */