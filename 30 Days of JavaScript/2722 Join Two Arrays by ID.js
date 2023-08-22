/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
const mergeTwoObjects = (obj1, obj2) => {
    const newObj = new Object();
    for (const key of Object.keys(obj2)) {
        newObj[key] = obj2[key];
    }
    for (const key of Object.keys(obj1)) {
        if (!newObj.hasOwnProperty(key)) {
            newObj[key] = obj1[key];
        }
    }
    return newObj;
};
var join = function(arr1, arr2) {
    let result = [];
    const arr1HashMap = new Map();
    for (const obj of arr1) {
        arr1HashMap.set(obj.id, obj);
    }
    const arr2HashMap = new Map();
    for (const obj of arr2) {
        arr2HashMap.set(obj.id, obj);
    }
    for (const obj of arr1) {
        if (arr2HashMap.has(obj.id)) {
            result.push(mergeTwoObjects(obj, arr2HashMap.get(obj.id)));
        }
        else {
            result.push(obj);
        }
    }
    for (const obj of arr2) {
        if (!arr1HashMap.has(obj.id)) {
            result.push(obj);
        }
    }
    result.sort((a, b) => Number(a.id) - Number(b.id));
    return result;
};