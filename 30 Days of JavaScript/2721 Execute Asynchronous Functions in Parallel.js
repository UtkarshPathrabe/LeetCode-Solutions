/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = async function(functions) {
    return new Promise((resolve, reject) => {
        if (functions.length === 0) {
            resolve([]);
            return;
        }
        const result = new Array(functions.length).fill(null);
        let resolvedCount = 0;
        functions.forEach(async (fn, index) => {
            try {
                result[index] = await fn();
                resolvedCount += 1;
                if (resolvedCount === functions.length) {
                    resolve(result);
                }
            } catch(error) {
                reject(error);
            }
        });
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */