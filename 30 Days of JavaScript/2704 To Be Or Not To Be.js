/**
 * @param {string} val
 * @return {Object}
 */
const expect = function(val) {
    const initVal = val;
    const toBe = (v) => {
        if (v === initVal) {
            return true;
        }
        throw new Error("Not Equal");
    };
    const notToBe = (v) => {
        if (v !== initVal) {
            return true;
        }
        throw new Error("Equal");
    };
    return {
        toBe: toBe,
        notToBe: notToBe,
    };
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */